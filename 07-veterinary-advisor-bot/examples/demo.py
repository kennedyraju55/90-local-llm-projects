"""
Demo script for Veterinary Advisor Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.vet_advisor.core import format_pet_context, get_response, check_symptoms, get_breed_advice, get_nutrition_advice, load_pet_profiles, save_pet_profiles, add_pet_profile, get_pet_profile, load_symptom_history


def main():
    """Run a quick demo of Veterinary Advisor Bot."""
    print("=" * 60)
    print("🚀 Veterinary Advisor Bot - Demo")
    print("=" * 60)
    print()
    # Format pet profile into context string.
    print("📝 Example: format_pet_context()")
    result = format_pet_context(
        profile={}
    )
    print(f"   Result: {result}")
    print()
    # Get a response from the vet advisor bot.
    print("📝 Example: get_response()")
    result = get_response(
        user_message="Can you help me with this?",
        history=[{"key": "value"}],
        pet_profile={}
    )
    print(f"   Result: {result}")
    print()
    # Check symptoms and provide guidance.
    print("📝 Example: check_symptoms()")
    result = check_symptoms(
        symptoms=["headache", "fever", "fatigue"],
        pet_profile={}
    )
    print(f"   Result: {result}")
    print()
    # Get breed-specific care advice.
    print("📝 Example: get_breed_advice()")
    result = get_breed_advice(
        pet_type="sample data",
        breed="sample data"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
