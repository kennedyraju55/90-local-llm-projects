"""
Demo script for Kpi Dashboard Reporter
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.kpi_reporter.core import load_config, load_kpi_data, safe_float, compute_kpi_trends, track_goals, detect_anomalies, compute_moving_average, generate_kpi_report, generate_executive_summary, generate_alert_summary


def main():
    """Run a quick demo of Kpi Dashboard Reporter."""
    print("=" * 60)
    print("🚀 Kpi Dashboard Reporter - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load KPI data from a CSV file.
    print("📝 Example: load_kpi_data()")
    result = load_kpi_data(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Safely convert a value to float, stripping $, %, and commas.
    print("📝 Example: safe_float()")
    result = safe_float(
        val="sample data"
    )
    print(f"   Result: {result}")
    print()
    # Compute trends and changes for each KPI column.
    print("📝 Example: compute_kpi_trends()")
    result = compute_kpi_trends(
        data=[{"key": "value"}]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
