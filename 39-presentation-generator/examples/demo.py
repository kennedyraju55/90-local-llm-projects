"""
Demo script for Presentation Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.presentation_gen.core import load_config, get_formats, get_slide_templates, get_visual_suggestions, estimate_timing, build_prompt, generate_presentation, export_to_markdown, generate_speaker_notes_only


def main():
    """Run a quick demo of Presentation Generator."""
    print("=" * 60)
    print("🚀 Presentation Generator - Demo")
    print("=" * 60)
    print()
    # Using load_config
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Using get_formats
    print("📝 Example: get_formats()")
    result = get_formats()
    print(f"   Result: {result}")
    print()
    # Using get_slide_templates
    print("📝 Example: get_slide_templates()")
    result = get_slide_templates()
    print(f"   Result: {result}")
    print()
    # Using get_visual_suggestions
    print("📝 Example: get_visual_suggestions()")
    result = get_visual_suggestions()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
