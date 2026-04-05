"""
Demo script for Cybersecurity Alert Summarizer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.cyber_alert.core import summarize_alert, prioritize_alerts, extract_iocs, lookup_cve, extract_cves, calculate_threat_score, correlate_alerts, label, Severity, IOCResult


def main():
    """Run a quick demo of Cybersecurity Alert Summarizer."""
    print("=" * 60)
    print("🚀 Cybersecurity Alert Summarizer - Demo")
    print("=" * 60)
    print()
    # Summarize a security alert using the LLM.
    print("📝 Example: summarize_alert()")
    result = summarize_alert(
        alert_text="CRITICAL: Unauthorized access attempt detected from IP 192.168.1.100"
    )
    print(f"   Result: {result}")
    print()
    # Prioritize multiple alerts by risk level.
    print("📝 Example: prioritize_alerts()")
    result = prioritize_alerts(
        alert_text="CRITICAL: Unauthorized access attempt detected from IP 192.168.1.100"
    )
    print(f"   Result: {result}")
    print()
    # Extract Indicators of Compromise from alert text.
    print("📝 Example: extract_iocs()")
    result = extract_iocs(
        text="The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."
    )
    print(f"   Result: {result}")
    print()
    # Look up CVE information from the local database.
    print("📝 Example: lookup_cve()")
    result = lookup_cve(
        cve_id="sample data"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
