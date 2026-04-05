"""
Demo script for Story Outline Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.story_gen.core import load_config, get_character_archetypes, get_plot_structures, get_worldbuilding_categories, build_prompt, generate_outline, generate_character_profile, visualize_plot_arc


def main():
    """Run a quick demo of Story Outline Generator."""
    print("=" * 60)
    print("🚀 Story Outline Generator - Demo")
    print("=" * 60)
    print()
    # Using load_config
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Using get_character_archetypes
    print("📝 Example: get_character_archetypes()")
    result = get_character_archetypes()
    print(f"   Result: {result}")
    print()
    # Using get_plot_structures
    print("📝 Example: get_plot_structures()")
    result = get_plot_structures()
    print(f"   Result: {result}")
    print()
    # Using get_worldbuilding_categories
    print("📝 Example: get_worldbuilding_categories()")
    result = get_worldbuilding_categories()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
