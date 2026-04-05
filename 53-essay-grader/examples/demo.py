"""
Demo script for Essay Grader
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.essay_grader.core import setup_logging, calculate_grade_letter, parse_response, validate_grade_data, read_essay, grade_essay, generate_annotations, check_plagiarism_indicators, export_grade_report, get_instance


def main():
    """Run a quick demo of Essay Grader."""
    print("=" * 60)
    print("🚀 Essay Grader - Demo")
    print("=" * 60)
    print()
    # Configure logging for the application.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Convert a numeric score to a letter grade.
    print("📝 Example: calculate_grade_letter()")
    result = calculate_grade_letter(
        score=0.7
    )
    print(f"   Result: {result}")
    print()
    # Parse an LLM JSON response, stripping markdown fences if present.
    print("📝 Example: parse_response()")
    result = parse_response(
        response=["Great product!", "Needs improvement in shipping", "Love the customer service"]
    )
    print(f"   Result: {result}")
    print()
    # Validate grade data structure. Returns a list of error messages (empty if valid).
    print("📝 Example: validate_grade_data()")
    result = validate_grade_data(
        data={}
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
