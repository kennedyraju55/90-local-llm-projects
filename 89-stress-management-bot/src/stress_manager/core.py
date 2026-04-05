"""
Core logic for the Stress Management Bot.

Provides stress assessment, breathing exercises, CBT worksheets,
coping toolkit, and AI-powered stress management support.

⚠️ DISCLAIMER: This tool is NOT a substitute for professional mental health care.
If you are in crisis, please contact:
  - 988 Suicide & Crisis Lifeline: Call or text 988
  - Crisis Text Line: Text HOME to 741741
  - Emergency Services: Call 911
"""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
import os
import sys
import time

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import chat, generate, check_ollama_running

logger = logging.getLogger(__name__)

console = Console()

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DISCLAIMER = (
    "[bold red]⚠️  IMPORTANT DISCLAIMER[/bold red]\n\n"
    "This tool is [bold]NOT[/bold] a substitute for professional mental health care.\n"
    "It provides general wellness suggestions only and is [bold]NOT medical advice[/bold].\n\n"
    "If you are in crisis, please contact:\n"
    "  • [bold]988 Suicide & Crisis Lifeline[/bold]: Call or text 988\n"
    "  • [bold]Crisis Text Line[/bold]: Text HOME to 741741\n"
    "  • [bold]Emergency Services[/bold]: Call 911"
)

SYSTEM_PROMPT = (
    "You are a compassionate, empathetic stress management assistant. "
    "You use evidence-based techniques from Cognitive Behavioral Therapy (CBT), "
    "mindfulness, and positive psychology to help users manage stress.\n\n"
    "Guidelines:\n"
    "- Be warm, supportive, and non-judgmental.\n"
    "- Suggest practical, evidence-based coping strategies.\n"
    "- Use CBT techniques like cognitive restructuring, thought challenging, "
    "and behavioral activation.\n"
    "- When a user expresses severe distress, suicidal thoughts, or crisis, "
    "ALWAYS recommend they contact professional help immediately "
    "(988 Suicide & Crisis Lifeline, 911, or a licensed therapist).\n"
    "- Remind users that you are an AI tool and NOT a replacement for "
    "professional mental health care.\n"
    "- Keep responses concise but caring.\n"
    "- Suggest breathing exercises, grounding techniques, and journaling "
    "when appropriate."
)

BREATHING_EXERCISES = {
    "box": {
        "name": "Box Breathing",
        "description": "A calming technique used by Navy SEALs to reduce stress.",
        "steps": [
            ("Inhale", 4),
            ("Hold", 4),
            ("Exhale", 4),
            ("Hold", 4),
        ],
        "cycles": 4,
    },
    "478": {
        "name": "4-7-8 Breathing",
        "description": "A relaxation technique that promotes calm and sleep.",
        "steps": [
            ("Inhale through your nose", 4),
            ("Hold your breath", 7),
            ("Exhale through your mouth", 8),
        ],
        "cycles": 3,
    },
}

STRESS_QUESTIONS = [
    ("How would you rate your overall stress level today? (1-10)", 1, 10),
    ("How well did you sleep last night? (1-10, 10=great)", 1, 10),
    ("How would you rate your energy level? (1-10, 10=high)", 1, 10),
    ("How anxious do you feel right now? (1-10, 10=very anxious)", 1, 10),
    ("How well can you concentrate today? (1-10, 10=very well)", 1, 10),
]

CBT_WORKSHEETS = {
    "thought_record": {
        "name": "Thought Record",
        "description": (
            "A core CBT tool for identifying and challenging negative automatic thoughts. "
            "Use this worksheet when you notice a shift in your mood or a strong emotional reaction."
        ),
        "columns": [
            "Situation",
            "Automatic Thought",
            "Emotion",
            "Evidence For",
            "Evidence Against",
            "Balanced Thought",
        ],
    },
    "behavioral_activation": {
        "name": "Behavioral Activation Planner",
        "description": (
            "Schedule and track activities to combat low mood and inactivity. "
            "Rate your predicted and actual enjoyment to identify uplifting activities."
        ),
        "columns": [
            "Activity",
            "Predicted Enjoyment",
            "Actual Enjoyment",
            "Notes",
        ],
    },
    "worry_time": {
        "name": "Worry Time Scheduler",
        "description": (
            "Contain and manage worry by scheduling a dedicated worry period. "
            "Outside this time, practice postponing worries."
        ),
        "steps": [
            "Set a specific 15-20 minute worry period each day.",
            "When worries arise outside this time, write them down and postpone.",
            "During worry time, review your list and think through each worry.",
            "Ask: Is this worry realistic? What can I control?",
            "Create an action plan for controllable worries.",
            "Practice letting go of uncontrollable worries.",
        ],
    },
}

COPING_TOOLKIT = {
    "physical": [
        "Progressive muscle relaxation",
        "Exercise",
        "Deep breathing",
        "Yoga",
        "Walking in nature",
    ],
    "cognitive": [
        "Journaling",
        "Thought challenging",
        "Gratitude listing",
        "Mindfulness meditation",
        "Visualization",
    ],
    "social": [
        "Talk to a friend",
        "Support group",
        "Volunteer work",
        "Quality time with loved ones",
    ],
    "creative": [
        "Art therapy",
        "Music",
        "Writing",
        "Cooking",
        "Gardening",
    ],
}

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def show_disclaimer():
    """Display the mental health disclaimer."""
    console.print(Panel(DISCLAIMER, border_style="red", title="Disclaimer"))
    console.print()


def run_breathing_exercise(exercise_key: str) -> None:
    """Run a guided breathing exercise with timed progress bars."""
    exercise = BREATHING_EXERCISES[exercise_key]
    logger.info("Starting breathing exercise: %s", exercise["name"])

    console.print(Panel(
        f"[bold green]{exercise['name']}[/bold green]\n\n{exercise['description']}",
        border_style="green",
        title="🌬️ Breathing Exercise",
    ))
    console.print()
    console.print("[dim]Get comfortable and follow along...[/dim]\n")
    time.sleep(2)

    for cycle in range(1, exercise["cycles"] + 1):
        console.print(f"[bold blue]--- Cycle {cycle}/{exercise['cycles']} ---[/bold blue]")
        for step_name, duration in exercise["steps"]:
            with Progress(
                TextColumn(f"  [green]{step_name}[/green]"),
                BarColumn(bar_width=40, complete_style="blue", finished_style="green"),
                TextColumn("[bold]{task.completed}/{task.total}s[/bold]"),
                console=console,
            ) as progress:
                task = progress.add_task(step_name, total=duration)
                for _ in range(duration):
                    time.sleep(1)
                    progress.update(task, advance=1)
        console.print()

    console.print("[bold green]✨ Great job! You completed the exercise.[/bold green]\n")
    logger.info("Breathing exercise completed: %s", exercise["name"])


def calculate_stress_score(answers: dict) -> dict:
    """Calculate a detailed stress score from assessment answers.

    Parameters
    ----------
    answers : dict
        Mapping of category name to integer score (1-10).
        Expected keys: stress_level, sleep_quality, energy_level,
        anxiety_level, concentration.

    Returns
    -------
    dict
        total_score, severity, breakdown (per category), recommendations.
    """
    category_order = [
        "stress_level",
        "sleep_quality",
        "energy_level",
        "anxiety_level",
        "concentration",
    ]

    def _severity(score: int) -> str:
        """Severity."""
        if score <= 3:
            return "low"
        if score <= 6:
            return "moderate"
        if score <= 8:
            return "high"
        return "critical"

    breakdown = {}
    for cat in category_order:
        val = answers.get(cat, 0)
        breakdown[cat] = {"score": val, "severity": _severity(val)}

    total_score = sum(answers.get(c, 0) for c in category_order)
    avg = total_score / max(len(category_order), 1)
    overall_severity = _severity(round(avg))

    recommendations: list[str] = []
    if overall_severity == "low":
        recommendations.append("Maintain your healthy habits and keep up the good work!")
        recommendations.append("Consider adding a daily gratitude practice.")
    elif overall_severity == "moderate":
        recommendations.append("Try a daily breathing exercise to manage stress.")
        recommendations.append("Consider journaling to process your thoughts.")
        recommendations.append("Ensure you get 7-9 hours of quality sleep.")
    elif overall_severity == "high":
        recommendations.append("Practice breathing exercises multiple times daily.")
        recommendations.append("Consider speaking with a counselor or therapist.")
        recommendations.append("Limit caffeine and screen time before bed.")
        recommendations.append("Try progressive muscle relaxation before sleep.")
    else:  # critical
        recommendations.append("Please reach out to a mental health professional.")
        recommendations.append("Call 988 Suicide & Crisis Lifeline if you need immediate support.")
        recommendations.append("Talk to a trusted friend or family member today.")
        recommendations.append("Avoid isolation — seek social support.")
        recommendations.append("Contact emergency services (911) if you are in danger.")

    logger.info("Stress score calculated: total=%d, severity=%s", total_score, overall_severity)

    return {
        "total_score": total_score,
        "severity": overall_severity,
        "breakdown": breakdown,
        "recommendations": recommendations,
    }


def get_cbt_worksheet(worksheet_type: str) -> dict:
    """Return a CBT worksheet template by type.

    Parameters
    ----------
    worksheet_type : str
        One of: thought_record, behavioral_activation, worry_time.

    Returns
    -------
    dict
        The worksheet template, or empty dict if not found.
    """
    worksheet = CBT_WORKSHEETS.get(worksheet_type, {})
    if not worksheet:
        logger.warning("Unknown worksheet type requested: %s", worksheet_type)
    return worksheet


def get_coping_suggestions(stress_level: str) -> list:
    """Return coping suggestions appropriate for the given stress severity.

    Parameters
    ----------
    stress_level : str
        One of: low, moderate, high, critical.

    Returns
    -------
    list
        Suggested coping techniques.
    """
    if stress_level == "low":
        suggestions = (
            COPING_TOOLKIT["creative"][:3]
            + COPING_TOOLKIT["social"][:2]
        )
    elif stress_level == "moderate":
        suggestions = (
            COPING_TOOLKIT["physical"][:3]
            + COPING_TOOLKIT["cognitive"][:3]
        )
    elif stress_level in ("high", "critical"):
        suggestions = (
            COPING_TOOLKIT["physical"]
            + COPING_TOOLKIT["cognitive"]
            + COPING_TOOLKIT["social"]
        )
    else:
        suggestions = list(COPING_TOOLKIT["physical"])

    logger.info("Coping suggestions returned for level=%s", stress_level)
    return suggestions
