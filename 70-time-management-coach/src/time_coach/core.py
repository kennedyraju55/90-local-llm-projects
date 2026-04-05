"""Core business logic for Time Management Coach."""

import sys
import os
import csv
import json
import logging
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import chat, generate, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PRODUCTIVITY_CATEGORIES = {
    "deep_work": {
        "activities": ["coding", "writing", "design", "research", "architecture"],
        "target_pct": 50,
        "description": "Focused, high-value creative work",
    },
    "shallow_work": {
        "activities": ["email", "meetings", "admin", "planning", "slack"],
        "target_pct": 30,
        "description": "Necessary but low-cognitive-demand tasks",
    },
    "breaks": {
        "activities": ["lunch", "break", "exercise", "walk", "rest"],
        "target_pct": 20,
        "description": "Recovery and wellness activities",
    },
}

POMODORO_DEFAULTS = {
    "work_minutes": 25,
    "short_break": 5,
    "long_break": 15,
    "sessions_before_long": 4,
}

TIME_BLOCKS = [
    {"block": "Morning Focus",   "start": "08:00", "end": "10:00", "type": "deep_work"},
    {"block": "Mid-Morning",     "start": "10:00", "end": "11:00", "type": "shallow_work"},
    {"block": "Late Morning",    "start": "11:00", "end": "12:00", "type": "deep_work"},
    {"block": "Lunch Break",     "start": "12:00", "end": "13:00", "type": "break"},
    {"block": "Early Afternoon", "start": "13:00", "end": "15:00", "type": "deep_work"},
    {"block": "Mid Afternoon",   "start": "15:00", "end": "16:00", "type": "shallow_work"},
    {"block": "Late Afternoon",  "start": "16:00", "end": "17:00", "type": "deep_work"},
]

DEFAULT_CONFIG = {
    "llm": {"model": "llama3.2", "temperature": 0.6, "max_tokens": 2000},
    "time_log": "timelog.csv",
    "pomodoro": dict(POMODORO_DEFAULTS),
    "productivity": {
        "target_deep_work_hours": 4.0,
        "target_total_hours": 8.0,
        "categories": {
            "deep_work": ["coding", "writing", "design", "research"],
            "shallow_work": ["email", "meetings", "admin"],
            "breaks": ["lunch", "break", "exercise"],
        },
    },
    "scoring": {
        "deep_work_weight": 0.4,
        "consistency_weight": 0.3,
        "balance_weight": 0.3,
    },
    "logging": {"level": "INFO", "file": "time_coach.log"},
}

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

def load_config(config_path: Optional[str] = None) -> dict:
    """Load configuration from a YAML file, falling back to defaults."""
    config = dict(DEFAULT_CONFIG)
    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                user_cfg = yaml.safe_load(f) or {}
            _deep_merge(config, user_cfg)
            logger.info("Loaded config from %s", config_path)
        except Exception as exc:
            logger.warning("Failed to load config %s: %s", config_path, exc)
    return config


def _deep_merge(base: dict, override: dict) -> None:
    """Recursively merge *override* into *base* in place."""
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value

# ---------------------------------------------------------------------------
# Time-log I/O
# ---------------------------------------------------------------------------

def load_timelog(file_path: str) -> list[dict]:
    """Load time log entries from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Time log not found: {file_path}")
    entries = []
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            entries.append(row)
    logger.info("Loaded %d entries from %s", len(entries), file_path)
    return entries


def save_time_entry(entry: dict, log_file: str) -> dict:
    """Append a single time entry to the CSV log, creating the file if needed."""
    fieldnames = ["date", "category", "activity", "duration"]
    file_exists = os.path.exists(log_file)
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        row = {k: entry.get(k, "") for k in fieldnames}
        writer.writerow(row)
    logger.info("Saved entry to %s: %s", log_file, row)
    return row

# ---------------------------------------------------------------------------
# Computation helpers
# ---------------------------------------------------------------------------

def _parse_duration(raw: str) -> float:
    """Parse a duration string like '3.0', '2h', '1.5hr' into float hours."""
    try:
        return float(str(raw).replace("h", "").replace("hr", "").strip())
    except (ValueError, TypeError):
        return 0.0


def compute_time_breakdown(entries: list[dict]) -> dict:
    """Compute total hours per category."""
    breakdown: dict[str, float] = defaultdict(float)
    for entry in entries:
        category = entry.get("category", entry.get("Category", "Uncategorized"))
        duration = _parse_duration(
            entry.get("duration", entry.get("Duration", entry.get("hours", "0")))
        )
        breakdown[category] += duration
    return dict(sorted(breakdown.items(), key=lambda x: x[1], reverse=True))


def compute_daily_totals(entries: list[dict]) -> dict:
    """Compute total hours per day."""
    daily: dict[str, float] = defaultdict(float)
    for entry in entries:
        date = entry.get("date", entry.get("Date", "unknown"))
        duration = _parse_duration(
            entry.get("duration", entry.get("Duration", entry.get("hours", "0")))
        )
        daily[date] += duration
    return dict(sorted(daily.items()))


def compute_productivity_score(breakdown: dict, config: Optional[dict] = None) -> dict:
    """Compute a productivity score (1-10) with contributing factors.

    Returns dict with keys: score, factors, suggestions.
    """
    cfg = config or DEFAULT_CONFIG
    scoring = cfg.get("scoring", DEFAULT_CONFIG["scoring"])
    prod_cfg = cfg.get("productivity", DEFAULT_CONFIG["productivity"])
    categories = prod_cfg.get("categories", DEFAULT_CONFIG["productivity"]["categories"])
    target_deep = prod_cfg.get("target_deep_work_hours", 4.0)
    target_total = prod_cfg.get("target_total_hours", 8.0)

    total_hours = sum(breakdown.values())

    # Deep-work ratio
    deep_cats = [c.lower() for c in categories.get("deep_work", [])]
    deep_hours = sum(v for k, v in breakdown.items() if k.lower() in deep_cats)
    deep_ratio = min(deep_hours / target_deep, 1.0) if target_deep else 0.0

    # Consistency (how close total is to target)
    consistency = 1.0 - min(abs(total_hours - target_total) / target_total, 1.0) if target_total else 0.0

    # Balance (break presence)
    break_cats = [c.lower() for c in categories.get("breaks", [])]
    break_hours = sum(v for k, v in breakdown.items() if k.lower() in break_cats)
    balance = min(break_hours / (target_total * 0.15), 1.0) if target_total else 0.0

    raw = (
        deep_ratio * scoring.get("deep_work_weight", 0.4)
        + consistency * scoring.get("consistency_weight", 0.3)
        + balance * scoring.get("balance_weight", 0.3)
    )
    score = round(max(1.0, min(10.0, raw * 10)), 1)

    factors = {
        "deep_work_hours": round(deep_hours, 1),
        "deep_work_ratio": round(deep_ratio, 2),
        "total_hours": round(total_hours, 1),
        "consistency": round(consistency, 2),
        "balance": round(balance, 2),
    }

    suggestions = []
    if deep_ratio < 0.6:
        suggestions.append(f"Increase deep work — currently {deep_hours:.1f}h vs {target_deep:.1f}h target.")
    if consistency < 0.5:
        suggestions.append(f"Total hours ({total_hours:.1f}h) deviate significantly from {target_total:.1f}h target.")
    if balance < 0.3:
        suggestions.append("Schedule more breaks to sustain energy throughout the day.")

    return {"score": score, "factors": factors, "suggestions": suggestions}


def generate_time_blocks(tasks: str, available_hours: float = 8.0,
                         config: Optional[dict] = None) -> str:
    """Use AI to suggest an optimal time-blocked schedule."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", DEFAULT_CONFIG["llm"])
    blocks_desc = json.dumps(TIME_BLOCKS, indent=2)

    prompt = f"""Create an optimal time-blocked daily schedule.

Tasks: {tasks}
Available hours: {available_hours}
Suggested block template:
{blocks_desc}

For each block:
1. Assign the most appropriate task based on energy levels
2. Specify start/end times
3. Label block type (deep work, shallow work, break)
4. Add brief rationale

Format as a clear markdown table with columns: Time, Task, Type, Rationale."""

    return generate(
        prompt=prompt,
        system_prompt="You are a time-blocking expert. Design schedules that maximize deep-work sessions in high-energy periods.",
        model=llm.get("model"),
        temperature=llm.get("temperature", 0.6),
    )


def analyze_time_usage(entries: list[dict], breakdown: dict, daily: dict,
                       config: Optional[dict] = None) -> str:
    """Use AI to analyze time-usage patterns."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", DEFAULT_CONFIG["llm"])
    summary = {
        "category_breakdown": breakdown,
        "daily_totals": daily,
        "total_entries": len(entries),
        "total_hours": sum(breakdown.values()),
        "avg_daily_hours": sum(daily.values()) / max(len(daily), 1),
    }

    prompt = f"""Analyze this time usage data:

{json.dumps(summary, indent=2)}

Provide:
1. **Time Usage Assessment**: How efficiently is time being spent?
2. **Productivity Score**: Rate 1-10 with reasoning
3. **Time Wasters**: Identify areas consuming disproportionate time
4. **Deep Work Analysis**: How much time is spent on focused, high-value work?
5. **Optimization Suggestions**: Specific, actionable time management tips
6. **Ideal Schedule**: Suggest an optimized daily schedule
7. **Work-Life Balance**: Assessment and recommendations

Be specific with numbers. Format in markdown."""

    return generate(
        prompt=prompt,
        system_prompt="You are an expert time management coach and productivity consultant. Provide data-driven, actionable advice.",
        model=llm.get("model"),
        temperature=llm.get("temperature", 0.6),
    )


def get_tips(goal: str, config: Optional[dict] = None) -> str:
    """Get AI time-management tips for a specific goal."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", DEFAULT_CONFIG["llm"])

    prompt = f"""Provide expert time management tips for this goal: "{goal}"

Include:
1. **Understanding the Goal**: What achieving this requires
2. **Time Blocking Strategy**: How to block time for this goal
3. **Top 5 Techniques**: Specific methods (Pomodoro, time boxing, etc.)
4. **Common Pitfalls**: Mistakes to avoid
5. **Daily Routine Suggestion**: Ideal daily schedule for this goal
6. **Tools & Resources**: Helpful tools and techniques
7. **Progress Metrics**: How to measure improvement

Be practical and actionable. Format in markdown."""

    return generate(
        prompt=prompt,
        system_prompt="You are a world-class time management coach. Provide practical, evidence-based productivity advice.",
        model=llm.get("model"),
        temperature=llm.get("temperature", 0.7),
    )


def generate_pomodoro_plan(tasks: str, available_hours: float = 8.0,
                           config: Optional[dict] = None) -> str:
    """Generate a Pomodoro-based daily plan."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", DEFAULT_CONFIG["llm"])
    pom = cfg.get("pomodoro", POMODORO_DEFAULTS)

    prompt = f"""Create a Pomodoro-based daily plan for these tasks:

Tasks: {tasks}
Available Hours: {available_hours}
Pomodoro Settings: {pom['work_minutes']}min work / {pom['short_break']}min break / {pom['long_break']}min long break every {pom['sessions_before_long']} sessions

For each task:
1. Estimate number of Pomodoro sessions ({pom['work_minutes']} min each)
2. Assign priority (High/Medium/Low)
3. Suggest optimal time of day
4. Include short and long breaks

Format as a clear schedule in markdown."""

    return generate(
        prompt=prompt,
        system_prompt="You are a Pomodoro technique expert.",
        model=llm.get("model"),
        temperature=llm.get("temperature", 0.5),
    )


def generate_weekly_review(entries: list[dict],
                           config: Optional[dict] = None) -> str:
    """Generate a comprehensive AI weekly review."""
    cfg = config or DEFAULT_CONFIG
    llm = cfg.get("llm", DEFAULT_CONFIG["llm"])
    breakdown = compute_time_breakdown(entries)
    daily = compute_daily_totals(entries)
    score_info = compute_productivity_score(breakdown, cfg)
    focus = get_focus_time_stats(entries, cfg)

    summary = {
        "category_breakdown": breakdown,
        "daily_totals": daily,
        "total_hours": sum(breakdown.values()),
        "days_tracked": len(daily),
        "avg_daily_hours": sum(daily.values()) / max(len(daily), 1),
        "productivity_score": score_info["score"],
        "focus_stats": focus,
    }

    prompt = f"""Generate a comprehensive weekly review from this data:

{json.dumps(summary, indent=2)}

Include:
1. **Weekly Summary**: Key stats at a glance
2. **Productivity Score**: {score_info['score']}/10 — explain what drove the score
3. **Category Analysis**: Where time went and whether it aligns with goals
4. **Deep Work Assessment**: Quality and quantity of focused work
5. **Trends**: Any patterns across days
6. **Top 3 Wins**: Positive highlights
7. **Top 3 Areas for Improvement**: Actionable next steps
8. **Next Week Plan**: Recommendations for the upcoming week

Format in markdown."""

    return generate(
        prompt=prompt,
        system_prompt="You are a productivity coach specializing in weekly reviews. Be encouraging but honest.",
        model=llm.get("model"),
        temperature=llm.get("temperature", 0.6),
    )


def get_focus_time_stats(entries: list[dict],
                         config: Optional[dict] = None) -> dict:
    """Calculate deep/focus work statistics.

    Returns dict with deep_work_hours, total_hours, focus_ratio.
    """
    cfg = config or DEFAULT_CONFIG
    prod_cfg = cfg.get("productivity", DEFAULT_CONFIG["productivity"])
    deep_cats = [c.lower() for c in prod_cfg.get("categories", {}).get("deep_work", [])]

    deep_hours = 0.0
    total_hours = 0.0
    for entry in entries:
        cat = entry.get("category", entry.get("Category", "")).lower()
        dur = _parse_duration(
            entry.get("duration", entry.get("Duration", entry.get("hours", "0")))
        )
        total_hours += dur
        if cat in deep_cats:
            deep_hours += dur

    focus_ratio = deep_hours / total_hours if total_hours > 0 else 0.0
    return {
        "deep_work_hours": round(deep_hours, 2),
        "total_hours": round(total_hours, 2),
        "focus_ratio": round(focus_ratio, 2),
    }


def get_category_breakdown(entries: list[dict], period_days: int = 7) -> dict:
    """Return per-category hours filtered to the last *period_days* days."""
    cutoff = datetime.now() - timedelta(days=period_days)
    filtered = []
    for entry in entries:
        raw_date = entry.get("date", entry.get("Date", ""))
        try:
            entry_date = datetime.strptime(raw_date, "%Y-%m-%d")
            if entry_date >= cutoff:
                filtered.append(entry)
        except (ValueError, TypeError):
            filtered.append(entry)
    return compute_time_breakdown(filtered)


def compute_trends(entries: list[dict], weeks: int = 4) -> dict:
    """Compute week-over-week trends for the last *weeks* weeks.

    Returns dict mapping ISO week labels to category breakdowns.
    """
    weekly: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        raw_date = entry.get("date", entry.get("Date", ""))
        try:
            entry_date = datetime.strptime(raw_date, "%Y-%m-%d")
        except (ValueError, TypeError):
            continue
        iso = entry_date.isocalendar()
        week_label = f"{iso[0]}-W{iso[1]:02d}"
        weekly[week_label].append(entry)

    sorted_weeks = sorted(weekly.keys())[-weeks:]
    trends: dict[str, dict] = {}
    for wk in sorted_weeks:
        trends[wk] = compute_time_breakdown(weekly[wk])
    return trends
