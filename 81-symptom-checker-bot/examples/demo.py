"""
Demo script for Symptom Checker Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.symptom_checker.core import load_config, assess_urgency, get_body_regions, display_disclaimer, check_symptoms, add_entry, get_history, get_summary, MedicalHistoryTracker


def main():
    """Run a quick demo of Symptom Checker Bot."""
    print("=" * 60)
    print("🚀 Symptom Checker Bot - Demo")
    print("=" * 60)
    print()
    # Load configuration from config.yaml or use defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Assess urgency level based on symptom keywords.
    print("📝 Example: assess_urgency()")
    result = assess_urgency(
        symptoms_text=["headache", "fever", "fatigue"]
    )
    print(f"   Result: {result}")
    print()
    # Identify which body regions are affected by the described symptoms.
    print("📝 Example: get_body_regions()")
    result = get_body_regions(
        symptoms_text=["headache", "fever", "fatigue"]
    )
    print(f"   Result: {result}")
    print()
    # Display the medical disclaimer using rich formatting.
    print("📝 Example: display_disclaimer()")
    result = display_disclaimer()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
