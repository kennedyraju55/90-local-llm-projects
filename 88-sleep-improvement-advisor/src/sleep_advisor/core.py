"""
Sleep Improvement Advisor - Core logic for sleep analysis and recommendations.

⚠️  DISCLAIMER: This tool is for educational and informational purposes only and
is NOT medical advice. It does NOT diagnose or treat sleep disorders. Always consult
a qualified healthcare provider for sleep-related health concerns.
"""

from typing import Optional, List, Dict, Any, Tuple, Union
import sys
import os
import csv
import logging
from datetime import datetime, timedelta
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate, chat, check_ollama_running

logger = logging.getLogger(__name__)

DISCLAIMER = (
    "[bold red]⚠️  MEDICAL DISCLAIMER:[/bold red] This tool provides AI-generated sleep "
    "improvement suggestions for [bold]informational purposes only[/bold]. It is [bold]NOT "
    "medical advice[/bold] and does [bold]NOT[/bold] diagnose or treat sleep disorders. "
    "If you have persistent sleep problems, please consult a qualified healthcare provider."
)

SYSTEM_PROMPT = """You are a knowledgeable sleep science advisor with expertise in
sleep hygiene and circadian rhythm management.

When providing sleep advice, always include:
1. **Analysis**: Clear assessment of sleep patterns or issues described.
2. **Evidence-Based Recommendations**: Actionable tips backed by sleep research.
3. **Sleep Hygiene Tips**: Practical habits for better sleep quality.
4. **Lifestyle Factors**: How diet, exercise, stress, and environment affect sleep.
5. **When to Seek Help**: Signs that professional medical evaluation is warranted.

Format your response in clean Markdown with clear section headers.
Be empathetic, practical, and evidence-based.

CRITICAL: Always remind users that your advice is NOT a substitute for professional
medical evaluation. Persistent sleep problems should be discussed with a healthcare
provider who can rule out sleep disorders like sleep apnea, insomnia, or restless
leg syndrome."""

ASSESSMENT_QUESTIONS = [
    {
        "key": "bedtime",
        "question": "What time do you typically go to bed?",
        "type": "text",
        "example": "e.g., 11:00 PM",
    },
    {
        "key": "waketime",
        "question": "What time do you typically wake up?",
        "type": "text",
        "example": "e.g., 7:00 AM",
    },
    {
        "key": "fall_asleep_time",
        "question": "How long does it usually take you to fall asleep (in minutes)?",
        "type": "int",
    },
    {
        "key": "wake_during_night",
        "question": "How many times do you typically wake up during the night?",
        "type": "int",
    },
    {
        "key": "sleep_quality",
        "question": "Rate your overall sleep quality (1=very poor, 5=excellent)",
        "type": "int",
    },
    {
        "key": "caffeine",
        "question": "Do you consume caffeine? If so, how late in the day?",
        "type": "text",
        "example": "e.g., 'Yes, until 3 PM' or 'No'",
    },
    {
        "key": "screen_time",
        "question": "Do you use screens (phone/TV/computer) within 1 hour of bedtime?",
        "type": "text",
        "example": "e.g., 'Yes, about 30 min' or 'No'",
    },
    {
        "key": "exercise",
        "question": "Do you exercise regularly? When during the day?",
        "type": "text",
        "example": "e.g., 'Yes, mornings' or 'No'",
    },
    {
        "key": "environment",
        "question": "Describe your sleep environment (dark, quiet, temperature, etc.)",
        "type": "text",
        "example": "e.g., 'Dark room, a bit warm, some street noise'",
    },
    {
        "key": "concerns",
        "question": "Any specific sleep concerns or issues?",
        "type": "text",
        "example": "e.g., 'Trouble falling asleep, racing thoughts'",
    },
]

ENVIRONMENT_CHECKLIST = [
    {
        "category": "Light",
        "item": "Blackout curtains",
        "recommendation": "Install blackout curtains or shades to block all external light sources.",
        "priority": "high",
    },
    {
        "category": "Light",
        "item": "No LED lights",
        "recommendation": "Cover or remove LED indicator lights from electronics in the bedroom.",
        "priority": "medium",
    },
    {
        "category": "Sound",
        "item": "White noise machine",
        "recommendation": "Use a white noise machine or fan to mask disruptive sounds.",
        "priority": "medium",
    },
    {
        "category": "Sound",
        "item": "Earplugs",
        "recommendation": "Keep earplugs available for noisy environments or travel.",
        "priority": "low",
    },
    {
        "category": "Temperature",
        "item": "Room temperature 65-68°F",
        "recommendation": "Keep bedroom temperature between 65-68°F (18-20°C) for optimal sleep.",
        "priority": "high",
    },
    {
        "category": "Bedding",
        "item": "Comfortable mattress",
        "recommendation": "Invest in a quality mattress that supports your sleeping position. Replace every 7-10 years.",
        "priority": "high",
    },
    {
        "category": "Bedding",
        "item": "Supportive pillows",
        "recommendation": "Choose pillows that keep your neck aligned with your spine.",
        "priority": "medium",
    },
    {
        "category": "Air",
        "item": "Ventilation",
        "recommendation": "Ensure adequate airflow; crack a window or use a fan for fresh air circulation.",
        "priority": "medium",
    },
    {
        "category": "Air",
        "item": "Humidity control",
        "recommendation": "Maintain 30-50% humidity with a humidifier or dehumidifier as needed.",
        "priority": "low",
    },
    {
        "category": "Electronics",
        "item": "No screens 1 hour before bed",
        "recommendation": "Stop using phones, tablets, and computers at least 60 minutes before bedtime.",
        "priority": "high",
    },
    {
        "category": "Electronics",
        "item": "Phone outside bedroom",
        "recommendation": "Charge your phone outside the bedroom to avoid late-night checking.",
        "priority": "medium",
    },
]


def parse_sleep_log(filepath: str) -> list[dict]:
    """Parse a sleep log CSV file.

    Expected CSV columns: date, bedtime, waketime, quality_rating, notes

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of sleep log entry dictionaries.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If required columns are missing.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Sleep log file not found: {filepath}")

    entries = []
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError("CSV file is empty or has no headers.")

        required_cols = {"date", "bedtime", "waketime", "quality_rating"}
        actual_cols = {col.strip().lower() for col in reader.fieldnames}
        missing = required_cols - actual_cols
        if missing:
            raise ValueError(
                f"CSV is missing required columns: {', '.join(missing)}. "
                f"Expected: date, bedtime, waketime, quality_rating, notes"
            )

        for row in reader:
            normalized = {k.strip().lower(): v.strip() for k, v in row.items()}
            entries.append(normalized)

    if not entries:
        raise ValueError("CSV file contains no data entries.")

    logger.info("Parsed %d sleep log entries from %s", len(entries), filepath)
    return entries


def compute_sleep_stats(entries: list[dict]) -> dict:
    """Compute summary statistics from sleep log entries.

    Args:
        entries: List of sleep log entry dictionaries.

    Returns:
        Dictionary containing sleep statistics.
    """
    durations = []
    qualities = []

    for entry in entries:
        try:
            quality = float(entry.get("quality_rating", 0))
            qualities.append(quality)
        except (ValueError, TypeError):
            pass

        try:
            bedtime_str = entry.get("bedtime", "")
            waketime_str = entry.get("waketime", "")
            if bedtime_str and waketime_str:
                bed = datetime.strptime(bedtime_str, "%H:%M")
                wake = datetime.strptime(waketime_str, "%H:%M")
                if wake < bed:
                    wake += timedelta(days=1)
                duration_hours = (wake - bed).total_seconds() / 3600
                durations.append(duration_hours)
        except (ValueError, TypeError):
            pass

    stats = {
        "total_entries": len(entries),
        "avg_duration": round(sum(durations) / len(durations), 1) if durations else None,
        "min_duration": round(min(durations), 1) if durations else None,
        "max_duration": round(max(durations), 1) if durations else None,
        "avg_quality": round(sum(qualities) / len(qualities), 1) if qualities else None,
        "min_quality": min(qualities) if qualities else None,
        "max_quality": max(qualities) if qualities else None,
        "durations": durations,
        "qualities": qualities,
    }

    logger.info("Computed stats: avg_duration=%.1f, avg_quality=%.1f",
                stats.get("avg_duration") or 0, stats.get("avg_quality") or 0)
    return stats


def calculate_sleep_score(stats: dict) -> dict:
    """Calculate a sleep score from 0-100 based on sleep statistics.

    Scoring breakdown:
    - Duration (30 pts): 7-9 hours optimal
    - Quality (25 pts): rating 4-5 is optimal
    - Consistency (20 pts): low variation in duration
    - Wake count proxy (25 pts): derived from quality pattern

    Args:
        stats: Dictionary from compute_sleep_stats().

    Returns:
        Dictionary with score, grade, and breakdown.
    """
    breakdown = {}
    total = 0

    # Duration score (30 points): 7-9 hours optimal
    avg_dur = stats.get("avg_duration")
    if avg_dur is not None:
        if 7.0 <= avg_dur <= 9.0:
            dur_score = 30
        elif 6.0 <= avg_dur < 7.0 or 9.0 < avg_dur <= 10.0:
            dur_score = 20
        elif 5.0 <= avg_dur < 6.0 or 10.0 < avg_dur <= 11.0:
            dur_score = 10
        else:
            dur_score = 5
    else:
        dur_score = 0
    breakdown["duration"] = dur_score
    total += dur_score

    # Quality score (25 points): rating 4-5 optimal
    avg_qual = stats.get("avg_quality")
    if avg_qual is not None:
        if avg_qual >= 4.0:
            qual_score = 25
        elif avg_qual >= 3.0:
            qual_score = 15
        elif avg_qual >= 2.0:
            qual_score = 8
        else:
            qual_score = 3
    else:
        qual_score = 0
    breakdown["quality"] = qual_score
    total += qual_score

    # Consistency score (20 points): low std deviation in duration
    durations = stats.get("durations", [])
    if len(durations) >= 2:
        mean_d = sum(durations) / len(durations)
        variance = sum((d - mean_d) ** 2 for d in durations) / len(durations)
        std_dev = variance ** 0.5
        if std_dev <= 0.5:
            cons_score = 20
        elif std_dev <= 1.0:
            cons_score = 15
        elif std_dev <= 1.5:
            cons_score = 10
        else:
            cons_score = 5
    else:
        cons_score = 10  # neutral for insufficient data
    breakdown["consistency"] = cons_score
    total += cons_score

    # Wake count proxy (25 points): use quality distribution as proxy
    qualities = stats.get("qualities", [])
    if qualities:
        low_quality_ratio = sum(1 for q in qualities if q <= 2) / len(qualities)
        if low_quality_ratio <= 0.1:
            wake_score = 25
        elif low_quality_ratio <= 0.25:
            wake_score = 18
        elif low_quality_ratio <= 0.5:
            wake_score = 10
        else:
            wake_score = 5
    else:
        wake_score = 0
    breakdown["low_wake_count"] = wake_score
    total += wake_score

    # Grade assignment
    if total >= 90:
        grade = "A"
    elif total >= 80:
        grade = "B"
    elif total >= 65:
        grade = "C"
    elif total >= 50:
        grade = "D"
    else:
        grade = "F"

    result = {"score": total, "grade": grade, "breakdown": breakdown}
    logger.info("Sleep score: %d (%s)", total, grade)
    return result


def get_environment_checklist() -> list[dict]:
    """Return the sleep environment optimization checklist.

    Returns:
        List of dictionaries with category, item, recommendation, priority.
    """
    return list(ENVIRONMENT_CHECKLIST)


def build_bedtime_routine(wake_time: str, sleep_duration: float = 8.0) -> dict:
    """Build a personalized bedtime routine based on desired wake time.

    Args:
        wake_time: Desired wake time in HH:MM format (24-hour).
        sleep_duration: Desired sleep duration in hours (default 8.0).

    Returns:
        Dictionary with calculated bedtime and routine timeline.
    """
    wake_dt = datetime.strptime(wake_time, "%H:%M")
    sleep_hours = int(sleep_duration)
    sleep_minutes = int((sleep_duration - sleep_hours) * 60)
    bedtime_dt = wake_dt - timedelta(hours=sleep_hours, minutes=sleep_minutes)

    routine_activities = [
        {"offset_min": -120, "activity": "Last caffeine intake cutoff", "duration": "N/A"},
        {"offset_min": -90, "activity": "Light stretching or gentle yoga", "duration": "15 min"},
        {"offset_min": -60, "activity": "Stop all screen usage", "duration": "N/A"},
        {"offset_min": -45, "activity": "Take a warm bath or shower", "duration": "15 min"},
        {"offset_min": -30, "activity": "Dim lights, start relaxation", "duration": "10 min"},
        {"offset_min": -20, "activity": "Read a physical book or journal", "duration": "15 min"},
        {"offset_min": -10, "activity": "Breathing exercises or meditation", "duration": "10 min"},
        {"offset_min": -5, "activity": "Final bedroom preparation (temperature, darkness)", "duration": "5 min"},
        {"offset_min": 0, "activity": "Lights out - bedtime", "duration": "N/A"},
    ]

    timeline = []
    for item in routine_activities:
        activity_time = bedtime_dt + timedelta(minutes=item["offset_min"])
        timeline.append({
            "time": activity_time.strftime("%H:%M"),
            "activity": item["activity"],
            "duration": item["duration"],
        })

    result = {
        "wake_time": wake_time,
        "bedtime": bedtime_dt.strftime("%H:%M"),
        "sleep_duration": sleep_duration,
        "routine": timeline,
    }

    logger.info("Built routine: wake=%s, bed=%s, duration=%.1f",
                wake_time, result["bedtime"], sleep_duration)
    return result


def analyze_weekly_patterns(entries: list[dict]) -> dict:
    """Analyze sleep patterns by day of week.

    Args:
        entries: List of sleep log entry dictionaries with 'date' field.

    Returns:
        Dictionary with day-of-week averages, best/worst days,
        weekday vs weekend comparison, and trend analysis.
    """
    day_durations = defaultdict(list)
    day_qualities = defaultdict(list)
    chronological_qualities = []

    for entry in entries:
        date_str = entry.get("date", "")
        if not date_str:
            continue

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            logger.warning("Skipping entry with unparseable date: %s", date_str)
            continue

        day_name = date_obj.strftime("%A")

        # Parse duration
        try:
            bedtime_str = entry.get("bedtime", "")
            waketime_str = entry.get("waketime", "")
            if bedtime_str and waketime_str:
                bed = datetime.strptime(bedtime_str, "%H:%M")
                wake = datetime.strptime(waketime_str, "%H:%M")
                if wake < bed:
                    wake += timedelta(days=1)
                duration = (wake - bed).total_seconds() / 3600
                day_durations[day_name].append(duration)
        except (ValueError, TypeError):
            pass

        # Parse quality
        try:
            quality = float(entry.get("quality_rating", 0))
            day_qualities[day_name].append(quality)
            chronological_qualities.append(quality)
        except (ValueError, TypeError):
            pass

    # Day-of-week averages
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_averages = {}
    for day in day_order:
        durs = day_durations.get(day, [])
        quals = day_qualities.get(day, [])
        day_averages[day] = {
            "avg_duration": round(sum(durs) / len(durs), 1) if durs else None,
            "avg_quality": round(sum(quals) / len(quals), 1) if quals else None,
            "count": len(quals),
        }

    # Best and worst days by quality
    scored_days = {d: v["avg_quality"] for d, v in day_averages.items() if v["avg_quality"] is not None}
    best_day = max(scored_days, key=scored_days.get) if scored_days else None
    worst_day = min(scored_days, key=scored_days.get) if scored_days else None

    # Weekday vs weekend
    weekday_names = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
    weekend_names = {"Saturday", "Sunday"}

    weekday_quals = [q for d in weekday_names for q in day_qualities.get(d, [])]
    weekend_quals = [q for d in weekend_names for q in day_qualities.get(d, [])]
    weekday_durs = [dur for d in weekday_names for dur in day_durations.get(d, [])]
    weekend_durs = [dur for d in weekend_names for dur in day_durations.get(d, [])]

    weekday_vs_weekend = {
        "weekday_avg_quality": round(sum(weekday_quals) / len(weekday_quals), 1) if weekday_quals else None,
        "weekend_avg_quality": round(sum(weekend_quals) / len(weekend_quals), 1) if weekend_quals else None,
        "weekday_avg_duration": round(sum(weekday_durs) / len(weekday_durs), 1) if weekday_durs else None,
        "weekend_avg_duration": round(sum(weekend_durs) / len(weekend_durs), 1) if weekend_durs else None,
    }

    # Trend analysis (simple: compare first half vs second half)
    if len(chronological_qualities) >= 4:
        mid = len(chronological_qualities) // 2
        first_half = sum(chronological_qualities[:mid]) / mid
        second_half = sum(chronological_qualities[mid:]) / (len(chronological_qualities) - mid)
        diff = second_half - first_half
        if diff > 0.3:
            trend = "improving"
        elif diff < -0.3:
            trend = "declining"
        else:
            trend = "stable"
    else:
        trend = "insufficient_data"

    result = {
        "day_averages": day_averages,
        "best_day": best_day,
        "worst_day": worst_day,
        "weekday_vs_weekend": weekday_vs_weekend,
        "trend": trend,
    }

    logger.info("Weekly patterns: best=%s, worst=%s, trend=%s", best_day, worst_day, trend)
    return result
