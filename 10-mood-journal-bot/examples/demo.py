"""
Demo script for Mood Journal Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.mood_journal.core import load_entries, save_entries, add_entry, get_recent_entries, analyze_entries, generate_weekly_report, generate_monthly_report, get_gratitude_prompt, get_mood_stats, export_entries


def main():
    """Run a quick demo of Mood Journal Bot."""
    print("=" * 60)
    print("🚀 Mood Journal Bot - Demo")
    print("=" * 60)
    print()
    # Load journal entries from the JSON file.
    print("📝 Example: load_entries()")
    result = load_entries()
    print(f"   Result: {result}")
    print()
    # Save journal entries to the JSON file.
    print("📝 Example: save_entries()")
    result = save_entries(
        entries=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    # Create and save a new journal entry.
    print("📝 Example: add_entry()")
    result = add_entry(
        mood_key="feeling productive and optimistic today",
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Get entries from the last N days.
    print("📝 Example: get_recent_entries()")
    result = get_recent_entries()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
