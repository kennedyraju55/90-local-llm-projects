"""
Demo script for Debate Topic Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.debate_gen.core import load_config, generate_debate_topics, generate_moderator_guide, rate_evidence_strength, check_service, to_dict, Argument, CounterargumentPair, JudgingCriteria, ModeratorGuide


def main():
    """Run a quick demo of Debate Topic Generator."""
    print("=" * 60)
    print("🚀 Debate Topic Generator - Demo")
    print("=" * 60)
    print()
    # Using load_config
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Generate debate topics using the LLM.
    print("📝 Example: generate_debate_topics()")
    result = generate_debate_topics(
        subject="Introduction to Python Programming"
    )
    print(f"   Result: {result}")
    print()
    # Generate a moderator guide for a debate motion.
    print("📝 Example: generate_moderator_guide()")
    result = generate_moderator_guide(
        motion="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Rate the strength of a piece of evidence.
    print("📝 Example: rate_evidence_strength()")
    result = rate_evidence_strength(
        evidence="sample data"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
