"""
Demo script for Vocabulary Builder
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.vocab_builder.core import load_config, generate_vocabulary, load_vocab_file, run_quiz, score_quiz, create_spaced_repetition_deck, get_due_cards, check_service, to_dict, update


def main():
    """Run a quick demo of Vocabulary Builder."""
    print("=" * 60)
    print("🚀 Vocabulary Builder - Demo")
    print("=" * 60)
    print()
    # Using load_config
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Generate a vocabulary set using the LLM.
    print("📝 Example: generate_vocabulary()")
    result = generate_vocabulary(
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    # Load vocabulary from a JSON file.
    print("📝 Example: load_vocab_file()")
    result = load_vocab_file(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Run a vocabulary quiz (non-interactive, returns structure for UI to handle).
    print("📝 Example: run_quiz()")
    result = run_quiz(
        words=[]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
