"""
Demo script for Blog Post Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.blog_gen.core import load_config, setup_logging, build_prompt, generate_blog_post, generate_outline, generate_multiple_drafts, score_seo, analyze_tone, export_markdown, parse_blog_post


def main():
    """Run a quick demo of Blog Post Generator."""
    print("=" * 60)
    print("🚀 Blog Post Generator - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Configure the root logger based on *config*.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Build the blog post generation prompt.
    print("📝 Example: build_prompt()")
    result = build_prompt(
        topic="artificial intelligence and machine learning",
        keywords=["item1", "item2", "item3"],
        tone="friendly and professional",
        length=5
    )
    print(f"   Result: {result}")
    print()
    # Generate a blog post using the LLM.
    print("📝 Example: generate_blog_post()")
    result = generate_blog_post(
        topic="artificial intelligence and machine learning",
        keywords=["item1", "item2", "item3"],
        tone="friendly and professional",
        length=5
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
