"""
Demo script for Gift Recommendation Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.gift_recommender.core import generate_recommendations, get_gift_details, compare_prices, load_wishlists, save_wishlists, add_to_wishlist, get_wishlist, mark_purchased, load_calendar, save_calendar


def main():
    """Run a quick demo of Gift Recommendation Bot."""
    print("=" * 60)
    print("🚀 Gift Recommendation Bot - Demo")
    print("=" * 60)
    print()
    # Generate gift recommendations based on parameters.
    print("📝 Example: generate_recommendations()")
    result = generate_recommendations(
        occasion="birthday",
        relationship="friend",
        budget=5
    )
    print(f"   Result: {result}")
    print()
    # Get detailed information about a specific gift idea.
    print("📝 Example: get_gift_details()")
    result = get_gift_details(
        gift_name="Smart Watch",
        budget=5
    )
    print(f"   Result: {result}")
    print()
    # Get price comparison information for a gift.
    print("📝 Example: compare_prices()")
    result = compare_prices(
        gift_name="Smart Watch"
    )
    print(f"   Result: {result}")
    print()
    # Load all wishlists.
    print("📝 Example: load_wishlists()")
    result = load_wishlists()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
