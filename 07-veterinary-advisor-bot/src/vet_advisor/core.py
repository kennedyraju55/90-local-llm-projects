"""Core business logic for Veterinary Advisor Bot."""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
from datetime import datetime

from .config import load_config
from .utils import get_llm_client, load_json_file, save_json_file, get_data_path

logger = logging.getLogger(__name__)

chat, check_ollama_running = get_llm_client()

SYSTEM_PROMPT = """You are a knowledgeable veterinary advisor AI assistant. Your role is to:
1. Provide general pet health information and guidance
2. Help identify potential issues based on described symptoms
3. Suggest when veterinary care is urgently needed
4. Offer general care tips for different pet types and breeds
5. Discuss nutrition, exercise, and preventive care

CRITICAL GUIDELINES:
- ALWAYS include a disclaimer that you are an AI and not a licensed veterinarian
- ALWAYS recommend consulting a real veterinarian for serious concerns
- Flag emergency symptoms clearly (e.g., difficulty breathing, seizures, poisoning)
- Never prescribe specific medications or dosages
- Be empathetic and supportive to worried pet owners
- If symptoms sound urgent, strongly recommend immediate vet visit"""

MEDICAL_DISCLAIMER = (
    "⚕️ **Disclaimer:** This is AI-generated advice for informational purposes only. "
    "It is NOT a substitute for professional veterinary care. Always consult a licensed "
    "veterinarian for your pet's health concerns, especially in emergencies."
)

PET_TYPES = ["dog", "cat", "bird", "fish", "rabbit", "hamster", "reptile", "other"]


def format_pet_context(profile: dict) -> str:
    """Format pet profile into context string."""
    return (
        f"Pet: {profile['name']} ({profile['type'].capitalize()})\n"
        f"Breed: {profile['breed']}\n"
        f"Age: {profile['age']}\n"
        f"Weight: {profile['weight']}"
    )


def get_response(user_message: str, history: list[dict], pet_profile: dict) -> str:
    """Get a response from the vet advisor bot."""
    context = format_pet_context(pet_profile)
    full_message = f"Pet Profile:\n{context}\n\nQuestion: {user_message}"
    messages = history + [{"role": "user", "content": full_message}]
    return chat(messages, system_prompt=SYSTEM_PROMPT)


def check_symptoms(symptoms: str, pet_profile: dict) -> str:
    """Check symptoms and provide guidance."""
    context = format_pet_context(pet_profile)
    messages = [
        {
            "role": "user",
            "content": (
                f"Pet Profile:\n{context}\n\n"
                f"Symptoms: {symptoms}\n\n"
                "Please analyze these symptoms and provide:\n"
                "1. Possible causes (from most to least likely)\n"
                "2. Urgency level (Emergency/Urgent/Non-urgent)\n"
                "3. Recommended immediate actions\n"
                "4. When to see a vet\n"
                "Include the medical disclaimer."
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=2048)


def get_breed_advice(pet_type: str, breed: str) -> str:
    """Get breed-specific care advice."""
    messages = [
        {
            "role": "user",
            "content": (
                f"Provide comprehensive breed-specific care advice for a {breed} {pet_type}.\n"
                "Include:\n"
                "1. Common health issues for this breed\n"
                "2. Dietary recommendations\n"
                "3. Exercise needs\n"
                "4. Grooming requirements\n"
                "5. Temperament and behavioral traits\n"
                "6. Preventive care schedule\n"
                "7. Signs to watch for"
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=2048)


def get_nutrition_advice(pet_profile: dict) -> str:
    """Get nutrition advice for a specific pet."""
    context = format_pet_context(pet_profile)
    messages = [
        {
            "role": "user",
            "content": (
                f"Pet Profile:\n{context}\n\n"
                "Provide detailed nutrition advice including:\n"
                "1. Recommended diet type and feeding schedule\n"
                "2. Portion sizes based on age and weight\n"
                "3. Foods to avoid\n"
                "4. Supplements to consider\n"
                "5. Hydration needs"
            ),
        }
    ]
    return chat(messages, system_prompt=SYSTEM_PROMPT, max_tokens=2048)


# --- Pet Profile Storage ---

def load_pet_profiles() -> list[dict]:
    """Load saved pet profiles."""
    path = get_data_path("pet_profiles.json")
    data = load_json_file(path)
    return data if isinstance(data, list) else []


def save_pet_profiles(profiles: list[dict]) -> None:
    """Save pet profiles."""
    path = get_data_path("pet_profiles.json")
    save_json_file(path, profiles)


def add_pet_profile(name: str, pet_type: str, breed: str = "unknown",
                    age: str = "unknown", weight: str = "unknown") -> dict:
    """Add a new pet profile."""
    profiles = load_pet_profiles()
    profile = {
        "id": len(profiles) + 1,
        "name": name,
        "type": pet_type,
        "breed": breed,
        "age": age,
        "weight": weight,
        "created_date": datetime.now().isoformat(),
    }
    profiles.append(profile)
    save_pet_profiles(profiles)
    logger.info("Added pet profile: %s (%s)", name, pet_type)
    return profile


def get_pet_profile(name: str) -> dict | None:
    """Get a pet profile by name."""
    profiles = load_pet_profiles()
    for p in profiles:
        if p["name"].lower() == name.lower():
            return p
    return None


# --- Symptom History ---

def load_symptom_history() -> list[dict]:
    """Load symptom history."""
    path = get_data_path("symptom_history.json")
    data = load_json_file(path)
    return data if isinstance(data, list) else []


def save_symptom_history(history: list[dict]) -> None:
    """Save symptom history."""
    path = get_data_path("symptom_history.json")
    save_json_file(path, history)


def record_symptom(pet_name: str, symptoms: str, severity: str = "unknown",
                   notes: str = "") -> dict:
    """Record a symptom entry."""
    history = load_symptom_history()
    entry = {
        "id": len(history) + 1,
        "pet_name": pet_name,
        "symptoms": symptoms,
        "severity": severity,
        "notes": notes,
        "date": datetime.now().isoformat(),
    }
    history.append(entry)
    save_symptom_history(history)
    logger.info("Recorded symptom for %s: %s", pet_name, symptoms[:50])
    return entry


def get_symptom_history_for_pet(pet_name: str) -> list[dict]:
    """Get symptom history for a specific pet."""
    history = load_symptom_history()
    return [h for h in history if h["pet_name"].lower() == pet_name.lower()]
