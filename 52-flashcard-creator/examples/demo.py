"""
Demo script for Flashcard Creator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.flashcard_creator.core import setup_logging, parse_response, create_flashcards, dict_to_flashcards, export_deck_json, import_deck_json, export_deck_csv, import_deck_csv, get, calculate_next_review


def main():
    """Run a quick demo of Flashcard Creator."""
    print("=" * 60)
    print("🚀 Flashcard Creator - Demo")
    print("=" * 60)
    print()
    # Configure module-level logging based on config.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Strip markdown fences and parse JSON from LLM output.
    print("📝 Example: parse_response()")
    result = parse_response(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Generate flashcards using the LLM.
    print("📝 Example: create_flashcards()")
    result = create_flashcards(
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    # Convert raw LLM JSON into a list of Flashcard dataclass instances.
    print("📝 Example: dict_to_flashcards()")
    result = dict_to_flashcards(
        data={}
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
