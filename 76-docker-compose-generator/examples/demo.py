"""
Demo script for Docker Compose Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.docker_gen.core import load_config, get_service_catalog, get_flat_catalog, get_env_profile, generate_compose, explain_compose, extract_yaml, validate_compose


def main():
    """Run a quick demo of Docker Compose Generator."""
    print("=" * 60)
    print("🚀 Docker Compose Generator - Demo")
    print("=" * 60)
    print()
    # Load application configuration from config.yaml.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Return the full service catalog organized by category.
    print("📝 Example: get_service_catalog()")
    result = get_service_catalog()
    print(f"   Result: {result}")
    print()
    # Return a flat dictionary of all services.
    print("📝 Example: get_flat_catalog()")
    result = get_flat_catalog()
    print(f"   Result: {result}")
    print()
    # Return configuration profile for an environment.
    print("📝 Example: get_env_profile()")
    result = get_env_profile(
        env="production"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
