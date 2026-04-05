"""
Demo script for Csv Data Analyzer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.csv_analyzer.core import load_config, get_llm_client, load_csv, detect_column_types, generate_statistical_summary, compute_correlations, suggest_charts, generate_data_summary, analyze_data, export_insights


def main():
    """Run a quick demo of Csv Data Analyzer."""
    print("=" * 60)
    print("🚀 Csv Data Analyzer - Demo")
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
    # Load a CSV file into a pandas DataFrame.
    print("📝 Example: load_csv()")
    result = load_csv(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Auto-detect and categorize column types.
    print("📝 Example: detect_column_types()")
    result = detect_column_types(
        df=None  # Pass a pandas DataFrame
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
