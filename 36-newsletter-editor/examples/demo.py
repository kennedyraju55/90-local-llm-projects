"""
Demo script for Newsletter Editor
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.newsletter_editor.core import load_config, read_input_file, get_section_templates, get_subscriber_segments, build_prompt, generate_newsletter, export_to_html, archive_newsletter, list_archive


def main():
    """Run a quick demo of Newsletter Editor."""
    print("=" * 60)
    print("🚀 Newsletter Editor - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML file with defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Read raw notes/content from a file.
    print("📝 Example: read_input_file()")
    result = read_input_file(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Return available section templates.
    print("📝 Example: get_section_templates()")
    result = get_section_templates()
    print(f"   Result: {result}")
    print()
    # Return available subscriber segments.
    print("📝 Example: get_subscriber_segments()")
    result = get_subscriber_segments()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
