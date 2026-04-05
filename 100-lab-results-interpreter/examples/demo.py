"""
Demo script for Lab Results Interpreter
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.lab_results_interpreter.core import (
    display_disclaimer,
    get_reference_range,
    interpret_results,
    identify_abnormalities,
    suggest_followup_tests,
    explain_lab_value,
    LabSession,
    REFERENCE_RANGES,
    LAB_PANELS,
)
from src.lab_results_interpreter.config import load_config


def main():
    """Run a quick demo of Lab Results Interpreter."""
    print("=" * 60)
    print("🚀 Lab Results Interpreter - Demo")
    print("=" * 60)
    print()

    # Display disclaimer
    print("📝 Example: display_disclaimer()")
    result = display_disclaimer()
    print(f"   Result: {result[:80]}...")
    print()

    # Load configuration
    print("📝 Example: load_config()")
    config = load_config()
    print(f"   Result: model={config['model']}, temp={config['temperature']}")
    print()

    # Get reference range
    print("📝 Example: get_reference_range('CBC', 'WBC')")
    ref = get_reference_range("CBC", "WBC")
    print(f"   Result: {ref}")
    print()

    # List available panels
    print("📝 Example: LAB_PANELS")
    print(f"   Result: {LAB_PANELS}")
    print()

    # Show CBC reference ranges
    print("📝 Example: REFERENCE_RANGES['CBC']")
    for test, info in REFERENCE_RANGES["CBC"].items():
        print(f"   {test}: {info['range']} {info['unit']} ({info['description']})")
    print()

    # Create a session
    print("📝 Example: LabSession()")
    session = LabSession()
    session.add_interpretation(
        lab_results="WBC: 12.5, RBC: 4.8, Hemoglobin: 11.2",
        interpretation="WBC slightly elevated; Hemoglobin low.",
        panel_type="CBC",
        patient_context="45-year-old female",
    )
    summary = session.get_summary()
    print(f"   Summary: {summary}")
    print()

    print("✅ Demo complete! See README.md for more examples.")
    print()
    print("💡 To run with LLM (requires Ollama):")
    print("   interpret_results('WBC: 12.5, Hemoglobin: 11.2', panel_type='CBC')")


if __name__ == "__main__":
    main()
