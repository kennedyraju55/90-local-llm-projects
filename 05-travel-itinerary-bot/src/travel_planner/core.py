"""Core business logic for Travel Itinerary Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))
from common.llm_client import chat, check_ollama_running  # noqa: E402

SYSTEM_PROMPT = """You are an expert travel planner with extensive knowledge of destinations worldwide. Your role is to:
1. Create detailed, day-by-day travel itineraries
2. Recommend attractions, restaurants, and activities
3. Consider budget constraints and suggest cost-saving tips
4. Include practical travel tips (transportation, timing, local customs)
5. Suggest alternative plans for bad weather

For each day include:
- Morning, afternoon, and evening activities
- Restaurant/food recommendations
- Estimated costs
- Travel tips and logistics
- Time estimates for each activity"""

BUDGETS = ["budget", "moderate", "luxury"]
INTERESTS_EXAMPLES = "culture, food, nature, adventure, shopping, history, nightlife, relaxation"


def generate_itinerary(
    destination: str,
    days: int,
    budget: str,
    interests: str | None = None,
    travelers: int = 1,
    model: str = "gemma4",
    temperature: float = 0.7,
) -> str:
    """Generate a travel itinerary."""
    logger.info("Generating %d-day itinerary for %s", days, destination)
    prompt_parts = [
        f"Create a detailed {days}-day travel itinerary for {destination}.",
        f"Budget level: {budget}.",
        f"Number of travelers: {travelers}.",
    ]
    if interests:
        prompt_parts.append(f"Interests and preferences: {interests}.")
    prompt_parts.append(
        "For each day, provide a complete schedule with morning, afternoon, "
        "and evening activities, food recommendations, and estimated costs."
    )
    messages = [{"role": "user", "content": " ".join(prompt_parts)}]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature, max_tokens=4096)


def generate_multi_destination_itinerary(
    destinations: list[str],
    days_per_dest: int,
    budget: str,
    interests: str | None = None,
    travelers: int = 1,
    model: str = "gemma4",
    temperature: float = 0.7,
) -> str:
    """Generate a multi-destination itinerary."""
    logger.info("Generating multi-dest itinerary for %d destinations", len(destinations))
    dest_str = " → ".join(destinations)
    total_days = days_per_dest * len(destinations)
    prompt = (
        f"Create a detailed {total_days}-day multi-destination travel itinerary: {dest_str}.\n"
        f"Spend approximately {days_per_dest} days at each destination.\n"
        f"Budget level: {budget}. Travelers: {travelers}.\n"
    )
    if interests:
        prompt += f"Interests: {interests}.\n"
    prompt += (
        "Include travel/transit between destinations. For each day, provide morning, "
        "afternoon, and evening activities with estimated costs."
    )
    messages = [{"role": "user", "content": prompt}]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature, max_tokens=4096)


def get_place_details(place: str, destination: str, model: str = "gemma4", temperature: float = 0.7) -> str:
    """Get detailed information about a specific place or attraction."""
    logger.info("Fetching details for %s in %s", place, destination)
    messages = [
        {
            "role": "user",
            "content": (
                f"Tell me more about: {place} in {destination}\n"
                "Include: description, best time to visit, entry fees, "
                "how to get there, tips, and nearby attractions."
            ),
        }
    ]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=temperature, max_tokens=1024)


def generate_budget_breakdown(itinerary: str, budget: str, travelers: int, model: str = "gemma4") -> str:
    """Generate a budget breakdown for the itinerary."""
    logger.info("Generating budget breakdown for %d travelers", travelers)
    from .utils import generate_budget_prompt
    messages = [{"role": "user", "content": generate_budget_prompt(itinerary, budget, travelers)}]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=0.3, max_tokens=2048)


def generate_packing_list(destination: str, days: int, interests: str | None, model: str = "gemma4") -> str:
    """Generate a packing list for the trip."""
    logger.info("Generating packing list for %s (%d days)", destination, days)
    from .utils import generate_packing_list_prompt
    messages = [{"role": "user", "content": generate_packing_list_prompt(destination, days, interests)}]
    return chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=0.3, max_tokens=2048)
