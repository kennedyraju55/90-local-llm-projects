"""
Demo script for Trend Analysis Tool
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.trend_analyzer.core import load_config, setup_logging, load_text_files, extract_topics, analyze_sentiment_trends, track_topic_evolution, correlate_sentiment_topics, detect_emerging_topics, generate_trend_report, generate_alert_report


def main():
    """Run a quick demo of Trend Analysis Tool."""
    print("=" * 60)
    print("🚀 Trend Analysis Tool - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Configure the logging subsystem from *config*.
    print("📝 Example: setup_logging()")
    result = setup_logging(
        config={}
    )
    print(f"   Result: {result}")
    print()
    # Load text files from *directory*.
    print("📝 Example: load_text_files()")
    result = load_text_files(
        directory="."
    )
    print(f"   Result: {result}")
    print()
    # Extract topics and trends from *documents* via LLM.
    print("📝 Example: extract_topics()")
    result = extract_topics(
        documents=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
