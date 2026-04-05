"""
Demo script for Exercise Form Guide
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.exercise_guide.core import get_warmup_routine, get_cooldown_routine, get_exercise_variations, get_muscle_info, generate_guide, list_exercises, generate_routine


def main():
    """Run a quick demo of Exercise Form Guide."""
    print("=" * 60)
    print("🚀 Exercise Form Guide - Demo")
    print("=" * 60)
    print()
    # Return a list of warm-up exercises for the given muscle group.
    print("📝 Example: get_warmup_routine()")
    result = get_warmup_routine(
        muscle_group="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Return a list of cool-down stretches for the given muscle group.
    print("📝 Example: get_cooldown_routine()")
    result = get_cooldown_routine(
        muscle_group="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Return the progression path for a given exercise.
    print("📝 Example: get_exercise_variations()")
    result = get_exercise_variations(
        exercise="bench press"
    )
    print(f"   Result: {result}")
    print()
    # Return muscle group information from the database.
    print("📝 Example: get_muscle_info()")
    result = get_muscle_info(
        muscle_group="sample data"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
