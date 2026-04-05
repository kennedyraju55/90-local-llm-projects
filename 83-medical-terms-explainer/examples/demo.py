"""
Demo script for Medical Terms Explainer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.medical_terms.core import load_config, explain_term, get_pronunciation, get_visual_aid, get_related_conditions, decode_abbreviation, search_abbreviations


def main():
    """Run a quick demo of Medical Terms Explainer."""
    print("=" * 60)
    print("🚀 Medical Terms Explainer - Demo")
    print("=" * 60)
    print()
    # Load configuration from config.yaml.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Explain a single medical term using the LLM.
    print("📝 Example: explain_term()")
    result = explain_term(
        term="hypertension"
    )
    print(f"   Result: {result}")
    print()
    # Look up the phonetic pronunciation of a medical term.
    print("📝 Example: get_pronunciation()")
    result = get_pronunciation(
        term="hypertension"
    )
    print(f"   Result: {result}")
    print()
    # Look up a visual-aid reference for a medical topic.
    print("📝 Example: get_visual_aid()")
    result = get_visual_aid(
        term="hypertension"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
