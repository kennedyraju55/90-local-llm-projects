"""
Demo script for Household Budget Analyzer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.budget_analyzer.core import load_config, get_config, setup_logging, load_expenses, filter_by_month, compute_category_breakdown, compute_total, display_breakdown, analyze_budget, compare_months


def main():
    """Run a quick demo of Household Budget Analyzer."""
    print("=" * 60)
    print("🚀 Household Budget Analyzer - Demo")
    print("=" * 60)
    print()
    # Load application configuration from YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Return cached configuration, loading on first call.
    print("📝 Example: get_config()")
    result = get_config()
    print(f"   Result: {result}")
    print()
    # Configure logging for the application.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Load expenses from a CSV file.
    print("📝 Example: load_expenses()")
    result = load_expenses(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
