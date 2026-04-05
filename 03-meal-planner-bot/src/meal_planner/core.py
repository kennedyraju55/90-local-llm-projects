"""Core business logic for Meal Planner Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))
from common.llm_client import chat, check_ollama_running  # noqa: E402

SYSTEM_PROMPT = """You are an expert nutritionist and meal planning assistant. Your role is to:
1. Create balanced, nutritious meal plans tailored to dietary preferences
2. Account for allergies and dietary restrictions
3. Provide complete recipes with ingredients and step-by-step instructions
4. Include estimated prep/cook times and calorie counts
5. Suggest ingredient substitutions when appropriate

Format your meal plans clearly with:
- Day headers
- Breakfast, Lunch, Dinner, and optional Snacks
- Brief recipe descriptions with key ingredients"""

DIETS = [
    "omnivore", "vegetarian", "vegan", "keto", "paleo",
    "mediterranean", "gluten-free", "dairy-free", "pescatarian", "low-carb",
]


def generate_meal_plan(
    diet: str,
    days: int,
    allergies: str | None = None,
    calories: int | None = None,
    model: str = "gemma4",
    temperature: float = 0.7,
) -> str:
    """Generate a meal plan based on preferences."""
    prompt_parts = [
        f"Create a {days}-day meal plan for a {diet} diet.",
        "Include Breakfast, Lunch, Dinner, and one Snack for each day.",
    ]
    if allergies:
        prompt_parts.append(f"IMPORTANT: Avoid these allergens/ingredients: {allergies}")
    if calories:
        prompt_parts.append(f"Target approximately {calories} calories per day.")
    prompt_parts.append("For each meal, provide: name, key ingredients, and estimated calories.")

    messages = [{"role": "user", "content": " ".join(prompt_parts)}]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature, max_tokens=4096)


def get_recipe_details(meal_name: str, diet: str, model: str = "gemma4", temperature: float = 0.7) -> str:
    """Get a detailed recipe for a specific meal."""
    messages = [
        {
            "role": "user",
            "content": (
                f"Give me a detailed recipe for: {meal_name}\n"
                f"Diet: {diet}\n"
                "Include: ingredients list, step-by-step instructions, prep time, "
                "cook time, servings, and nutritional info."
            ),
        }
    ]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature, max_tokens=2048)


def generate_shopping_list(meal_plan: str, model: str = "gemma4", temperature: float = 0.3) -> str:
    """Generate a consolidated shopping list from a meal plan."""
    from .utils import generate_shopping_list_prompt
    messages = [{"role": "user", "content": generate_shopping_list_prompt(meal_plan)}]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature, max_tokens=2048)
