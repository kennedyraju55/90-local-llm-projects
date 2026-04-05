"""
Demo script for Fitness Coach Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.fitness_coach.core import generate_workout_plan, get_exercise_details


def main():
    """Run a quick demo of Fitness Coach Bot."""
    print("=" * 60)
    print("🚀 Fitness Coach Bot - Demo")
    print("=" * 60)
    print()
    # Generate a personalized workout plan.
    print("📝 Example: generate_workout_plan()")
    result = generate_workout_plan(
        level="intermediate",
        goal="improve overall fitness",
        equipment="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Get detailed instructions for a specific exercise.
    print("📝 Example: get_exercise_details()")
    result = get_exercise_details(
        exercise_name="bench press",
        level="intermediate"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
