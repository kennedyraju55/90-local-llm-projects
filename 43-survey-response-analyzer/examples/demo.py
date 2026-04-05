"""
Demo script for Survey Response Analyzer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.survey_analyzer.core import load_config, get_llm_client, load_survey_data, identify_text_columns, identify_demographic_columns, extract_themes, cluster_themes, compute_demographic_crosstabs, highlight_verbatims, generate_recommendations


def main():
    """Run a quick demo of Survey Response Analyzer."""
    print("=" * 60)
    print("🚀 Survey Response Analyzer - Demo")
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
    # Load survey responses from a CSV file.
    print("📝 Example: load_survey_data()")
    result = load_survey_data(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Identify columns likely containing free-text responses.
    print("📝 Example: identify_text_columns()")
    result = identify_text_columns(
        data=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
