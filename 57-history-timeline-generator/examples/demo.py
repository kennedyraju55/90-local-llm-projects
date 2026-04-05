"""
Demo script for History Timeline Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.history_timeline.core import load_config, generate_timeline, get_figure_profiles, get_cause_effect_chains, check_service, to_dict, HistoricalEvent, KeyFigureProfile, CauseEffectChain, Timeline


def main():
    """Run a quick demo of History Timeline Generator."""
    print("=" * 60)
    print("🚀 History Timeline Generator - Demo")
    print("=" * 60)
    print()
    # Using load_config
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Generate a historical timeline using the LLM.
    print("📝 Example: generate_timeline()")
    result = generate_timeline(
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    # Get detailed profiles of key historical figures.
    print("📝 Example: get_figure_profiles()")
    result = get_figure_profiles(
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    # Analyze cause-and-effect chains for a historical topic.
    print("📝 Example: get_cause_effect_chains()")
    result = get_cause_effect_chains(
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
