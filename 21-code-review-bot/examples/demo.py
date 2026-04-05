"""
Demo script for Code Review Bot
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.code_reviewer.core import review_single_file, review_multiple_files, generate_autofix, export_report


def main():
    """Run a quick demo of Code Review Bot."""
    print("=" * 60)
    print("🚀 Code Review Bot - Demo")
    print("=" * 60)
    print()
    # Review a single code file and return structured results.
    print("📝 Example: review_single_file()")
    result = review_single_file(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Review multiple files and return aggregated results.
    print("📝 Example: review_multiple_files()")
    result = review_multiple_files(
        filepaths=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    # Generate auto-fix suggestions based on review results.
    print("📝 Example: generate_autofix()")
    result = generate_autofix(
        filepath="sample.txt",
        review_text="The service was okay but delivery took too long. Product quality is decent."
    )
    print(f"   Result: {result}")
    print()
    # Export review results to a file.
    print("📝 Example: export_report()")
    result = export_report(
        results=[{"key": "value"}],
        output_path="output.txt"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
