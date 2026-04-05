"""
Demo script for Incident Report Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.incident_reporter.core import generate_report, generate_timeline, build_timeline, calculate_impact, generate_lessons_learned, get_template, severity_label, Priority, TimelineEntry, ImpactAssessment


def main():
    """Run a quick demo of Incident Report Generator."""
    print("=" * 60)
    print("🚀 Incident Report Generator - Demo")
    print("=" * 60)
    print()
    # Generate an incident report from raw logs.
    print("📝 Example: generate_report()")
    result = generate_report(
        logs="2024-01-15 10:30:00 ERROR Connection failed\n2024-01-15 10:31:00 INFO Recovered",
        incident_type="outage"
    )
    print(f"   Result: {result}")
    print()
    # Extract a timeline from incident logs.
    print("📝 Example: generate_timeline()")
    result = generate_timeline(
        logs="2024-01-15 10:30:00 ERROR Connection failed\n2024-01-15 10:31:00 INFO Recovered"
    )
    print(f"   Result: {result}")
    print()
    # Parse logs into structured timeline entries.
    print("📝 Example: build_timeline()")
    result = build_timeline(
        logs="2024-01-15 10:30:00 ERROR Connection failed\n2024-01-15 10:31:00 INFO Recovered"
    )
    print(f"   Result: {result}")
    print()
    # Calculate impact assessment from incident data.
    print("📝 Example: calculate_impact()")
    result = calculate_impact(
        logs="2024-01-15 10:30:00 ERROR Connection failed\n2024-01-15 10:31:00 INFO Recovered"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
