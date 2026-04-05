"""
Demo script for Password Strength Advisor
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.password_advisor.core import calculate_entropy, check_breach_database, generate_policy, analyze_password_llm, analyze_policy_llm, generate_password, bulk_analyze, StrengthLevel, EntropyResult, BreachCheckResult


def main():
    """Run a quick demo of Password Strength Advisor."""
    print("=" * 60)
    print("🚀 Password Strength Advisor - Demo")
    print("=" * 60)
    print()
    # Calculate password entropy in bits.
    print("📝 Example: calculate_entropy()")
    result = calculate_entropy(
        password="MyP@ssw0rd123!"
    )
    print(f"   Result: {result}")
    print()
    # Check if a password is in known breach databases (conceptual local check).
    print("📝 Example: check_breach_database()")
    result = check_breach_database(
        password="MyP@ssw0rd123!"
    )
    print(f"   Result: {result}")
    print()
    # Generate a password policy based on NIST SP 800-63B.
    print("📝 Example: generate_policy()")
    result = generate_policy()
    print(f"   Result: {result}")
    print()
    # Analyze a password using the LLM (masked characteristics only).
    print("📝 Example: analyze_password_llm()")
    result = analyze_password_llm(
        password="MyP@ssw0rd123!"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
