"""
Demo script for Sales Email Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.sales_email_gen.core import load_config, generate_email, generate_variants, research_prospect, generate_follow_up_sequence, score_personalization, get_template, list_templates


def main():
    """Run a quick demo of Sales Email Generator."""
    print("=" * 60)
    print("🚀 Sales Email Generator - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Generate a personalised sales email via the LLM.
    print("📝 Example: generate_email()")
    result = generate_email(
        prospect={"name": "Jane Doe", "company": "TechCorp", "role": "CTO"},
        product="Smart Assistant Pro",
        tone="friendly and professional"
    )
    print(f"   Result: {result}")
    print()
    # Generate multiple email variants for A/B testing.
    print("📝 Example: generate_variants()")
    result = generate_variants(
        prospect={"name": "Jane Doe", "company": "TechCorp", "role": "CTO"},
        product="Smart Assistant Pro",
        tone="friendly and professional"
    )
    print(f"   Result: {result}")
    print()
    # Use the LLM to generate a research profile for the prospect.
    print("📝 Example: research_prospect()")
    result = research_prospect(
        prospect_info={"name": "Jane Doe", "company": "TechCorp", "role": "CTO"}
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
