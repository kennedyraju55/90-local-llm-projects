"""
Demo script for Product Description Writer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.product_writer.core import load_config, get_platform_configs, get_feature_benefit_map, map_features_to_benefits, calculate_seo_score, build_prompt, generate_descriptions, generate_ab_variants


def main():
    """Run a quick demo of Product Description Writer."""
    print("=" * 60)
    print("🚀 Product Description Writer - Demo")
    print("=" * 60)
    print()
    # Using load_config
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Using get_platform_configs
    print("📝 Example: get_platform_configs()")
    result = get_platform_configs()
    print(f"   Result: {result}")
    print()
    # Using get_feature_benefit_map
    print("📝 Example: get_feature_benefit_map()")
    result = get_feature_benefit_map()
    print(f"   Result: {result}")
    print()
    # Map product features to customer benefits.
    print("📝 Example: map_features_to_benefits()")
    result = map_features_to_benefits(
        features=["item1", "item2", "item3"]
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
