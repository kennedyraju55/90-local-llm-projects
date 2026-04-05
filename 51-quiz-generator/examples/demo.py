"""
Demo script for Quiz Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.quiz_gen.core import setup_logging, parse_response, validate_quiz_data, generate_quiz, score_quiz, export_quiz_json, export_quiz_pdf_ready, get, raw, to_dict


def main():
    """Run a quick demo of Quiz Generator."""
    print("=" * 60)
    print("🚀 Quiz Generator - Demo")
    print("=" * 60)
    print()
    # Configure the quiz_gen logger.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Parse LLM response text into a quiz dict, handling code fences.
    print("📝 Example: parse_response()")
    result = parse_response(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Return a list of validation errors (empty == valid).
    print("📝 Example: validate_quiz_data()")
    result = validate_quiz_data(
        quiz_data={}
    )
    print(f"   Result: {result}")
    print()
    # Generate a quiz using the LLM.
    print("📝 Example: generate_quiz()")
    result = generate_quiz(
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
