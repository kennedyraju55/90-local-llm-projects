"""
Demo script for Textbook Summarizer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.textbook_summarizer.core import read_chapter_file, detect_chapter_info, summarize_chapter, summarize_multi_chapter, generate_glossary, generate_concept_map, generate_study_questions


def main():
    """Run a quick demo of Textbook Summarizer."""
    print("=" * 60)
    print("🚀 Textbook Summarizer - Demo")
    print("=" * 60)
    print()
    # Read and return the contents of a textbook chapter file.
    print("📝 Example: read_chapter_file()")
    result = read_chapter_file(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Attempt to detect chapter number and title from the text.
    print("📝 Example: detect_chapter_info()")
    result = detect_chapter_info(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Generate a structured summary of a textbook chapter using the LLM.
    print("📝 Example: summarize_chapter()")
    result = summarize_chapter(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Summarize all chapters found in a multi-chapter textbook file.
    print("📝 Example: summarize_multi_chapter()")
    result = summarize_multi_chapter(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
