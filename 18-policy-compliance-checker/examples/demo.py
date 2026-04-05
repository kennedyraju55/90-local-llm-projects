"""
Demo script for Policy Compliance Checker
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.compliance_checker.core import read_file, check_compliance, parse_compliance_response, filter_violations, get_score_color, get_score_label


def main():
    """Run a quick demo of Policy Compliance Checker."""
    print("=" * 60)
    print("🚀 Policy Compliance Checker - Demo")
    print("=" * 60)
    print()
    # Read and return the contents of a file.
    print("📝 Example: read_file()")
    result = read_file(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Send document and policy to the LLM for compliance analysis.
    print("📝 Example: check_compliance()")
    result = check_compliance(
        document="The parties agree to the following terms and conditions...",
        policy="Our company collects user email addresses for marketing purposes."
    )
    print(f"   Result: {result}")
    print()
    # Parse the LLM JSON response into a compliance report dict.
    print("📝 Example: parse_compliance_response()")
    result = parse_compliance_response(
        response=["Great product!", "Needs improvement in shipping", "Love the customer service"]
    )
    print(f"   Result: {result}")
    print()
    # Filter violations by severity level.
    print("📝 Example: filter_violations()")
    result = filter_violations(
        violations=[],
        severity="HIGH"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
