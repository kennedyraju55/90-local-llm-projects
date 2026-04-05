"""
Demo script for Reading List Manager
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.reading_list.core import load_config, load_books, save_books, add_book, update_progress, rate_book, get_genre_stats, recommend_similar, calculate_reading_speed, set_reading_goal


def main():
    """Run a quick demo of Reading List Manager."""
    print("=" * 60)
    print("🚀 Reading List Manager - Demo")
    print("=" * 60)
    print()
    # Load application configuration from config.yaml.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load reading list from JSON file.
    print("📝 Example: load_books()")
    result = load_books()
    print(f"   Result: {result}")
    print()
    # Save reading list to JSON file.
    print("📝 Example: save_books()")
    result = save_books(
        data={}
    )
    print(f"   Result: {result}")
    print()
    # Add a book to the reading list.
    print("📝 Example: add_book()")
    result = add_book(
        title="Sample Project Title",
        author="sample data"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
