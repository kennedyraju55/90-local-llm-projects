"""
Demo script for Api Doc Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.api_doc_gen.core import generate_docs, generate_openapi, export_docs


def main():
    """Run a quick demo of Api Doc Generator."""
    print("=" * 60)
    print("🚀 Api Doc Generator - Demo")
    print("=" * 60)
    print()
    # Generate API documentation for all files in the source path.
    print("📝 Example: generate_docs()")
    result = generate_docs(
        source_path="."
    )
    print(f"   Result: {result}")
    print()
    # Generate OpenAPI specification from source code.
    print("📝 Example: generate_openapi()")
    result = generate_openapi(
        source_path="."
    )
    print(f"   Result: {result}")
    print()
    # Export documentation to file.
    print("📝 Example: export_docs()")
    result = export_docs(
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration.",
        output_path="output.txt"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
