"""
Demo script for Regex Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.regex_gen.core import generate_regex, explain_regex, get_pattern_from_library, list_library_patterns


def main():
    """Run a quick demo of Regex Generator."""
    print("=" * 60)
    print("🚀 Regex Generator - Demo")
    print("=" * 60)
    print()
    # Generate a regex pattern from natural language description.
    print("📝 Example: generate_regex()")
    result = generate_regex(
        description="A comprehensive guide to building modern applications."
    )
    print(f"   Result: {result}")
    print()
    # Explain an existing regex pattern in plain English.
    print("📝 Example: explain_regex()")
    result = explain_regex(
        pattern="email addresses"
    )
    print(f"   Result: {result}")
    print()
    # Look up a pattern from the built-in pattern library.
    print("📝 Example: get_pattern_from_library()")
    result = get_pattern_from_library(
        name="John Doe"
    )
    print(f"   Result: {result}")
    print()
    # Return the full pattern library.
    print("📝 Example: list_library_patterns()")
    result = list_library_patterns()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
