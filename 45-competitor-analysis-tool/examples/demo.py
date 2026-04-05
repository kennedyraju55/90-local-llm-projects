"""
Demo script for Competitor Analysis Tool
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.competitor_analyzer.core import load_config, get_llm_client, generate_swot, generate_feature_matrix, generate_pricing_comparison, generate_market_positioning, generate_comparison, generate_action_items, generate_recommendations


def main():
    """Run a quick demo of Competitor Analysis Tool."""
    print("=" * 60)
    print("🚀 Competitor Analysis Tool - Demo")
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
    # Generate SWOT analysis for the company vs competitors.
    print("📝 Example: generate_swot()")
    result = generate_swot(
        company="TechCorp Inc.",
        competitors=["item1", "item2", "item3"],
        industry="technology"
    )
    print(f"   Result: {result}")
    print()
    # Generate a feature comparison matrix.
    print("📝 Example: generate_feature_matrix()")
    result = generate_feature_matrix(
        company="TechCorp Inc.",
        competitors=["item1", "item2", "item3"],
        industry="technology"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
