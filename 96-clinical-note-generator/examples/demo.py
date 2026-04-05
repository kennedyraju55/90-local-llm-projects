"""
Demo script for Clinical Note Generator.
Shows how to use the core module programmatically.

Usage:
    python examples/demo.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.clinical_note_generator.core import (
    load_config,
    generate_soap_note,
    generate_note_section,
    NOTE_TEMPLATES,
    SPECIALTY_PROMPTS,
    NoteSession,
    display_disclaimer,
)


def main():
    """Run a quick demo of Clinical Note Generator."""
    print("=" * 60)
    print("🏥 Clinical Note Generator - Demo")
    print("=" * 60)
    print()

    display_disclaimer()

    print("\n📋 Available Note Templates:")
    for key, desc in NOTE_TEMPLATES.items():
        print(f"   • {key}: {desc}")

    print("\n🏥 Available Specialties:")
    for key in SPECIALTY_PROMPTS:
        print(f"   • {key.replace('_', ' ').title()}")

    print("\n📝 Example: Generating a SOAP note...")
    print("   (Requires Ollama running with gemma4 model)")

    encounter = (
        "55-year-old male presents with 3-day history of progressive chest pain, "
        "worse with deep inspiration. Reports mild shortness of breath on exertion. "
        "No fever, chills, or cough. PMH: HTN, DM2, hyperlipidemia. "
        "Vitals: BP 145/90, HR 88, RR 18, Temp 98.6F, SpO2 96% on RA."
    )
    print(f"\n   Encounter: {encounter[:80]}...")

    try:
        note = generate_soap_note(encounter, note_type="general", specialty="internal_medicine")
        print(f"\n   Generated Note Preview:\n   {note[:200]}...")
    except Exception as e:
        print(f"\n   ⚠️ Could not generate (Ollama may not be running): {e}")

    print("\n✅ Demo complete!")


if __name__ == "__main__":
    main()
