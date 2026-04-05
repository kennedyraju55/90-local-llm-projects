"""
Demo script for Reading Comprehension Builder
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.reading_comp.core import load_config, generate_comprehension, score_exercise, get_answer_key, check_service, to_dict, VocabularyWord, Question, ScoringRubric, ReadingExercise


def main():
    """Run a quick demo of Reading Comprehension Builder."""
    print("=" * 60)
    print("🚀 Reading Comprehension Builder - Demo")
    print("=" * 60)
    print()
    # Using load_config
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Generate a reading comprehension exercise using the LLM.
    print("📝 Example: generate_comprehension()")
    result = generate_comprehension(
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    # Score a completed exercise and return detailed results.
    print("📝 Example: score_exercise()")
    result = score_exercise(
        exercise="bench press",
        user_answers={}
    )
    print(f"   Result: {result}")
    print()
    # Get the answer key with explanations.
    print("📝 Example: get_answer_key()")
    result = get_answer_key(
        exercise="bench press"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
