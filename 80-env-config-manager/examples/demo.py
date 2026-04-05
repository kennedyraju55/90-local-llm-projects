"""
Demo script for Env Config Manager
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.env_manager.core import load_config, parse_env_file, detect_secrets, compare_envs, generate_migration_script, validate_env, generate_env_template, suggest_missing_vars, generate_env_documentation


def main():
    """Run a quick demo of Env Config Manager."""
    print("=" * 60)
    print("🚀 Env Config Manager - Demo")
    print("=" * 60)
    print()
    # Load application configuration from config.yaml.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Parse a .env file into key-value pairs.
    print("📝 Example: parse_env_file()")
    result = parse_env_file(
        filepath="sample.txt"
    )
    print(f"   Result: {result}")
    print()
    # Detect potential secrets in environment variables.
    print("📝 Example: detect_secrets()")
    result = detect_secrets(
        env_vars={}
    )
    print(f"   Result: {result}")
    print()
    # Compare two environment configurations.
    print("📝 Example: compare_envs()")
    result = compare_envs(
        env1={},
        env2={}
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
