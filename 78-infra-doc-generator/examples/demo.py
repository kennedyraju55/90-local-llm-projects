"""
Demo script for Infra Doc Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.infra_doc_gen.core import load_config, detect_config_type, extract_dependencies, generate_docs, generate_diagram, generate_dependency_map


def main():
    """Run a quick demo of Infra Doc Generator."""
    print("=" * 60)
    print("🚀 Infra Doc Generator - Demo")
    print("=" * 60)
    print()
    # Load application configuration from config.yaml.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Detect the type of infrastructure config file.
    print("📝 Example: detect_config_type()")
    result = detect_config_type(
        filepath="sample.txt",
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration."
    )
    print(f"   Result: {result}")
    print()
    # Extract service/resource dependencies from config content.
    print("📝 Example: extract_dependencies()")
    result = extract_dependencies(
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration.",
        config_type="docker-compose"
    )
    print(f"   Result: {result}")
    print()
    # Generate documentation from an infrastructure config file.
    print("📝 Example: generate_docs()")
    result = generate_docs(
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration.",
        config_type="docker-compose"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
