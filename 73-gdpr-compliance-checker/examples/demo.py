"""
Demo script for Gdpr Compliance Checker
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.gdpr_checker.core import check_compliance, generate_checklist, build_article_checklist, map_data_flows, generate_dpo_recommendations, create_audit_entry, ComplianceStatus, ChecklistItem, DataFlowEntry, AuditLogEntry


def main():
    """Run a quick demo of Gdpr Compliance Checker."""
    print("=" * 60)
    print("🚀 Gdpr Compliance Checker - Demo")
    print("=" * 60)
    print()
    # Check content for GDPR compliance using LLM.
    print("📝 Example: check_compliance()")
    result = check_compliance(
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration.",
        check_type="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Generate a GDPR compliance checklist using LLM.
    print("📝 Example: generate_checklist()")
    result = generate_checklist(
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration."
    )
    print(f"   Result: {result}")
    print()
    # Build an article-by-article compliance checklist from content analysis.
    print("📝 Example: build_article_checklist()")
    result = build_article_checklist(
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration."
    )
    print(f"   Result: {result}")
    print()
    # Extract data flow mappings from document content.
    print("📝 Example: map_data_flows()")
    result = map_data_flows(
        content="The quick brown fox jumps over the lazy dog. This is sample content for demonstration."
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
