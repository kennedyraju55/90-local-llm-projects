"""
Demo script for Code Snippet Search
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.code_search.core import load_config, get_file_hash, detect_language, scan_directory, build_search_context, score_relevance, rank_files, search_code, save_index_cache, load_index_cache


def main():
    """Run a quick demo of Code Snippet Search."""
    print("=" * 60)
    print("🚀 Code Snippet Search - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Compute MD5 hash of a file for cache invalidation.
    print("📝 Example: get_file_hash()")
    result = get_file_hash(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Detect programming language from file extension.
    print("📝 Example: detect_language()")
    result = detect_language(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Scan a directory and read code files with metadata.
    print("📝 Example: scan_directory()")
    result = scan_directory(
        directory="."
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
