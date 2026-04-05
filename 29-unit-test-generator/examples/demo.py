"""
Demo script for Unit Test Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.test_gen.core import load_config, extract_code_info, analyze_coverage, generate_tests, organize_test_structure


def main():
    """Run a quick demo of Unit Test Generator."""
    print("=" * 60)
    print("🚀 Unit Test Generator - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Extract functions, classes, and imports from a Python file.
    print("📝 Example: extract_code_info()")
    result = extract_code_info(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Analyze what needs testing and estimate coverage requirements.
    print("📝 Example: analyze_coverage()")
    result = analyze_coverage(
        code_info={}
    )
    print(f"   Result: {result}")
    print()
    # Generate unit tests for the code in filepath.
    print("📝 Example: generate_tests()")
    result = generate_tests(
        filepath="sample.txt",
        chat_fn=None  # Uses default LLM chat function
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
