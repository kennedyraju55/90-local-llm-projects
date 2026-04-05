"""
Demo script for Sentiment Analysis Dashboard
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.sentiment_analyzer.core import load_config, get_llm_client, read_text_file, read_batch_files, analyze_sentiment, batch_analyze, compute_sentiment_distribution, compute_trend_over_time, extract_word_cloud_data, compare_sources


def main():
    """Run a quick demo of Sentiment Analysis Dashboard."""
    print("=" * 60)
    print("🚀 Sentiment Analysis Dashboard - Demo")
    print("=" * 60)
    print()
    # Load configuration from config.yaml.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Get LLM client with proper path setup.
    print("📝 Example: get_llm_client()")
    result = get_llm_client()
    print(f"   Result: {result}")
    print()
    # Read a text file and return non-empty lines.
    print("📝 Example: read_text_file()")
    result = read_text_file(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Read multiple text files for batch processing.
    print("📝 Example: read_batch_files()")
    result = read_batch_files(
        file_paths=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
