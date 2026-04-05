"""
Demo script for Time Management Coach
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.time_coach.core import load_config, load_timelog, save_time_entry, compute_time_breakdown, compute_daily_totals, compute_productivity_score, generate_time_blocks, analyze_time_usage, get_tips, generate_pomodoro_plan


def main():
    """Run a quick demo of Time Management Coach."""
    print("=" * 60)
    print("🚀 Time Management Coach - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load time log entries from a CSV file.
    print("📝 Example: load_timelog()")
    result = load_timelog(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Append a single time entry to the CSV log, creating the file if needed.
    print("📝 Example: save_time_entry()")
    result = save_time_entry(
        entry={},
        log_file="app.log"
    )
    print(f"   Result: {result}")
    print()
    # Compute total hours per category.
    print("📝 Example: compute_time_breakdown()")
    result = compute_time_breakdown(
        entries=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
