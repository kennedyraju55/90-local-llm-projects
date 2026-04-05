"""
Demo script for Family Story Creator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.family_story.core import load_config, load_stories, save_story, delete_story, create_character, create_story, create_chapter, create_book, continue_story, create_poem


def main():
    """Run a quick demo of Family Story Creator."""
    print("=" * 60)
    print("🚀 Family Story Creator - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load saved stories from JSON file.
    print("📝 Example: load_stories()")
    result = load_stories()
    print(f"   Result: {result}")
    print()
    # Save a new story and return it with generated id and timestamp.
    print("📝 Example: save_story()")
    result = save_story(
        story={}
    )
    print(f"   Result: {result}")
    print()
    # Delete a story by its id. Returns True if found and deleted.
    print("📝 Example: delete_story()")
    result = delete_story(
        story_id="Once upon a time in a digital world..."
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
