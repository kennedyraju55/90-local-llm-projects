"""
Demo script for Language Learning Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.language_learner.core import get_system_prompt, get_response, get_lesson, get_pronunciation_tips, generate_lesson_plan, load_vocabulary, save_vocabulary, add_vocabulary_word, get_vocabulary_quiz, load_progress


def main():
    """Run a quick demo of Language Learning Bot."""
    print("=" * 60)
    print("🚀 Language Learning Bot - Demo")
    print("=" * 60)
    print()
    # Build the system prompt for the specified language and level.
    print("📝 Example: get_system_prompt()")
    result = get_system_prompt(
        language="python",
        level="intermediate"
    )
    print(f"   Result: {result}")
    print()
    # Get a response from the language tutor.
    print("📝 Example: get_response()")
    result = get_response(
        user_message="Can you help me with this?",
        history=[{"key": "value"}],
        language="python",
        level="intermediate"
    )
    print(f"   Result: {result}")
    print()
    # Get a mini lesson on a specific topic.
    print("📝 Example: get_lesson()")
    result = get_lesson(
        topic="artificial intelligence and machine learning",
        language="python",
        level="intermediate"
    )
    print(f"   Result: {result}")
    print()
    # Get pronunciation tips for a word in the target language.
    print("📝 Example: get_pronunciation_tips()")
    result = get_pronunciation_tips(
        word="serendipity",
        language="python"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
