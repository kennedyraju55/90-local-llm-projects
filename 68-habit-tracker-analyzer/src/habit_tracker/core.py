#!/usr/bin/env python3
"""Habit Tracker Analyzer - Core business logic."""

import sys
import os
import json
import logging
from datetime import datetime, timedelta
from collections import defaultdict
from itertools import combinations
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import chat, generate, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Achievement definitions
# ---------------------------------------------------------------------------

ACHIEVEMENTS = {
    "first_log": {
        "name": "First Step",
        "description": "Log your first habit",
        "icon": "🌱",
        "threshold": 1,
    },
    "week_streak": {
        "name": "Week Warrior",
        "description": "7-day streak",
        "icon": "🔥",
        "threshold": 7,
    },
    "month_streak": {
        "name": "Monthly Master",
        "description": "30-day streak",
        "icon": "⭐",
        "threshold": 30,
    },
    "century": {
        "name": "Century Club",
        "description": "100-day streak",
        "icon": "💯",
        "threshold": 100,
    },
    "perfect_week": {
        "name": "Perfect Week",
        "description": "All habits done for 7 days",
        "icon": "🏆",
        "threshold": 7,
    },
    "consistency": {
        "name": "Consistency King",
        "description": "90%+ completion rate for 30 days",
        "icon": "👑",
        "threshold": 90,
    },
}

# ---------------------------------------------------------------------------
# Configuration helpers
# ---------------------------------------------------------------------------

_DEFAULT_CONFIG = {
    "llm": {"model": "llama3.2", "temperature": 0.6, "max_tokens": 2000},
    "habits_file": "habits.json",
    "default_target": "daily",
    "achievements": {"enabled": True, "notifications": True},
    "reports": {"weekly": True, "monthly": True},
    "logging": {"level": "INFO", "file": "habit_tracker.log"},
}


def load_config(config_path: str = "config.yaml") -> dict:
    """Load configuration from YAML, falling back to defaults."""
    config = dict(_DEFAULT_CONFIG)
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_cfg = yaml.safe_load(f) or {}
            for key, val in user_cfg.items():
                if isinstance(val, dict) and isinstance(config.get(key), dict):
                    config[key] = {**config[key], **val}
                else:
                    config[key] = val
        except Exception:
            logger.warning("Failed to load %s, using defaults", config_path)
    return config


def _setup_logging(config: dict) -> None:
    log_cfg = config.get("logging", {})
    """Setup logging."""
    logging.basicConfig(
        level=getattr(logging, log_cfg.get("level", "INFO")),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_cfg.get("file", "habit_tracker.log")),
        ],
    )


# ---------------------------------------------------------------------------
# Data persistence
# ---------------------------------------------------------------------------

def _resolve_habits_file(habits_file: Optional[str] = None, config: Optional[dict] = None) -> str:
    """Resolve habits file."""
    if habits_file:
        return habits_file
    if config:
        return config.get("habits_file", "habits.json")
    return "habits.json"


def load_habits(habits_file: Optional[str] = None) -> dict:
    """Load habits data from JSON file."""
    path = _resolve_habits_file(habits_file)
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            logger.error("Corrupt habits file %s, starting fresh", path)
            return {"habits": {}, "logs": []}
    return {"habits": {}, "logs": []}


def save_habits(data: dict, habits_file: Optional[str] = None) -> None:
    """Save habits data to JSON file."""
    path = _resolve_habits_file(habits_file)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    logger.debug("Saved habits to %s", path)


# ---------------------------------------------------------------------------
# Habit CRUD
# ---------------------------------------------------------------------------

def log_habit(
    habit_name: str,
    done: bool = True,
    notes: str = "",
    habits_file: Optional[str] = None,
) -> dict:
    """Log a habit completion for today."""
    data = load_habits(habits_file)
    habit_key = habit_name.lower().replace(" ", "_")

    if habit_key not in data["habits"]:
        data["habits"][habit_key] = {
            "name": habit_name,
            "created": datetime.now().isoformat(),
            "target": "daily",
            "category": "general",
        }

    log_entry = {
        "habit": habit_key,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M"),
        "done": done,
        "notes": notes,
    }

    data["logs"].append(log_entry)
    save_habits(data, habits_file)
    logger.info("Logged %s: done=%s", habit_key, done)
    return log_entry


def add_habit(
    name: str,
    category: str = "general",
    target: str = "daily",
    habits_file: Optional[str] = None,
) -> dict:
    """Add a new habit definition."""
    data = load_habits(habits_file)
    habit_key = name.lower().replace(" ", "_")

    habit = {
        "name": name,
        "created": datetime.now().isoformat(),
        "target": target,
        "category": category,
    }
    data["habits"][habit_key] = habit
    save_habits(data, habits_file)
    logger.info("Added habit %s (category=%s)", habit_key, category)
    return habit


def delete_habit(habit_key: str, habits_file: Optional[str] = None) -> bool:
    """Delete a habit and all its logs."""
    data = load_habits(habits_file)
    if habit_key not in data["habits"]:
        return False
    del data["habits"][habit_key]
    data["logs"] = [l for l in data["logs"] if l["habit"] != habit_key]
    save_habits(data, habits_file)
    logger.info("Deleted habit %s", habit_key)
    return True


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------

def compute_streaks(data: dict) -> dict:
    """Compute current and best streaks for each habit."""
    streaks = {}
    for habit_key in data["habits"]:
        logs = sorted(
            [l for l in data["logs"] if l["habit"] == habit_key and l["done"]],
            key=lambda x: x["date"],
        )

        if not logs:
            streaks[habit_key] = {"current": 0, "best": 0, "total": 0}
            continue

        dates = sorted(set(l["date"] for l in logs))
        total = len(dates)

        # Current streak (count backwards from today)
        current = 0
        today = datetime.now().strftime("%Y-%m-%d")
        check_date = today
        for _ in range(len(dates)):
            if check_date in dates:
                current += 1
                prev = datetime.strptime(check_date, "%Y-%m-%d") - timedelta(days=1)
                check_date = prev.strftime("%Y-%m-%d")
            else:
                break

        # Best streak
        best = 1
        run = 1
        for i in range(1, len(dates)):
            d1 = datetime.strptime(dates[i - 1], "%Y-%m-%d")
            d2 = datetime.strptime(dates[i], "%Y-%m-%d")
            if (d2 - d1).days == 1:
                run += 1
                best = max(best, run)
            else:
                run = 1

        streaks[habit_key] = {"current": current, "best": best, "total": total}

    return streaks


def get_completion_rate(data: dict, days: int = 30) -> dict:
    """Compute completion rates for each habit over a period."""
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    rates = {}

    for habit_key in data["habits"]:
        recent_logs = [
            l for l in data["logs"]
            if l["habit"] == habit_key and l["date"] >= cutoff
        ]
        done_count = sum(1 for l in recent_logs if l["done"])
        created_str = data["habits"][habit_key].get(
            "created", datetime.now().isoformat()
        )[:10]
        total_days = min(
            days,
            (datetime.now() - datetime.strptime(created_str, "%Y-%m-%d")).days + 1,
        )
        rates[habit_key] = {
            "done": done_count,
            "total_days": total_days,
            "rate": (done_count / total_days * 100) if total_days > 0 else 0,
        }

    return rates


def compute_correlations(data: dict) -> dict:
    """Find which habits are frequently completed on the same day."""
    if len(data["habits"]) < 2:
        return {}

    # Build date -> set of done habits
    day_habits: dict[str, set] = defaultdict(set)
    for log in data["logs"]:
        if log["done"]:
            day_habits[log["date"]].add(log["habit"])

    if not day_habits:
        return {}

    total_days = len(day_habits)
    correlations = {}
    habit_keys = list(data["habits"].keys())

    for h1, h2 in combinations(habit_keys, 2):
        both = sum(1 for habits in day_habits.values() if h1 in habits and h2 in habits)
        correlation = (both / total_days * 100) if total_days > 0 else 0
        pair_key = f"{h1}+{h2}"
        correlations[pair_key] = {
            "habits": [h1, h2],
            "co_occurrence": both,
            "total_days": total_days,
            "rate": round(correlation, 1),
        }

    return correlations


def check_achievements(data: dict) -> list[dict]:
    """Check which achievements have been earned."""
    earned = []
    streaks = compute_streaks(data)
    rates = get_completion_rate(data, 30)

    total_logs = sum(1 for l in data["logs"] if l["done"])

    # first_log
    if total_logs >= ACHIEVEMENTS["first_log"]["threshold"]:
        earned.append({**ACHIEVEMENTS["first_log"], "id": "first_log", "earned": True})

    # streak-based achievements
    for habit_key, streak in streaks.items():
        best = streak.get("best", 0)
        current = streak.get("current", 0)
        max_streak = max(best, current)

        if max_streak >= ACHIEVEMENTS["week_streak"]["threshold"]:
            ach = {**ACHIEVEMENTS["week_streak"], "id": "week_streak",
                   "earned": True, "habit": habit_key}
            if ach not in earned:
                earned.append(ach)

        if max_streak >= ACHIEVEMENTS["month_streak"]["threshold"]:
            ach = {**ACHIEVEMENTS["month_streak"], "id": "month_streak",
                   "earned": True, "habit": habit_key}
            if ach not in earned:
                earned.append(ach)

        if max_streak >= ACHIEVEMENTS["century"]["threshold"]:
            ach = {**ACHIEVEMENTS["century"], "id": "century",
                   "earned": True, "habit": habit_key}
            if ach not in earned:
                earned.append(ach)

    # perfect_week: all habits done every day for the last 7 days
    if data["habits"]:
        all_keys = set(data["habits"].keys())
        perfect_days = 0
        for offset in range(ACHIEVEMENTS["perfect_week"]["threshold"]):
            day = (datetime.now() - timedelta(days=offset)).strftime("%Y-%m-%d")
            done_that_day = {
                l["habit"] for l in data["logs"]
                if l["date"] == day and l["done"]
            }
            if all_keys.issubset(done_that_day):
                perfect_days += 1
            else:
                break
        if perfect_days >= ACHIEVEMENTS["perfect_week"]["threshold"]:
            earned.append({
                **ACHIEVEMENTS["perfect_week"],
                "id": "perfect_week",
                "earned": True,
            })

    # consistency: any habit with 90%+ rate over 30 days
    for habit_key, rate_info in rates.items():
        if rate_info["rate"] >= ACHIEVEMENTS["consistency"]["threshold"]:
            earned.append({
                **ACHIEVEMENTS["consistency"],
                "id": "consistency",
                "earned": True,
                "habit": habit_key,
            })

    return earned


def get_calendar_data(
    data: dict,
    habit_key: str,
    months: int = 3,
) -> dict:
    """Return date->bool mapping for heatmap visualisation."""
    cutoff = datetime.now() - timedelta(days=months * 30)
    calendar: dict[str, bool] = {}

    done_dates = {
        l["date"]
        for l in data["logs"]
        if l["habit"] == habit_key and l["done"]
    }

    current = cutoff
    while current <= datetime.now():
        date_str = current.strftime("%Y-%m-%d")
        calendar[date_str] = date_str in done_dates
        current += timedelta(days=1)

    return calendar


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------

def generate_weekly_report(data: dict, config: Optional[dict] = None) -> str:
    """Generate a weekly summary report."""
    config = config or load_config()
    streaks = compute_streaks(data)
    rates = get_completion_rate(data, 7)
    achievements = check_achievements(data)

    lines = ["# 📊 Weekly Habit Report", ""]
    lines.append(f"**Period**: Last 7 days")
    lines.append(f"**Date**: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("## Streaks")
    for key, info in streaks.items():
        name = data["habits"].get(key, {}).get("name", key)
        lines.append(f"- **{name}**: 🔥 {info['current']} days (best: {info['best']})")

    lines.append("")
    lines.append("## Completion Rates (7 days)")
    for key, info in rates.items():
        name = data["habits"].get(key, {}).get("name", key)
        bar = "█" * int(info["rate"] / 10) + "░" * (10 - int(info["rate"] / 10))
        lines.append(f"- **{name}**: {info['rate']:.0f}% |{bar}|")

    if achievements:
        lines.append("")
        lines.append("## 🏅 Achievements Earned")
        for ach in achievements:
            lines.append(f"- {ach['icon']} **{ach['name']}**: {ach['description']}")

    return "\n".join(lines)


def generate_monthly_report(data: dict, config: Optional[dict] = None) -> str:
    """Generate a monthly summary report."""
    config = config or load_config()
    streaks = compute_streaks(data)
    rates = get_completion_rate(data, 30)
    correlations = compute_correlations(data)
    achievements = check_achievements(data)

    lines = ["# 📊 Monthly Habit Report", ""]
    lines.append(f"**Period**: Last 30 days")
    lines.append(f"**Date**: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("")

    lines.append("## Streaks")
    for key, info in streaks.items():
        name = data["habits"].get(key, {}).get("name", key)
        lines.append(
            f"- **{name}**: 🔥 {info['current']} days "
            f"(best: {info['best']}, total: {info['total']})"
        )

    lines.append("")
    lines.append("## Completion Rates (30 days)")
    for key, info in rates.items():
        name = data["habits"].get(key, {}).get("name", key)
        bar = "█" * int(info["rate"] / 10) + "░" * (10 - int(info["rate"] / 10))
        lines.append(f"- **{name}**: {info['rate']:.0f}% |{bar}|")

    if correlations:
        lines.append("")
        lines.append("## 🔗 Habit Correlations")
        for pair_key, info in correlations.items():
            names = [data["habits"].get(h, {}).get("name", h) for h in info["habits"]]
            lines.append(f"- **{names[0]}** ↔ **{names[1]}**: {info['rate']}% co-occurrence")

    if achievements:
        lines.append("")
        lines.append("## 🏅 Achievements Earned")
        for ach in achievements:
            lines.append(f"- {ach['icon']} **{ach['name']}**: {ach['description']}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# AI Analysis
# ---------------------------------------------------------------------------

def analyze_habits(data: dict, period: str, config: Optional[dict] = None) -> str:
    """Use AI to analyze habit patterns."""
    config = config or load_config()
    streaks = compute_streaks(data)
    days = {"week": 7, "month": 30, "year": 365}.get(period, 30)
    rates = get_completion_rate(data, days)
    correlations = compute_correlations(data)

    summary = {
        "habits": {k: v["name"] for k, v in data["habits"].items()},
        "streaks": streaks,
        "completion_rates": rates,
        "correlations": correlations,
        "period": period,
        "total_logs": len(data["logs"]),
    }

    prompt = f"""Analyze these habit tracking patterns:

{json.dumps(summary, indent=2)}

Provide:
1. **Overall Assessment**: How well are habits being maintained?
2. **Streak Analysis**: Which habits have strong/weak streaks
3. **Completion Patterns**: Best and worst performing habits
4. **Correlation Insights**: Which habits are done together and what that means
5. **Improvement Suggestions**: Specific, actionable tips for each habit
6. **Habit Stacking**: Suggest how to link habits together for better consistency
7. **Motivational Insight**: An encouraging observation

Be specific with numbers and percentages. Format in markdown."""

    llm_cfg = config.get("llm", {})
    return generate(
        prompt=prompt,
        system_prompt=(
            "You are a behavioral science expert and habit coach. "
            "Provide data-driven, supportive habit analysis."
        ),
        temperature=llm_cfg.get("temperature", 0.6),
        max_tokens=llm_cfg.get("max_tokens", 2000),
    )
