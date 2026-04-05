#!/usr/bin/env python3
"""Demo script for Court Filing Generator.

Shows how to use the core API to generate court filings,
motions, and discovery requests programmatically.

Usage:
    python examples/demo.py

Note: Requires Ollama running with Gemma 4 model.
      Start with: ollama serve && ollama pull gemma4
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.filing_generator.core import (
    LEGAL_DISCLAIMER,
    CaseInfo,
    FilingType,
    FILING_TEMPLATES,
    SAMPLE_CASE_INFO,
    format_filing_header,
    generate_filing,
    generate_motion,
    generate_discovery_request,
    validate_filing,
)
from common.llm_client import check_ollama_running


def demo_filing_header() -> None:
    """Demo: Format a filing header."""
    print("=" * 60)
    print("DEMO 1: Format Filing Header")
    print("=" * 60)
    header = format_filing_header(SAMPLE_CASE_INFO)
    print(header)


def demo_list_templates() -> None:
    """Demo: List all available templates."""
    print("=" * 60)
    print("DEMO 2: Available Filing Templates")
    print("=" * 60)
    for ft, template in FILING_TEMPLATES.items():
        print(f"\n  📄 {template['title']}")
        print(f"     Type: {ft.value}")
        print(f"     Sections: {len(template['sections'])}")
        print(f"     Description: {template['description'][:80]}...")


def demo_generate_filing() -> None:
    """Demo: Generate a motion to dismiss."""
    print("\n" + "=" * 60)
    print("DEMO 3: Generate Motion to Dismiss")
    print("=" * 60)

    case_info = CaseInfo(
        case_number="2025-CV-05678",
        court="United States District Court for the Western District of Texas",
        parties={
            "plaintiff": "Alice Johnson",
            "defendant": "TechCorp LLC",
        },
        judge="Hon. Robert Chen",
        jurisdiction="federal",
    )

    result = generate_filing(
        filing_type=FilingType.MOTION_TO_DISMISS.value,
        case_info=case_info,
        facts="Plaintiff alleges breach of contract for software services. "
              "However, the contract contains a mandatory arbitration clause.",
        arguments="The complaint should be dismissed because: "
                  "1) The arbitration clause is enforceable under the FAA. "
                  "2) Plaintiff failed to exhaust the arbitration remedy. "
                  "3) The court lacks subject matter jurisdiction over arbitrable claims.",
    )

    print(f"\nTitle: {result.title}")
    print(f"Sections: {', '.join(result.sections)}")
    print(f"\n{result.content[:500]}...")

    if result.warnings:
        print("\n⚠️ Warnings:")
        for w in result.warnings:
            print(f"  - {w}")


def demo_generate_motion() -> None:
    """Demo: Generate a motion to compel discovery."""
    print("\n" + "=" * 60)
    print("DEMO 4: Generate Motion to Compel")
    print("=" * 60)

    result = generate_motion(
        motion_type="motion_to_compel",
        case_info=SAMPLE_CASE_INFO,
        grounds="Defendant has failed to respond to Plaintiff's First Set of "
                "Interrogatories within the 30-day period required by Rule 33. "
                "Despite good-faith meet-and-confer efforts, Defendant refuses "
                "to provide responses.",
    )

    print(f"\nTitle: {result.title}")
    print(f"\n{result.content[:500]}...")


def demo_generate_discovery() -> None:
    """Demo: Generate interrogatories."""
    print("\n" + "=" * 60)
    print("DEMO 5: Generate Interrogatories")
    print("=" * 60)

    result = generate_discovery_request(
        case_info=SAMPLE_CASE_INFO,
        discovery_type="interrogatories",
        items=[
            "Employment history and compensation",
            "Communications regarding the contract",
            "Documents related to performance metrics",
        ],
    )

    print(f"\nTitle: {result.title}")
    print(f"\n{result.content[:500]}...")


def main() -> None:
    """Run all demos."""
    print(LEGAL_DISCLAIMER)

    # Always run offline demos
    demo_filing_header()
    demo_list_templates()

    # Check if Ollama is available for LLM demos
    if not check_ollama_running():
        print("\n⚠️ Ollama is not running. Skipping LLM-dependent demos.")
        print("Start Ollama with: ollama serve && ollama pull gemma4")
        return

    print("\n✅ Ollama is running. Running LLM demos...\n")
    demo_generate_filing()
    demo_generate_motion()
    demo_generate_discovery()

    print("\n" + "=" * 60)
    print("✅ All demos completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
