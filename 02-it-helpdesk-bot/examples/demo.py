"""
Demo script for It Helpdesk Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.helpdesk_bot.core import get_response


def main():
    """Run a quick demo of It Helpdesk Bot."""
    print("=" * 60)
    print("🚀 It Helpdesk Bot - Demo")
    print("=" * 60)
    print()
    # Get a response from the IT helpdesk bot.
    print("📝 Example: get_response()")
    result = get_response(
        user_message="Can you help me with this?",
        history=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
