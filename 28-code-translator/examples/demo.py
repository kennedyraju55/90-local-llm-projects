"""
Demo script for Code Translator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.code_translator.core import load_config, detect_source_language, get_language_name, get_language_ext, read_source_file, translate_code, validate_syntax, compare_codes, batch_translate_files, generate_translation_notes


def main():
    """Run a quick demo of Code Translator."""
    print("=" * 60)
    print("🚀 Code Translator - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Detect the source language from file extension.
    print("📝 Example: detect_source_language()")
    result = detect_source_language(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Get display name for a language code.
    print("📝 Example: get_language_name()")
    result = get_language_name(
        lang="python"
    )
    print(f"   Result: {result}")
    print()
    # Get file extension for a language code.
    print("📝 Example: get_language_ext()")
    result = get_language_ext(
        lang="python"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
