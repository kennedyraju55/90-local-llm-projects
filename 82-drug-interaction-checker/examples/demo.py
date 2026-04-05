"""
Demo script for Drug Interaction Checker
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.drug_checker.core import load_config, parse_medications, check_interactions, get_food_interactions, get_dosage_notes, get_alternatives, classify_severity, display_results


def main():
    """Run a quick demo of Drug Interaction Checker."""
    print("=" * 60)
    print("🚀 Drug Interaction Checker - Demo")
    print("=" * 60)
    print()
    # Load configuration from config.yaml, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Parse a comma-separated medication string into a cleaned list.
    print("📝 Example: parse_medications()")
    result = parse_medications(
        medications_str=["aspirin", "ibuprofen"]
    )
    print(f"   Result: {result}")
    print()
    # Send medication list to the LLM for interaction analysis.
    print("📝 Example: check_interactions()")
    result = check_interactions(
        medications=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    # Look up known food interactions for a medication.
    print("📝 Example: get_food_interactions()")
    result = get_food_interactions(
        medication="ibuprofen"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
