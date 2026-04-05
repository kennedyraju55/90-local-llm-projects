"""
Demo script for Patient Intake Summarizer
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.patient_intake_summarizer.core import (
    load_config,
    INTAKE_CATEGORIES,
    summarize_intake,
    extract_medical_history,
    generate_pre_visit_summary,
    identify_risk_factors,
    flag_missing_info,
    display_disclaimer,
    IntakeSession,
)


SAMPLE_INTAKE = """
Patient: Jane Doe, 52F, DOB: 1973-03-15
Chief Complaint: Persistent lower back pain for 3 weeks, radiating to left leg.
Medical History: Type 2 diabetes mellitus (diagnosed 2018), hypertension (2015),
  hyperlipidemia. Previous episode of sciatica (2021).
Surgical History: Appendectomy (1995), cesarean section (2001).
Medications: Metformin 500mg BID, Lisinopril 10mg daily, Atorvastatin 20mg daily.
Allergies: Penicillin (rash), sulfa drugs (hives).
Family History: Father — MI at age 60, Mother — breast cancer at age 65,
  Sister — Type 2 diabetes.
Social History: Non-smoker, occasional alcohol (1-2 drinks/week), works as an
  office manager, sedentary lifestyle, married, 2 children.
Review of Systems: Denies fever, chills, weight loss. Reports occasional numbness
  in left foot. Denies chest pain, SOB. Reports mild fatigue.
"""


def main():
    """Run a quick demo of Patient Intake Summarizer."""
    print("=" * 60)
    print("🏥 Patient Intake Summarizer - Demo")
    print("=" * 60)
    print()

    # Show disclaimer
    print("📝 Displaying clinical disclaimer...")
    display_disclaimer()
    print()

    # Show configuration
    print("📝 Example: load_config()")
    result = load_config()
    print(f"   Result: {result}")
    print()

    # Show intake categories
    print("📝 Available intake categories:")
    for key, desc in INTAKE_CATEGORIES.items():
        print(f"   • {key}: {desc}")
    print()

    # Demo session tracking
    print("📝 Example: IntakeSession")
    session = IntakeSession()
    session.add_summary(SAMPLE_INTAKE, "Demo summary text", "structured", ["demographics"])
    print(f"   Session summary: {session.get_summary()}")
    print()

    print("📝 Note: The following functions require Ollama to be running:")
    print("   • summarize_intake(intake_text)")
    print("   • extract_medical_history(intake_text)")
    print("   • generate_pre_visit_summary(intake_data, appointment_type)")
    print("   • identify_risk_factors(intake_text)")
    print("   • flag_missing_info(intake_text)")
    print()
    print("✅ Demo complete! See README.md for more examples.")


if __name__ == "__main__":
    main()
