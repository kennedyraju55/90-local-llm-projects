"""
Demo script for Medical Lit Summarizer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.medical_summarizer.core import extract_section, summarize_paper, extract_pico, rate_evidence_quality, format_citation


def main():
    """Run a quick demo of Medical Lit Summarizer."""
    print("=" * 60)
    print("🚀 Medical Lit Summarizer - Demo")
    print("=" * 60)
    print()
    # Extract a specific section from a paper using the LLM.
    print("📝 Example: extract_section()")
    result = extract_section(
        paper_text="This research paper explores the effects of machine learning on healthcare outcomes...",
        section_key="sample data",
        section_prompt="Explain the concept in simple terms.",
        detail_level="detailed"
    )
    print(f"   Result: {result}")
    print()
    # Summarize a medical paper into structured sections.
    print("📝 Example: summarize_paper()")
    result = summarize_paper(
        paper_text="This research paper explores the effects of machine learning on healthcare outcomes..."
    )
    print(f"   Result: {result}")
    print()
    # Extract PICO framework elements from a medical paper.
    print("📝 Example: extract_pico()")
    result = extract_pico(
        paper_text="This research paper explores the effects of machine learning on healthcare outcomes..."
    )
    print(f"   Result: {result}")
    print()
    # Rate the quality of evidence in a medical paper.
    print("📝 Example: rate_evidence_quality()")
    result = rate_evidence_quality(
        paper_text="This research paper explores the effects of machine learning on healthcare outcomes..."
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
