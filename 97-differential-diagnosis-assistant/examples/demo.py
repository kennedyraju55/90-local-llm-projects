"""
Demo script for Differential Diagnosis Assistant
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.differential_diagnosis.core import (
    load_config,
    assess_urgency,
    get_affected_systems,
    display_disclaimer,
    generate_differential,
    get_workup_recommendations,
    compare_diagnoses,
    DiagnosisSession,
)


def main():
    """Run a quick demo of Differential Diagnosis Assistant."""
    print("=" * 60)
    print("🚀 Differential Diagnosis Assistant - Demo")
    print("=" * 60)
    print()

    # Load configuration
    print("📝 Example: load_config()")
    config = load_config()
    print(f"   Result: {config}")
    print()

    # Assess urgency level
    print("📝 Example: assess_urgency('chest pain with shortness of breath')")
    level, label, advice = assess_urgency("chest pain with shortness of breath")
    print(f"   Level: {level}, Label: {label}")
    print(f"   Advice: {advice}")
    print()

    # Identify affected body systems
    print("📝 Example: get_affected_systems('headache, fever, nausea')")
    systems = get_affected_systems("headache, fever, nausea")
    print(f"   Affected systems: {systems}")
    print()

    # Display disclaimer
    print("📝 Example: display_disclaimer()")
    display_disclaimer()
    print()

    # Track a diagnosis session
    print("📝 Example: DiagnosisSession()")
    session = DiagnosisSession()
    session.add_entry(
        symptoms="chest pain radiating to left arm",
        patient_info="55M, HTN, DM2, smoker",
        exam_findings="diaphoretic, BP 160/95",
        urgency=5,
        systems=["cardiovascular"],
        response="Top differential: ACS (STEMI vs NSTEMI)",
    )
    summary = session.get_summary()
    print(f"   Session summary: {summary}")
    print()

    # NOTE: The following functions require Ollama to be running.
    # Uncomment to test with a live LLM:
    #
    # print("📝 Example: generate_differential()")
    # result = generate_differential(
    #     symptoms="sudden onset severe headache, worst of life, neck stiffness",
    #     patient_info="35F, no significant PMH",
    #     exam_findings="photophobia, positive Kernig sign",
    # )
    # print(f"   Result: {result[:200]}...")
    #
    # print("📝 Example: get_workup_recommendations()")
    # workup = get_workup_recommendations("Subarachnoid hemorrhage")
    # print(f"   Result: {workup[:200]}...")
    #
    # print("📝 Example: compare_diagnoses()")
    # comparison = compare_diagnoses(
    #     "Subarachnoid hemorrhage", "Meningitis",
    #     "sudden severe headache with neck stiffness",
    # )
    # print(f"   Result: {comparison[:200]}...")

    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
