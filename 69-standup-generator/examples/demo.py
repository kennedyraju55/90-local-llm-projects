"""
Demo script for Standup Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.standup_gen.core import load_config, load_tasks, get_git_log, get_git_branches, categorize_tasks, extract_ticket_refs, format_ticket_refs, generate_standup, generate_weekly_summary, generate_sprint_review


def main():
    """Run a quick demo of Standup Generator."""
    print("=" * 60)
    print("🚀 Standup Generator - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load tasks from a JSON file or return inline dict/list.
    print("📝 Example: load_tasks()")
    result = load_tasks(
        file_path="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Get git log for the specified number of days, optionally filtered by author.
    print("📝 Example: get_git_log()")
    result = get_git_log()
    print(f"   Result: {result}")
    print()
    # Get list of git branches in the repository.
    print("📝 Example: get_git_branches()")
    result = get_git_branches()
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
