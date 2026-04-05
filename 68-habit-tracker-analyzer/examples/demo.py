"""
Demo script for Habit Tracker Analyzer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.habit_tracker.core import load_config, load_habits, save_habits, log_habit, add_habit, delete_habit, compute_streaks, get_completion_rate, compute_correlations, check_achievements


def main():
    """Run a quick demo of Habit Tracker Analyzer."""
    print("=" * 60)
    print("🚀 Habit Tracker Analyzer - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load habits data from JSON file.
    print("📝 Example: load_habits()")
    result = load_habits()
    print(f"   Result: {result}")
    print()
    # Save habits data to JSON file.
    print("📝 Example: save_habits()")
    result = save_habits(
        data={}
    )
    print(f"   Result: {result}")
    print()
    # Log a habit completion for today.
    print("📝 Example: log_habit()")
    result = log_habit(
        habit_name="exercise"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
