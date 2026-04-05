"""
Demo script for Support Ticket Classifier
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.ticket_classifier.core import load_config, load_tickets, find_text_column, classify_ticket, classify_tickets_batch, build_priority_queue, compute_sla_deadlines, route_to_team, generate_auto_response, compute_analytics


def main():
    """Run a quick demo of Support Ticket Classifier."""
    print("=" * 60)
    print("🚀 Support Ticket Classifier - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load support tickets from a CSV file.
    print("📝 Example: load_tickets()")
    result = load_tickets(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Identify the column most likely containing ticket descriptions.
    print("📝 Example: find_text_column()")
    result = find_text_column(
        data=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    # Classify a single support ticket via the LLM.
    print("📝 Example: classify_ticket()")
    result = classify_ticket(
        ticket_text="My login is not working. I get an error when trying to reset my password.",
        categories=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
