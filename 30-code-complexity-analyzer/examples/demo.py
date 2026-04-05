"""
Demo script for Code Complexity Analyzer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.complexity_analyzer.core import load_config, calculate_cyclomatic_complexity, calculate_cognitive_complexity, count_lines, calculate_halstead_volume, analyze_dependencies, analyze_file, get_complexity_rating, get_mi_rating, get_llm_suggestions


def main():
    """Run a quick demo of Code Complexity Analyzer."""
    print("=" * 60)
    print("🚀 Code Complexity Analyzer - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Calculate cyclomatic complexity for a function/method node.
    print("📝 Example: calculate_cyclomatic_complexity()")
    result = calculate_cyclomatic_complexity(
        node="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Calculate cognitive complexity (simplified) for a function node.
    print("📝 Example: calculate_cognitive_complexity()")
    result = calculate_cognitive_complexity(
        node="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Count different types of lines in source code.
    print("📝 Example: count_lines()")
    result = count_lines(
        source="def process(data):\n    return [x * 2 for x in data]"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
