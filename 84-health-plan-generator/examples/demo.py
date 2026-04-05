"""
Demo script for Health Plan Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.health_planner.core import load_config, get_milestones_for_goal, generate_adaptive_recommendation, generate_plan, start_plan, add_checkin, get_progress_summary, get_current_milestone, to_dict, from_dict


def main():
    """Run a quick demo of Health Plan Generator."""
    print("=" * 60)
    print("🚀 Health Plan Generator - Demo")
    print("=" * 60)
    print()
    # Load configuration from config.yaml, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Get milestones for a given goal.
    print("📝 Example: get_milestones_for_goal()")
    result = get_milestones_for_goal(
        goal="improve overall fitness"
    )
    print(f"   Result: {result}")
    print()
    # Generate adaptive recommendations based on progress.
    print("📝 Example: generate_adaptive_recommendation()")
    result = generate_adaptive_recommendation(
        tracker="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Generate a wellness plan using the LLM.
    print("📝 Example: generate_plan()")
    result = generate_plan(
        goal="improve overall fitness"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
