"""
Demo script for Commit Message Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.commit_gen.core import generate_commit_messages, generate_batch_messages


def main():
    """Run a quick demo of Commit Message Generator."""
    print("=" * 60)
    print("🚀 Commit Message Generator - Demo")
    print("=" * 60)
    print()
    # Generate conventional commit messages from a diff.
    print("📝 Example: generate_commit_messages()")
    result = generate_commit_messages(
        diff="--- a/utils.py\n+++ b/utils.py\n@@ -5,3 +5,6 @@\n def process(data):\n-    return data\n+    return data.strip()"
    )
    print(f"   Result: {result}")
    print()
    # Generate commit messages for multiple diffs (batch mode).
    print("📝 Example: generate_batch_messages()")
    result = generate_batch_messages(
        diffs=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
