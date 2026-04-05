"""
Demo script for First Aid Guide Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.first_aid.core import show_disclaimer, get_severity_style, evaluate_emergency, get_supply_checklist, get_cpr_steps, add_contact, remove_contact, get_contacts, get_default, EmergencyContact


def main():
    """Run a quick demo of First Aid Guide Bot."""
    print("=" * 60)
    print("🚀 First Aid Guide Bot - Demo")
    print("=" * 60)
    print()
    # Display the emergency disclaimer prominently.
    print("📝 Example: show_disclaimer()")
    result = show_disclaimer()
    print(f"   Result: {result}")
    print()
    # Return a rich style string based on severity level.
    print("📝 Example: get_severity_style()")
    result = get_severity_style(
        severity="HIGH"
    )
    print(f"   Result: {result}")
    print()
    # Evaluate an emergency situation using the decision tree.
    print("📝 Example: evaluate_emergency()")
    result = evaluate_emergency(
        conscious=True,
        breathing=True
    )
    print(f"   Result: {result}")
    print()
    # Return the first aid supply checklist, optionally filtered by priority.
    print("📝 Example: get_supply_checklist()")
    result = get_supply_checklist()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
