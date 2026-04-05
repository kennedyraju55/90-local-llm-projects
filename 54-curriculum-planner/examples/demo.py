"""
Demo script for Curriculum Planner
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.curriculum_planner.core import setup_logging, parse_response, generate_curriculum, validate_curriculum_data, build_course_design, export_curriculum, load, get, data, map_outcomes_to_weeks


def main():
    """Run a quick demo of Curriculum Planner."""
    print("=" * 60)
    print("🚀 Curriculum Planner - Demo")
    print("=" * 60)
    print()
    # Configure the root logger from config.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Parse a JSON response from the LLM, stripping markdown fences.
    print("📝 Example: parse_response()")
    result = parse_response(
        response=["Great product!", "Needs improvement in shipping", "Love the customer service"]
    )
    print(f"   Result: {result}")
    print()
    # Generate a curriculum using the LLM (enhanced from app.py).
    print("📝 Example: generate_curriculum()")
    result = generate_curriculum(
        course="sample data",
        weeks=5,
        level="intermediate"
    )
    print(f"   Result: {result}")
    print()
    # Validate curriculum data and return a list of issues (empty = valid).
    print("📝 Example: validate_curriculum_data()")
    result = validate_curriculum_data(
        data={}
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
