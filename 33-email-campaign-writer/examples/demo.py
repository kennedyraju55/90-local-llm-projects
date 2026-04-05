"""
Demo script for Email Campaign Writer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.email_campaign.core import load_config, setup_logging, build_prompt, generate_campaign, generate_subject_variants, build_email_sequence, extract_personalization_tokens, preview_html, render_email, calculate_sequence_timeline


def main():
    """Run a quick demo of Email Campaign Writer."""
    print("=" * 60)
    print("🚀 Email Campaign Writer - Demo")
    print("=" * 60)
    print()
    # Load and cache application configuration from config.yaml.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Configure logging from config.yaml.
    print("📝 Example: setup_logging()")
    result = setup_logging()
    print(f"   Result: {result}")
    print()
    # Build the email campaign generation prompt.
    print("📝 Example: build_prompt()")
    result = build_prompt(
        product="Smart Assistant Pro",
        audience="tech professionals aged 25-45",
        num_emails=5,
        campaign_type="promotional"
    )
    print(f"   Result: {result}")
    print()
    # Generate an email campaign using the LLM and return raw text.
    print("📝 Example: generate_campaign()")
    result = generate_campaign(
        product="Smart Assistant Pro",
        audience="tech professionals aged 25-45",
        num_emails=5,
        campaign_type="promotional"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
