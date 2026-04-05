"""
Demo script for Travel Itinerary Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.travel_planner.core import generate_itinerary, generate_multi_destination_itinerary, get_place_details, generate_budget_breakdown, generate_packing_list


def main():
    """Run a quick demo of Travel Itinerary Bot."""
    print("=" * 60)
    print("🚀 Travel Itinerary Bot - Demo")
    print("=" * 60)
    print()
    # Generate a travel itinerary.
    print("📝 Example: generate_itinerary()")
    result = generate_itinerary(
        destination="Tokyo, Japan",
        days=5,
        budget=50
    )
    print(f"   Result: {result}")
    print()
    # Generate a multi-destination itinerary.
    print("📝 Example: generate_multi_destination_itinerary()")
    result = generate_multi_destination_itinerary(
        destinations=["item1", "item2", "item3"],
        days_per_dest=5,
        budget=50
    )
    print(f"   Result: {result}")
    print()
    # Get detailed information about a specific place or attraction.
    print("📝 Example: get_place_details()")
    result = get_place_details(
        place="sample data",
        destination="Tokyo, Japan"
    )
    print(f"   Result: {result}")
    print()
    # Generate a budget breakdown for the itinerary.
    print("📝 Example: generate_budget_breakdown()")
    result = generate_budget_breakdown(
        itinerary="sample data",
        budget=50,
        travelers=5
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
