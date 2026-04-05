"""
Demo script for Log File Analyzer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.log_analyzer.core import read_log_file, analyze_logs, cluster_errors, match_patterns, detect_anomalies, cluster_errors_local, build_timeline, evaluate_alert_rules, LogLevel, PatternMatch


def main():
    """Run a quick demo of Log File Analyzer."""
    print("=" * 60)
    print("🚀 Log File Analyzer - Demo")
    print("=" * 60)
    print()
    # Read a log file, optionally only the last N lines.
    print("📝 Example: read_log_file()")
    result = read_log_file(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Analyze log content using the LLM.
    print("📝 Example: analyze_logs()")
    result = analyze_logs(
        log_content="2024-01-15 10:30:00 ERROR Failed to connect\n2024-01-15 10:30:01 INFO Retry succeeded",
        focus="productivity"
    )
    print(f"   Result: {result}")
    print()
    # Cluster similar errors using LLM.
    print("📝 Example: cluster_errors()")
    result = cluster_errors(
        log_content="2024-01-15 10:30:00 ERROR Failed to connect\n2024-01-15 10:30:01 INFO Retry succeeded"
    )
    print(f"   Result: {result}")
    print()
    # Match known patterns in log content.
    print("📝 Example: match_patterns()")
    result = match_patterns(
        log_content="2024-01-15 10:30:00 ERROR Failed to connect\n2024-01-15 10:30:01 INFO Retry succeeded"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
