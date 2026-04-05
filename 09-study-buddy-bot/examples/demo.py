"""
Demo script for Study Buddy Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.study_buddy.core import generate_quiz, explain_concept, create_study_plan, generate_flashcards, ask_question, load_saved_flashcards, save_flashcards_data, save_flashcard_set, get_flashcard_set, load_study_progress


def main():
    """Run a quick demo of Study Buddy Bot."""
    print("=" * 60)
    print("🚀 Study Buddy Bot - Demo")
    print("=" * 60)
    print()
    # Generate quiz questions on a topic.
    print("📝 Example: generate_quiz()")
    result = generate_quiz(
        subject="Introduction to Python Programming",
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    # Explain a concept in detail.
    print("📝 Example: explain_concept()")
    result = explain_concept(
        subject="Introduction to Python Programming",
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    # Create a study plan for exam preparation.
    print("📝 Example: create_study_plan()")
    result = create_study_plan(
        subject="Introduction to Python Programming",
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    # Generate flashcard-style Q&A pairs.
    print("📝 Example: generate_flashcards()")
    result = generate_flashcards(
        subject="Introduction to Python Programming",
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
