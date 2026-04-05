"""
Demo script for Sql Query Generator
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.sql_gen.core import load_config, read_schema, parse_schema_text, get_table_names, visualize_schema, generate_sql, generate_sql_no_schema, optimize_query, load_history, save_to_history


def main():
    """Run a quick demo of Sql Query Generator."""
    print("=" * 60)
    print("🚀 Sql Query Generator - Demo")
    print("=" * 60)
    print()
    # Load configuration from YAML file.
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()
    # Read a SQL schema file.
    print("📝 Example: read_schema()")
    result = read_schema(
        schema_path="users(id INT, name TEXT, email TEXT, created_at DATE); orders(id INT, user_id INT, total DECIMAL)"
    )
    print(f"   Result: {result}")
    print()
    # Extract table info from schema text.
    print("📝 Example: parse_schema_text()")
    result = parse_schema_text(
        schema_text="CREATE TABLE users (id INT PRIMARY KEY, name TEXT, email TEXT);\nCREATE TABLE orders (id INT, user_id INT, total DECIMAL);"
    )
    print(f"   Result: {result}")
    print()
    # Extract table names from schema text.
    print("📝 Example: get_table_names()")
    result = get_table_names(
        schema_text="CREATE TABLE users (id INT PRIMARY KEY, name TEXT, email TEXT);\nCREATE TABLE orders (id INT, user_id INT, total DECIMAL);"
    )
    print(f"   Result: {result}")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
