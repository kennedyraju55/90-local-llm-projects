"""
Demo script for Stock Report Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.stock_reporter.core import load_config, get_llm_client, load_stock_data, compute_metrics, compute_technical_indicators, assess_risk, compare_tickers, generate_report


def main():
    """Run a quick demo of Stock Report Generator."""
    print("=" * 60)
    print("🚀 Stock Report Generator - Demo")
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
    # Load stock data from a CSV file.
    print("📝 Example: load_stock_data()")
    result = load_stock_data(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Compute basic technical analysis metrics from stock data.
    print("📝 Example: compute_metrics()")
    result = compute_metrics(
        data=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
