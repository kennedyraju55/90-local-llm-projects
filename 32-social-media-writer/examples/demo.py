"""
Demo script for Social Media Writer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.social_writer.core import load_config, setup_logging, build_prompt, generate_posts, validate_char_count, generate_hashtags, suggest_schedule, generate_ab_variants, format_for_platform, preview_post


def main():
    """Run a quick demo of Social Media Writer."""
    print("=" * 60)
    print("🚀 Social Media Writer - Demo")
    print("=" * 60)
    print()
    # Load configuration from config.yaml, with caching.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Configure logging from the loaded config.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Build the social media post generation prompt.
    print("📝 Example: build_prompt()")
    result = build_prompt(
        platform="twitter",
        topic="artificial intelligence and machine learning",
        tone="friendly and professional",
        variants=5
    )
    print(f"   Result: {result}")
    print()
    # Generate social media posts using the LLM.
    print("📝 Example: generate_posts()")
    result = generate_posts(
        platform="twitter",
        topic="artificial intelligence and machine learning",
        tone="friendly and professional",
        variants=5
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
