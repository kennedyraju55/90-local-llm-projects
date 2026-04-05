"""
Demo script for Nutrition Label Analyzer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.nutrition_analyzer.core import analyze_food, analyze_label, compare_foods, read_file, calculate_daily_values, check_allergens, add_meal, get_daily_totals, get_remaining_budget, reset


def main():
    """Run a quick demo of Nutrition Label Analyzer."""
    print("=" * 60)
    print("🚀 Nutrition Label Analyzer - Demo")
    print("=" * 60)
    print()
    # Analyze nutrition for a single food item.
    print("📝 Example: analyze_food()")
    result = analyze_food(
        food="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Analyze nutrition label data from text.
    print("📝 Example: analyze_label()")
    result = analyze_label(
        label_text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Compare nutrition across multiple food items.
    print("📝 Example: compare_foods()")
    result = compare_foods(
        foods=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    # Read text content from a file.
    print("📝 Example: read_file()")
    result = read_file(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
