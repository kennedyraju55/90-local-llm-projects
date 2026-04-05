"""
Demo script for Home Automation Scripter
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.home_automation.core import load_config, load_rules, save_rule, delete_rule, validate_script, list_templates, get_template, get_template_categories, generate_from_template, detect_syntax


def main():
    """Run a quick demo of Home Automation Scripter."""
    print("=" * 60)
    print("🚀 Home Automation Scripter - Demo")
    print("=" * 60)
    print()
    # Load configuration from a YAML file, falling back to defaults.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Load saved automation rules from JSON.
    print("📝 Example: load_rules()")
    result = load_rules()
    print(f"   Result: {result}")
    print()
    # Persist a new automation rule and return it with id/timestamp.
    print("📝 Example: save_rule()")
    result = save_rule(
        rule={}
    )
    print(f"   Result: {result}")
    print()
    # Delete a rule by its integer id. Returns True if found and deleted.
    print("📝 Example: delete_rule()")
    result = delete_rule(
        rule_id=5
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
