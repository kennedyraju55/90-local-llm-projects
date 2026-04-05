"""
Demo script for Cicd Pipeline Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.cicd_gen.core import load_config, get_platforms, get_stage_catalog, get_secret_template, get_matrix_preset, generate_pipeline, explain_pipeline, extract_config, validate_pipeline_config


def main():
    """Run a quick demo of Cicd Pipeline Generator."""
    print("=" * 60)
    print("🚀 Cicd Pipeline Generator - Demo")
    print("=" * 60)
    print()
    # Load application configuration from config.yaml.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Return all supported CI/CD platforms.
    print("📝 Example: get_platforms()")
    result = get_platforms()
    print(f"   Result: {result}")
    print()
    # Return available pipeline stages.
    print("📝 Example: get_stage_catalog()")
    result = get_stage_catalog()
    print(f"   Result: {result}")
    print()
    # Return secret templates for a platform.
    print("📝 Example: get_secret_template()")
    result = get_secret_template(
        platform="twitter"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
