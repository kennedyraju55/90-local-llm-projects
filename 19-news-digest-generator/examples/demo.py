"""
Demo script for News Digest Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.news_digest.core import read_news_files, categorize_articles, generate_digest, analyze_sentiment, save_output


def main():
    """Run a quick demo of News Digest Generator."""
    print("=" * 60)
    print("🚀 News Digest Generator - Demo")
    print("=" * 60)
    print()
    # Read all .txt files from the sources directory.
    print("📝 Example: read_news_files()")
    result = read_news_files(
        sources_dir="def process(data):\n    return [x * 2 for x in data]"
    )
    print(f"   Result: {result}")
    print()
    # Send articles to the LLM for topic categorization.
    print("📝 Example: categorize_articles()")
    result = categorize_articles(
        articles=[{"key": "value"}],
        num_topics=5
    )
    print(f"   Result: {result}")
    print()
    # Generate an overall news digest from the categorized articles.
    print("📝 Example: generate_digest()")
    result = generate_digest(
        articles=[{"key": "value"}],
        categorization={"type": "bug", "priority": "high"}
    )
    print(f"   Result: {result}")
    print()
    # Analyze sentiment across articles.
    print("📝 Example: analyze_sentiment()")
    result = analyze_sentiment(
        articles=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
