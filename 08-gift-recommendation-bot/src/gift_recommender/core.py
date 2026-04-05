"""Core business logic for Gift Recommendation Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
from datetime import datetime

from .config import load_config
from .utils import get_llm_client, load_json_file, save_json_file, get_data_path

logger = logging.getLogger(__name__)

chat, check_ollama_running = get_llm_client()

SYSTEM_PROMPT = """You are a creative gift recommendation expert. Your role is to:
1. Suggest thoughtful, personalized gift ideas based on the recipient's profile
2. Consider budget constraints and provide options at different price points
3. Include both physical and experience-based gift ideas
4. Explain WHY each gift would be meaningful for the recipient
5. Suggest where to purchase each gift
6. Include creative wrapping or presentation ideas

Format each recommendation with:
- Gift name and brief description
- Estimated price range
- Why it's a good fit
- Where to buy it"""

OCCASIONS = [
    "birthday", "christmas", "anniversary", "wedding", "graduation",
    "baby-shower", "housewarming", "valentines", "mothers-day",
    "fathers-day", "retirement", "thank-you", "get-well", "other",
]

RELATIONSHIPS = [
    "partner", "parent", "sibling", "friend", "colleague",
    "child", "grandparent", "teacher", "boss", "neighbor",
]


def generate_recommendations(
    occasion: str,
    relationship: str,
    budget: int,
    interests: str | None = None,
    age: str | None = None,
    gender: str | None = None,
) -> str:
    """Generate gift recommendations based on parameters."""
    prompt_parts = [
        f"Suggest 5-7 gift ideas for a {occasion} gift.",
        f"Recipient: {relationship}.",
        f"Budget: up to ${budget}.",
    ]
    if interests:
        prompt_parts.append(f"Recipient's interests: {interests}.")
    if age:
        prompt_parts.append(f"Recipient's age: {age}.")
    if gender:
        prompt_parts.append(f"Recipient's gender: {gender}.")
    prompt_parts.append(
        "Include a mix of practical, fun, and sentimental options. "
        "For each gift, provide: name, price range, why it's great, and where to buy."
    )

    messages = [{"role": "user", "content": " ".join(prompt_parts)}]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=3072)


def get_gift_details(gift_name: str, budget: int) -> str:
    """Get detailed information about a specific gift idea."""
    messages = [
        {
            "role": "user",
            "content": (
                f"Give me more details about this gift idea: {gift_name}\n"
                f"Budget: up to ${budget}\n"
                "Include: specific product recommendations, where to buy, "
                "creative presentation ideas, and any DIY alternatives."
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=1024)


def compare_prices(gift_name: str) -> str:
    """Get price comparison information for a gift."""
    messages = [
        {
            "role": "user",
            "content": (
                f"Provide a price comparison for: {gift_name}\n"
                "List different retailers/options with estimated prices, "
                "pros and cons of each option, and any current deal tips."
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=1024)


# --- Wishlist Management ---

def load_wishlists() -> dict:
    """Load all wishlists."""
    path = get_data_path("wishlists.json")
    data = load_json_file(path)
    return data if isinstance(data, dict) else {}


def save_wishlists(wishlists: dict) -> None:
    """Save wishlists."""
    path = get_data_path("wishlists.json")
    save_json_file(path, wishlists)


def add_to_wishlist(person: str, gift: str, price: str = "",
                    occasion: str = "", notes: str = "") -> dict:
    """Add an item to someone's wishlist."""
    wishlists = load_wishlists()
    person_key = person.lower().strip()
    if person_key not in wishlists:
        wishlists[person_key] = {"name": person, "items": []}
    item = {
        "id": len(wishlists[person_key]["items"]) + 1,
        "gift": gift,
        "price": price,
        "occasion": occasion,
        "notes": notes,
        "added_date": datetime.now().isoformat(),
        "purchased": False,
    }
    wishlists[person_key]["items"].append(item)
    save_wishlists(wishlists)
    logger.info("Added to %s's wishlist: %s", person, gift)
    return item


def get_wishlist(person: str) -> list[dict]:
    """Get wishlist items for a person."""
    wishlists = load_wishlists()
    person_key = person.lower().strip()
    return wishlists.get(person_key, {}).get("items", [])


def mark_purchased(person: str, item_id: int) -> bool:
    """Mark a wishlist item as purchased."""
    wishlists = load_wishlists()
    person_key = person.lower().strip()
    if person_key in wishlists:
        for item in wishlists[person_key]["items"]:
            if item["id"] == item_id:
                item["purchased"] = True
                save_wishlists(wishlists)
                return True
    return False


# --- Occasion Calendar ---

def load_calendar() -> list[dict]:
    """Load occasion calendar."""
    path = get_data_path("occasion_calendar.json")
    data = load_json_file(path)
    return data if isinstance(data, list) else []


def save_calendar(calendar: list[dict]) -> None:
    """Save occasion calendar."""
    path = get_data_path("occasion_calendar.json")
    save_json_file(path, calendar)


def add_occasion(person: str, occasion: str, date: str,
                 notes: str = "") -> dict:
    """Add an occasion to the calendar."""
    calendar = load_calendar()
    entry = {
        "id": len(calendar) + 1,
        "person": person,
        "occasion": occasion,
        "date": date,
        "notes": notes,
        "reminder_sent": False,
    }
    calendar.append(entry)
    save_calendar(calendar)
    logger.info("Added occasion: %s - %s on %s", person, occasion, date)
    return entry


def get_upcoming_occasions(days: int = 30) -> list[dict]:
    """Get occasions in the next N days."""
    calendar = load_calendar()
    now = datetime.now()
    upcoming = []
    for entry in calendar:
        try:
            occ_date = datetime.strptime(entry["date"], "%Y-%m-%d")
            # Check same month-day in current year
            this_year = occ_date.replace(year=now.year)
            delta = (this_year - now).days
            if 0 <= delta <= days:
                entry["days_until"] = delta
                upcoming.append(entry)
        except (ValueError, KeyError):
            continue
    return sorted(upcoming, key=lambda x: x.get("days_until", 999))
