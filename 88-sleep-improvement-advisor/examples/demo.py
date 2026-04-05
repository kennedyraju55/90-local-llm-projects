"""
Demo script for Sleep Improvement Advisor
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.sleep_advisor.core import parse_sleep_log, compute_sleep_stats, calculate_sleep_score, get_environment_checklist, build_bedtime_routine, analyze_weekly_patterns


def main():
    """Run a quick demo of Sleep Improvement Advisor."""
    print("=" * 60)
    print("🚀 Sleep Improvement Advisor - Demo")
    print("=" * 60)
    print()
    # Parse a sleep log CSV file.
    print("📝 Example: parse_sleep_log()")
    result = parse_sleep_log(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Compute summary statistics from sleep log entries.
    print("📝 Example: compute_sleep_stats()")
    result = compute_sleep_stats(
        entries=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    # Calculate a sleep score from 0-100 based on sleep statistics.
    print("📝 Example: calculate_sleep_score()")
    result = calculate_sleep_score(
        stats={}
    )
    print(f"   Result: {result}")
    print()
    # Return the sleep environment optimization checklist.
    print("📝 Example: get_environment_checklist()")
    result = get_environment_checklist()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
