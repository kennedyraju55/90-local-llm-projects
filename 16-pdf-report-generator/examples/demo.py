"""
Demo script for Pdf Report Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.report_generator.core import read_csv_data, summarize_data, generate_report, save_report


def main():
    """Run a quick demo of Pdf Report Generator."""
    print("=" * 60)
    print("🚀 Pdf Report Generator - Demo")
    print("=" * 60)
    print()
    # Read CSV file and return headers and rows.
    print("📝 Example: read_csv_data()")
    result = read_csv_data(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Build a statistical summary of the CSV data for LLM context.
    print("📝 Example: summarize_data()")
    result = summarize_data(
        headers=["item1", "item2", "item3"],
        rows=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    # Use the LLM to generate a structured markdown report.
    print("📝 Example: generate_report()")
    result = generate_report(
        topic="artificial intelligence and machine learning",
        data_summary="This document covers the basics of machine learning."
    )
    print(f"   Result: {result}")
    print()
    # Save the generated report to a file with metadata header.
    print("📝 Example: save_report()")
    result = save_report(
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration.",
        output_path="output.txt",
        topic="artificial intelligence and machine learning"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
