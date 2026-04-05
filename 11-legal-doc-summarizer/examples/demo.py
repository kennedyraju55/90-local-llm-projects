"""
Demo script for Legal Doc Summarizer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.legal_summarizer.core import summarize_document, extract_clauses, score_risks, compare_documents, generate_export_markdown


def main():
    """Run a quick demo of Legal Doc Summarizer."""
    print("=" * 60)
    print("🚀 Legal Doc Summarizer - Demo")
    print("=" * 60)
    print()
    # Send document text to the LLM for analysis and summarization.
    print("📝 Example: summarize_document()")
    result = summarize_document(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Extract and categorize individual clauses from a legal document.
    print("📝 Example: extract_clauses()")
    result = extract_clauses(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Analyze document for risk factors and return risk scores.
    print("📝 Example: score_risks()")
    result = score_risks(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Compare multiple legal documents side by side.
    print("📝 Example: compare_documents()")
    result = compare_documents(
        file_paths=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
