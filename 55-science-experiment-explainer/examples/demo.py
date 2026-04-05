"""
Demo script for Science Experiment Explainer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.science_explainer.core import setup_logging, parse_response, explain_experiment, suggest_alternatives, search_experiments, validate_experiment_data, export_experiment, get, raw, get_safety_info


def main():
    """Run a quick demo of Science Experiment Explainer."""
    print("=" * 60)
    print("🚀 Science Experiment Explainer - Demo")
    print("=" * 60)
    print()
    # Configure the root logger based on config values.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Parse an LLM response that may be wrapped in markdown code fences.
    print("📝 Example: parse_response()")
    result = parse_response(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Generate an experiment explanation via the LLM.
    print("📝 Example: explain_experiment()")
    result = explain_experiment(
        experiment="photosynthesis",
        level="intermediate"
    )
    print(f"   Result: {result}")
    print()
    # Ask the LLM for alternative experiments related to the given one.
    print("📝 Example: suggest_alternatives()")
    result = suggest_alternatives(
        experiment="photosynthesis",
        level="intermediate"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
