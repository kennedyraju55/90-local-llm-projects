"""
Demo script for Smart Calendar Assistant
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.calendar_assistant.core import load_config, get_config, load_schedule, display_schedule, optimize_schedule, suggest_meeting_time, analyze_workload, detect_conflicts, score_priority, generate_daily_agenda


def main():
    """Run a quick demo of Smart Calendar Assistant."""
    print("=" * 60)
    print("🚀 Smart Calendar Assistant - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Return the cached application config, loading it on first access.
    print("📝 Example: get_config()")
    result = get_config()
    print(f"   Result: {result}")
    print()
    # Load schedule events from a JSON file.
    print("📝 Example: load_schedule()")
    result = load_schedule(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Return a human-readable text representation of the schedule.
    print("📝 Example: display_schedule()")
    result = display_schedule(
        events=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
