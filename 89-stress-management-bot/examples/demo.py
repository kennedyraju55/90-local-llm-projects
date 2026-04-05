"""
Demo script for Stress Management Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.stress_manager.core import show_disclaimer, run_breathing_exercise, calculate_stress_score, get_cbt_worksheet, get_coping_suggestions


def main():
    """Run a quick demo of Stress Management Bot."""
    print("=" * 60)
    print("🚀 Stress Management Bot - Demo")
    print("=" * 60)
    print()
    # Display the mental health disclaimer.
    print("📝 Example: show_disclaimer()")
    result = show_disclaimer()
    print(f"   Result: {result}")
    print()
    # Run a guided breathing exercise with timed progress bars.
    print("📝 Example: run_breathing_exercise()")
    result = run_breathing_exercise(
        exercise_key="bench press"
    )
    print(f"   Result: {result}")
    print()
    # Calculate a detailed stress score from assessment answers.
    print("📝 Example: calculate_stress_score()")
    result = calculate_stress_score(
        answers={}
    )
    print(f"   Result: {result}")
    print()
    # Return a CBT worksheet template by type.
    print("📝 Example: get_cbt_worksheet()")
    result = get_cbt_worksheet(
        worksheet_type="sample data"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
