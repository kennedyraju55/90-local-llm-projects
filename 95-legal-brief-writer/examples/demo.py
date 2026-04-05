#!/usr/bin/env python3
"""Demo script for Legal Brief Writer."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.brief_writer.core import (
    BriefType,
    CaseDetails,
    LEGAL_DISCLAIMER,
    BRIEF_TEMPLATES,
    SAMPLE_CASE_DETAILS,
    write_brief,
    write_memorandum,
    write_irac_analysis,
    improve_legal_writing,
    format_brief_text,
    format_irac_text,
    display_brief_types,
)
from common.llm_client import check_ollama_running


def main():
    """Run Legal Brief Writer demo."""
    print("=" * 70)
    print("  ⚖️  Legal Brief Writer — Demo")
    print("=" * 70)

    # Check Ollama
    if not check_ollama_running():
        print("\n❌ Ollama is not running. Start it with: ollama serve")
        print("   Then run: ollama pull gemma4:latest")
        sys.exit(1)

    print("\n✅ Ollama is running\n")

    # Show disclaimer
    print(LEGAL_DISCLAIMER)

    # Display available brief types
    print(display_brief_types())

    # --- Demo 1: Write a Memorandum of Law ---
    print("\n" + "=" * 70)
    print("  Demo 1: Writing a Memorandum of Law")
    print("=" * 70)

    case_details = CaseDetails(
        case_name="Johnson v. Metro Transit Authority",
        case_number="2024-CV-05678",
        court="United States District Court for the Southern District of New York",
        jurisdiction="Federal",
        client_position="Plaintiff",
        opposing_party="Metro Transit Authority",
    )

    facts = """On March 15, 2024, the plaintiff, Sarah Johnson, was a passenger on 
    a Metro Transit Authority bus (Route 42). The bus driver, while operating the vehicle, 
    was observed by multiple witnesses using a personal cell phone. The bus driver failed 
    to stop at a marked stop sign at the intersection of 5th Avenue and Main Street, 
    causing a collision with a sedan. The plaintiff sustained a fractured wrist, 
    cervical strain, and emotional distress. The plaintiff incurred $45,000 in medical 
    expenses and lost 8 weeks of wages ($12,000). The defendant's employee handbook 
    explicitly prohibits cell phone use while operating transit vehicles."""

    issues = """1. Whether the bus driver's cell phone use while operating a transit vehicle 
    constitutes negligence per se.
    2. Whether the Metro Transit Authority is vicariously liable for the driver's negligent acts 
    under the doctrine of respondeat superior.
    3. Whether the plaintiff is entitled to damages for emotional distress in addition to 
    physical injuries."""

    arguments = """1. The bus driver violated the explicit company policy prohibiting cell phone 
    use, which establishes the standard of care. The violation of this policy, combined with 
    running a stop sign, constitutes negligence per se.
    2. The driver was acting within the scope of employment at the time of the incident, 
    making the MTA vicariously liable under respondeat superior.
    3. The plaintiff's emotional distress arises directly from the physical impact and injuries, 
    satisfying the physical manifestation requirement."""

    print("\nGenerating memorandum of law...")
    result = write_brief(
        brief_type="memorandum_of_law",
        case_details=case_details,
        facts=facts,
        issues=issues,
        arguments=arguments,
    )
    print(format_brief_text(result))

    # --- Demo 2: IRAC Analysis ---
    print("\n" + "=" * 70)
    print("  Demo 2: IRAC Analysis")
    print("=" * 70)

    issue = "Whether an employer is vicariously liable for an employee's negligent acts committed during the scope of employment."
    irac_facts = """A delivery driver employed by FastShip Inc. caused a traffic accident 
    while making deliveries on their assigned route. The driver was texting while driving, 
    which violates both state law and company policy. The accident resulted in property 
    damage and personal injuries to the other driver."""

    print("\nPerforming IRAC analysis...")
    irac_result = write_irac_analysis(issue=issue, facts=irac_facts)
    print(format_irac_text(irac_result))

    # --- Demo 3: Improve Legal Writing ---
    print("\n" + "=" * 70)
    print("  Demo 3: Improve Legal Writing")
    print("=" * 70)

    text_to_improve = """The defendant was negligent because they didn't do what they were 
    supposed to do. The plaintiff got hurt real bad and needs money for their injuries. 
    The law says that when someone is careless and someone else gets hurt, the careless 
    person has to pay. This is pretty clear from the facts of the case."""

    print("\nImproving legal writing...")
    improved = improve_legal_writing(text=text_to_improve)
    print(f"\nImproved Text:\n{improved['improved_text']}")
    print(f"\nChanges Made:")
    for change in improved.get("changes", []):
        print(f"  • {change}")
    print(f"\nReadability: {improved.get('readability_score', 'N/A')}")

    print("\n" + "=" * 70)
    print("  ✅ Demo Complete!")
    print("  All processing was done 100% locally — no data left your machine.")
    print("=" * 70)


if __name__ == "__main__":
    main()
