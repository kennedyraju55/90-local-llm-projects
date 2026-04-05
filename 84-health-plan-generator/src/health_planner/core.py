"""
Health Plan Generator - Core logic for personalized wellness plan creation.

⚠️  DISCLAIMER: This tool is for INFORMATIONAL and EDUCATIONAL PURPOSES ONLY.
It does NOT provide medical advice, diagnosis, or treatment. Always consult a
qualified healthcare professional before starting any new health, diet, or
exercise program.
"""

from typing import Optional, List, Dict, Any, Tuple, Union
import datetime
import json
import logging
import os
import sys

import yaml

# ---------------------------------------------------------------------------
# Common LLM client import
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import generate, check_ollama_running  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")


def load_config() -> dict:
    """Load configuration from config.yaml, falling back to defaults."""
    defaults = {
        "model": "gemma4",
        "temperature": 0.4,
        "max_tokens": 3000,
    }
    try:
        with open(_CONFIG_PATH, "r", encoding="utf-8") as fh:
            cfg = yaml.safe_load(fh) or {}
            defaults.update(cfg)
    except FileNotFoundError:
        logger.debug("config.yaml not found – using defaults")
    return defaults


# ---------------------------------------------------------------------------
# Medical Disclaimer
# ---------------------------------------------------------------------------
DISCLAIMER = (
    "⚠️  DISCLAIMER: This tool is for INFORMATIONAL and EDUCATIONAL PURPOSES ONLY. "
    "It does NOT provide medical advice, diagnosis, or treatment. The plans generated "
    "are general wellness suggestions and are NOT a substitute for professional medical "
    "guidance. Always consult a qualified healthcare professional before starting any "
    "new health, diet, or exercise program."
)

# ---------------------------------------------------------------------------
# System Prompt
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are a wellness plan assistant. Your role is to generate structured,
general wellness plans based on a user's stated goals and preferences.

For each plan, provide the following sections in Markdown format:

1. **Overview**: A brief summary of the plan and its goals.
2. **Diet Suggestions**: General nutrition guidance aligned with the goal.
3. **Exercise Plan**: Activity recommendations appropriate for the stated lifestyle level.
4. **Sleep Recommendations**: Tips and habits for better sleep.
5. **Stress Management**: Techniques for managing stress.
6. **Sample Weekly Schedule**: A day-by-day outline for one week (use a Markdown table).

CRITICAL RULES:
- You are NOT a doctor. Always include a reminder that this is general wellness information only.
- Never diagnose conditions or prescribe medications.
- Recommend consulting a healthcare professional before starting any new program.
- Tailor the intensity and specifics to the stated lifestyle level and age if provided.
- If the duration is specified, structure the plan for that timeframe."""

# ---------------------------------------------------------------------------
# Goal Milestones
# ---------------------------------------------------------------------------
GOAL_MILESTONES = {
    "weight_loss": [
        {"week": 1, "milestone": "Establish baseline measurements and food diary", "tip": "Take photos and measurements for reference"},
        {"week": 2, "milestone": "Consistent meal planning established", "tip": "Prep meals in advance for the week"},
        {"week": 4, "milestone": "First progress check - expect 2-4 lbs change", "tip": "Focus on trends, not daily fluctuations"},
        {"week": 8, "milestone": "Habits becoming routine, increased energy", "tip": "Try a new healthy recipe each week"},
        {"week": 12, "milestone": "Significant progress checkpoint", "tip": "Reassess goals and adjust plan"},
    ],
    "better_sleep": [
        {"week": 1, "milestone": "Establish consistent sleep/wake times", "tip": "Set alarms for both bedtime and wake time"},
        {"week": 2, "milestone": "Screen-free bedroom routine in place", "tip": "Replace phone with a book before bed"},
        {"week": 4, "milestone": "Noticeable improvement in sleep quality", "tip": "Track your energy levels throughout the day"},
        {"week": 8, "milestone": "Consistent 7-8 hours of quality sleep", "tip": "Fine-tune your sleep environment"},
    ],
    "fitness": [
        {"week": 1, "milestone": "Complete fitness assessment", "tip": "Record baseline: pushups, run time, flexibility"},
        {"week": 2, "milestone": "Consistent workout schedule established", "tip": "Start with 3 days/week minimum"},
        {"week": 4, "milestone": "Increase intensity by 10-15%", "tip": "Add variety to prevent boredom"},
        {"week": 8, "milestone": "Noticeable strength/endurance gains", "tip": "Consider adding a new activity"},
        {"week": 12, "milestone": "Major fitness milestone achieved", "tip": "Set new challenging goals"},
    ],
    "stress_management": [
        {"week": 1, "milestone": "Identify top 3 stress triggers", "tip": "Keep a stress journal for one week"},
        {"week": 2, "milestone": "Daily mindfulness practice established", "tip": "Start with just 5 minutes of meditation"},
        {"week": 4, "milestone": "Stress response noticeably improved", "tip": "Practice deep breathing in stressful moments"},
        {"week": 8, "milestone": "Healthy coping mechanisms are habitual", "tip": "Share techniques with someone you trust"},
    ],
    "general_wellness": [
        {"week": 1, "milestone": "Health baseline assessment complete", "tip": "Note current energy, mood, and habits"},
        {"week": 2, "milestone": "Hydration and nutrition basics in place", "tip": "Aim for 8 glasses of water daily"},
        {"week": 4, "milestone": "Balanced routine established", "tip": "Include movement, nutrition, sleep, and social time"},
        {"week": 8, "milestone": "Sustainable healthy lifestyle forming", "tip": "Celebrate small wins along the way"},
        {"week": 12, "milestone": "Comprehensive wellness habits established", "tip": "Consider setting new advanced goals"},
    ],
}

# ---------------------------------------------------------------------------
# Weekly Check-in Questions
# ---------------------------------------------------------------------------
WEEKLY_CHECKIN_QUESTIONS = [
    "How would you rate your energy level this week? (1-10)",
    "Did you follow your meal plan this week? (mostly/partially/not really)",
    "How many days did you exercise this week?",
    "How would you rate your sleep quality? (1-10)",
    "What was your biggest challenge this week?",
    "What was your biggest win this week?",
    "How is your stress level? (1-10)",
    "Any symptoms or concerns to note?",
    "What would you like to adjust for next week?",
]

# ---------------------------------------------------------------------------
# Progress Tracker
# ---------------------------------------------------------------------------


class ProgressTracker:
    """Track progress toward health goals."""

    def __init__(self) -> None:
        """Init."""
        self.checkins: list[dict] = []
        self.current_week: int = 1
        self.goal: str | None = None
        self.start_date: str | None = None

    def start_plan(self, goal: str) -> None:
        """Initialize tracking for a new plan."""
        self.goal = goal
        self.start_date = datetime.date.today().isoformat()
        self.current_week = 1
        self.checkins = []

    def add_checkin(self, responses: dict) -> dict:
        """Add a weekly check-in."""
        entry = {
            "week": self.current_week,
            "date": datetime.date.today().isoformat(),
            "responses": responses,
        }
        self.checkins.append(entry)
        self.current_week += 1
        return entry

    def get_progress_summary(self) -> dict:
        """Get a summary of progress."""
        if not self.checkins:
            return {"status": "No check-ins recorded yet", "weeks_completed": 0}

        energy_scores = [
            c["responses"].get("energy", 0)
            for c in self.checkins
            if "energy" in c["responses"]
        ]
        sleep_scores = [
            c["responses"].get("sleep", 0)
            for c in self.checkins
            if "sleep" in c["responses"]
        ]

        return {
            "goal": self.goal,
            "start_date": self.start_date,
            "weeks_completed": len(self.checkins),
            "current_week": self.current_week,
            "avg_energy": sum(energy_scores) / len(energy_scores) if energy_scores else None,
            "avg_sleep": sum(sleep_scores) / len(sleep_scores) if sleep_scores else None,
            "total_checkins": len(self.checkins),
        }

    def get_current_milestone(self) -> dict | None:
        """Get the next upcoming milestone."""
        goal_key = self._normalize_goal()
        milestones = GOAL_MILESTONES.get(goal_key, GOAL_MILESTONES["general_wellness"])
        for m in milestones:
            if m["week"] >= self.current_week:
                return m
        return milestones[-1] if milestones else None

    def _normalize_goal(self) -> str:
        """Normalize goal text to a milestone key."""
        if not self.goal:
            return "general_wellness"
        goal_lower = self.goal.lower()
        if any(w in goal_lower for w in ["weight", "lose", "slim", "diet"]):
            return "weight_loss"
        elif any(w in goal_lower for w in ["sleep", "rest", "insomnia"]):
            return "better_sleep"
        elif any(w in goal_lower for w in ["fit", "exercise", "muscle", "strength", "run"]):
            return "fitness"
        elif any(w in goal_lower for w in ["stress", "relax", "calm", "anxiety"]):
            return "stress_management"
        return "general_wellness"

    def to_dict(self) -> dict:
        """Serialize tracker state to a dictionary."""
        return {
            "goal": self.goal,
            "start_date": self.start_date,
            "current_week": self.current_week,
            "checkins": self.checkins,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ProgressTracker":
        """Deserialize tracker state from a dictionary."""
        tracker = cls()
        tracker.goal = data.get("goal")
        tracker.start_date = data.get("start_date")
        tracker.current_week = data.get("current_week", 1)
        tracker.checkins = data.get("checkins", [])
        return tracker


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------


def get_milestones_for_goal(goal: str) -> list[dict]:
    """Get milestones for a given goal."""
    tracker = ProgressTracker()
    tracker.goal = goal
    key = tracker._normalize_goal()
    return GOAL_MILESTONES.get(key, GOAL_MILESTONES["general_wellness"])


def generate_adaptive_recommendation(tracker: ProgressTracker) -> str:
    """Generate adaptive recommendations based on progress."""
    summary = tracker.get_progress_summary()
    recommendations: list[str] = []

    if summary.get("avg_energy") is not None and summary["avg_energy"] < 5:
        recommendations.append(
            "Your energy levels have been low. Consider reviewing sleep habits and nutrition."
        )
    if summary.get("avg_sleep") is not None and summary["avg_sleep"] < 5:
        recommendations.append(
            "Sleep quality needs attention. Try establishing a consistent bedtime routine."
        )
    if summary.get("weeks_completed", 0) > 0:
        recommendations.append(
            f"Great job completing {summary['weeks_completed']} week(s)! Keep the momentum going."
        )

    milestone = tracker.get_current_milestone()
    if milestone:
        recommendations.append(
            f"Next milestone (Week {milestone['week']}): {milestone['milestone']}"
        )
        recommendations.append(f"\U0001f4a1 Tip: {milestone['tip']}")

    return "\n".join(recommendations) if recommendations else "Keep following your plan consistently!"


# ---------------------------------------------------------------------------
# Prompt Building & Plan Generation
# ---------------------------------------------------------------------------


def _build_prompt(
    goal: str,
    age: int | None,
    lifestyle: str | None,
    duration: str | None,
) -> str:
    """Build the prompt for generating a wellness plan."""
    parts = [f"Create a wellness plan for the following goal: {goal}"]

    if age is not None:
        parts.append(f"Age: {age}")
    if lifestyle:
        parts.append(f"Current lifestyle/activity level: {lifestyle}")
    if duration:
        duration_map = {
            "1week": "1 week",
            "1month": "1 month",
            "3months": "3 months",
        }
        parts.append(f"Plan duration: {duration_map.get(duration, duration)}")

    parts.append("\nFormat the plan in clear Markdown with the required sections.")
    return "\n".join(parts)


def generate_plan(
    goal: str,
    age: int | None = None,
    lifestyle: str | None = None,
    duration: str | None = None,
) -> str:
    """Generate a wellness plan using the LLM.

    Args:
        goal: The health/wellness goal.
        age: Optional age of the user.
        lifestyle: Optional activity level (sedentary, moderate, active).
        duration: Optional plan duration (1week, 1month, 3months).

    Returns:
        The LLM-generated wellness plan as a string.
    """
    config = load_config()
    prompt = _build_prompt(goal, age, lifestyle, duration)
    logger.info("Generating plan for goal=%s age=%s lifestyle=%s duration=%s", goal, age, lifestyle, duration)
    response = generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=config.get("temperature", 0.4),
        max_tokens=config.get("max_tokens", 3000),
    )
    return response
