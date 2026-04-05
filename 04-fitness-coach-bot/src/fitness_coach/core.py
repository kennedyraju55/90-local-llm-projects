"""Core business logic for Fitness Coach Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))
from common.llm_client import chat, check_ollama_running  # noqa: E402

SYSTEM_PROMPT = """You are a certified personal fitness trainer and exercise physiologist. Your role is to:
1. Create safe, effective workout plans tailored to the user's fitness level
2. Consider available equipment and time constraints
3. Include warm-up and cool-down routines
4. Provide proper form instructions to prevent injury
5. Suggest modifications for different ability levels

Safety guidelines:
- Always recommend consulting a doctor before starting a new program
- Warn about exercises that may be risky for beginners
- Suggest progressive overload and rest days
- Include stretching and mobility work"""

LEVELS = ["beginner", "intermediate", "advanced"]
GOALS = ["weight-loss", "muscle-gain", "endurance", "flexibility", "general-fitness", "strength"]


def generate_workout_plan(
    level: str,
    goal: str,
    equipment: str,
    days_per_week: int = 4,
    session_minutes: int = 45,
    model: str = "gemma4",
    temperature: float = 0.7,
) -> str:
    """Generate a personalized workout plan."""
    logger.info("Generating workout plan: level=%s goal=%s", level, goal)
    prompt = (
        f"Create a {days_per_week}-day per week workout plan.\n"
        f"Fitness Level: {level}\n"
        f"Goal: {goal}\n"
        f"Available Equipment: {equipment}\n"
        f"Session Duration: {session_minutes} minutes\n\n"
        "For each workout day, include:\n"
        "- Warm-up (5 min)\n"
        "- Main exercises with sets, reps, and rest periods\n"
        "- Cool-down stretches (5 min)\n"
        "- Estimated calories burned\n"
        "Include rest days in the schedule."
    )
    messages = [{"role": "user", "content": prompt}]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature, max_tokens=4096)


def get_exercise_details(exercise_name: str, level: str, model: str = "gemma4", temperature: float = 0.7) -> str:
    """Get detailed instructions for a specific exercise."""
    logger.info("Fetching exercise details: %s", exercise_name)
    messages = [
        {
            "role": "user",
            "content": (
                f"Explain how to perform: {exercise_name}\n"
                f"For a {level} level person.\n"
                "Include: proper form, common mistakes, muscles targeted, "
                "modifications for beginners, and progression tips."
            ),
        }
    ]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature, max_tokens=1024)
