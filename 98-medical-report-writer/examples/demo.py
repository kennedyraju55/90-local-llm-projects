"""
Demo script for Medical Report Writer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from medical_report_writer.core import (
    load_config,
    REPORT_TYPES,
    DISCLAIMER,
    display_disclaimer,
    format_report,
    extract_key_findings,
    ReportSession,
)
from medical_report_writer.config import load_config


def main():
    """Run a quick demo of Medical Report Writer."""
    print("=" * 60)
    print("🚀 Medical Report Writer - Demo")
    print("=" * 60)
    print()

    # Show disclaimer
    print("📝 Example: display_disclaimer()")
    display_disclaimer()
    print()

    # Load configuration
    print("📝 Example: load_config()")
    config = load_config()
    print(f"   Result: {config}")
    print()

    # Show available report types
    print("📝 Example: REPORT_TYPES")
    for key, info in REPORT_TYPES.items():
        print(f"   • {info['name']} ({key})")
    print()

    # Format a sample report
    print("📝 Example: format_report()")
    sample = "DISCHARGE SUMMARY\n\n\n\nPatient was admitted on 2024-01-15.\n\n\n\nDischarged on 2024-01-20."
    formatted = format_report(sample, "compact")
    print(f"   Compact result:\n{formatted}")
    print()

    # Extract key findings
    print("📝 Example: extract_key_findings()")
    sample_report = (
        "ASSESSMENT:\n"
        "- Diagnosis: Community-acquired pneumonia\n"
        "- Finding: Bilateral infiltrates on chest X-ray\n"
        "PLAN:\n"
        "- Continue IV antibiotics\n"
        "- Follow-up in 2 weeks"
    )
    findings = extract_key_findings(sample_report)
    for f in findings:
        print(f"   • {f}")
    print()

    # Report session tracking
    print("📝 Example: ReportSession")
    session = ReportSession()
    session.add_report("progress_note", "Sample data", "Sample report")
    session.add_report("discharge_summary", "Sample data 2", "Sample report 2")
    summary = session.get_summary()
    print(f"   Session summary: {summary}")
    print()

    print("✅ Demo complete! See README.md for more examples.")
    print()
    print("⚠️  To generate actual reports, ensure Ollama is running:")
    print("    ollama serve")
    print("    ollama pull gemma4")


if __name__ == "__main__":
    main()
