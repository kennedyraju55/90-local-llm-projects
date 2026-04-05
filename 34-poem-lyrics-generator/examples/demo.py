"""
Demo script for Poem Lyrics Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.poem_gen.core import build_prompt, generate_poem, generate_with_rhyme_scheme, mix_styles, count_syllables, detect_rhyme_scheme, analyze_poem, format_poem, manage_collection, to_dict


def main():
    """Run a quick demo of Poem Lyrics Generator."""
    print("=" * 60)
    print("🚀 Poem Lyrics Generator - Demo")
    print("=" * 60)
    print()
    # Build the poem/lyrics generation prompt.
    print("📝 Example: build_prompt()")
    result = build_prompt(
        theme="innovation",
        style="professional",
        mood="feeling productive and optimistic today",
        title="Sample Project Title"
    )
    print(f"   Result: {result}")
    print()
    # Generate a poem or lyrics using the LLM.
    print("📝 Example: generate_poem()")
    result = generate_poem(
        theme="innovation",
        style="professional"
    )
    print(f"   Result: {result}")
    print()
    # Generate a poem following a specific rhyme scheme (e.g. 'ABAB').
    print("📝 Example: generate_with_rhyme_scheme()")
    result = generate_with_rhyme_scheme(
        theme="innovation",
        scheme="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Generate a poem that mixes two poetic styles.
    print("📝 Example: mix_styles()")
    result = mix_styles(
        theme="innovation",
        styles=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
