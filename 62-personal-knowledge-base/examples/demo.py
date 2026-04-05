"""
Demo script for Personal Knowledge Base
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.knowledge_base.core import load_config, load_kb, save_kb, add_note, delete_note, get_note, display_notes, search_notes, summarize_kb, get_all_tags


def main():
    """Run a quick demo of Personal Knowledge Base."""
    print("=" * 60)
    print("🚀 Personal Knowledge Base - Demo")
    print("=" * 60)
    print()
    # Load configuration from config.yaml, falling back to sensible defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load the knowledge base from JSON file.
    print("📝 Example: load_kb()")
    result = load_kb()
    print(f"   Result: {result}")
    print()
    # Save the knowledge base to JSON file.
    print("📝 Example: save_kb()")
    result = save_kb(
        kb={}
    )
    print(f"   Result: {result}")
    print()
    # Add a note to the knowledge base.
    print("📝 Example: add_note()")
    result = add_note(
        title="Sample Project Title",
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration."
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
