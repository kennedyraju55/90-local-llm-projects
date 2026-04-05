"""
Demo script for Meal Planner Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.meal_planner.core import generate_meal_plan, get_recipe_details, generate_shopping_list


def main():
    """Run a quick demo of Meal Planner Bot."""
    print("=" * 60)
    print("🚀 Meal Planner Bot - Demo")
    print("=" * 60)
    print()
    # Generate a meal plan based on preferences.
    print("📝 Example: generate_meal_plan()")
    result = generate_meal_plan(
        diet="balanced",
        days=5
    )
    print(f"   Result: {result}")
    print()
    # Get a detailed recipe for a specific meal.
    print("📝 Example: get_recipe_details()")
    result = get_recipe_details(
        meal_name="John Doe",
        diet="balanced"
    )
    print(f"   Result: {result}")
    print()
    # Generate a consolidated shopping list from a meal plan.
    print("📝 Example: generate_shopping_list()")
    result = generate_shopping_list(
        meal_plan="sample data"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
