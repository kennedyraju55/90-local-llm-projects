"""
Demo script for Ehr Deidentifier
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.ehr_deidentifier.core import load_config, regex_preprocess, configurable_regex_preprocess, deidentify_text, read_file, write_file, batch_deidentify, display_results, log_operation, get_log


def main():
    """Run a quick demo of Ehr Deidentifier."""
    print("=" * 60)
    print("🚀 Ehr Deidentifier - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Apply regex-based PII detection before LLM processing.
    print("📝 Example: regex_preprocess()")
    result = regex_preprocess(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Apply configurable regex-based PII detection.
    print("📝 Example: configurable_regex_preprocess()")
    result = configurable_regex_preprocess(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # De-identify text using regex pre-processing followed by LLM analysis.
    print("📝 Example: deidentify_text()")
    result = deidentify_text(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
