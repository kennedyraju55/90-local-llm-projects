"""
Demo script for Invoice Extractor
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.invoice_extractor.core import extract_invoice_data, batch_extract, detect_duplicates, categorize_items, export_to_csv


def main():
    """Run a quick demo of Invoice Extractor."""
    print("=" * 60)
    print("🚀 Invoice Extractor - Demo")
    print("=" * 60)
    print()
    # Send invoice text to the LLM and parse the structured JSON response.
    print("📝 Example: extract_invoice_data()")
    result = extract_invoice_data(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Extract data from multiple invoice files.
    print("📝 Example: batch_extract()")
    result = batch_extract(
        file_paths=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    # Detect potential duplicate invoices by invoice number and vendor.
    print("📝 Example: detect_duplicates()")
    result = detect_duplicates(
        invoices=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    # Categorize invoice line items using the LLM.
    print("📝 Example: categorize_items()")
    result = categorize_items(
        invoice_data={}
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
