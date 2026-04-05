"""
Demo script for Stack Trace Explainer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.stack_explainer.core import explain_trace, generate_fix_code, find_similar_errors


def main():
    """Run a quick demo of Stack Trace Explainer."""
    print("=" * 60)
    print("🚀 Stack Trace Explainer - Demo")
    print("=" * 60)
    print()
    # Analyze a stack trace and return explanation.
    print("📝 Example: explain_trace()")
    result = explain_trace(
        trace="Traceback (most recent call last):\n  File \"main.py\", line 5\nValueError: invalid literal"
    )
    print(f"   Result: {result}")
    print()
    # Generate fix code based on trace and explanation.
    print("📝 Example: generate_fix_code()")
    result = generate_fix_code(
        trace="Traceback (most recent call last):\n  File \"main.py\", line 5\nValueError: invalid literal",
        explanation="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Find similar errors and distinguish between them.
    print("📝 Example: find_similar_errors()")
    result = find_similar_errors(
        trace="Traceback (most recent call last):\n  File \"main.py\", line 5\nValueError: invalid literal"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
