"""
Core module for Legal Brief Writer.

Provides comprehensive legal brief and memoranda generation using local LLMs.
All processing happens locally - no data ever leaves the machine.
"""

import json
import logging
import sys
import os
from enum import Enum
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# Add project root to path for common imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from common.llm_client import chat, check_ollama_running

from .config import load_config

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

LEGAL_DISCLAIMER = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                              LEGAL DISCLAIMER                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  This tool generates legal documents using AI and is intended for          ║
║  DRAFTING ASSISTANCE ONLY. All output must be reviewed, verified, and      ║
║  approved by a licensed attorney before use in any legal proceeding.       ║
║                                                                            ║
║  This tool does NOT constitute legal advice. The developers assume no      ║
║  liability for the accuracy, completeness, or applicability of any         ║
║  generated content. Use at your own risk.                                  ║
║                                                                            ║
║  Attorney-client privilege: All data is processed 100% locally using       ║
║  Ollama. No data is transmitted to external servers.                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

SYSTEM_PROMPT = """You are an expert legal writing assistant specializing in drafting 
legal briefs, memoranda, and legal analyses. You produce clear, precise, and 
professionally formatted legal documents.

Follow these principles:
1. Use formal legal writing style with proper citations format (Bluebook).
2. Structure arguments logically with clear headings and subheadings.
3. Apply IRAC method (Issue, Rule, Application, Conclusion) where appropriate.
4. Include relevant legal standards and burdens of proof.
5. Use persuasive but professional language.
6. Cite cases in proper format: Party v. Party, Volume Reporter Page (Court Year).
7. Include procedural history where relevant.
8. Address counterarguments proactively.
9. Maintain objectivity in memoranda and persuasion in briefs.
10. Always respond with valid JSON when requested."""


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class BriefType(str, Enum):
    """Types of legal briefs and memoranda."""
    TRIAL_BRIEF = "trial_brief"
    APPELLATE_BRIEF = "appellate_brief"
    AMICUS_BRIEF = "amicus_brief"
    MEMORANDUM_OF_LAW = "memorandum_of_law"
    MEMORANDUM_IN_SUPPORT = "memorandum_in_support"
    MEMORANDUM_IN_OPPOSITION = "memorandum_in_opposition"
    REPLY_BRIEF = "reply_brief"
    LEGAL_MEMORANDUM = "legal_memorandum"
    CASE_SUMMARY = "case_summary"


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class BriefSection:
    """A section of a legal brief."""
    title: str
    content: str
    order: int


@dataclass
class LegalIssue:
    """An IRAC-structured legal issue analysis."""
    issue: str
    rule: str
    analysis: str
    conclusion: str


@dataclass
class CaseDetails:
    """Details about the case for which the brief is being written."""
    case_name: str
    case_number: str = ""
    court: str = ""
    jurisdiction: str = ""
    client_position: str = ""
    opposing_party: str = ""


@dataclass
class BriefResult:
    """Result of a brief generation."""
    brief_type: str
    title: str
    sections: List[BriefSection] = field(default_factory=list)
    legal_issues: List[LegalIssue] = field(default_factory=list)
    word_count: int = 0
    warnings: List[str] = field(default_factory=list)
    table_of_authorities: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Brief Templates
# ---------------------------------------------------------------------------

BRIEF_TEMPLATES = {
    BriefType.TRIAL_BRIEF: {
        "sections": [
            "Caption and Title",
            "Table of Contents",
            "Table of Authorities",
            "Preliminary Statement",
            "Statement of Facts",
            "Legal Standard",
            "Argument",
            "Conclusion",
            "Certificate of Service",
        ],
        "description": "A brief filed with the trial court to persuade the judge on legal issues.",
    },
    BriefType.APPELLATE_BRIEF: {
        "sections": [
            "Cover Page",
            "Table of Contents",
            "Table of Authorities",
            "Statement of Jurisdiction",
            "Statement of Issues",
            "Statement of the Case",
            "Statement of Facts",
            "Summary of Argument",
            "Argument",
            "Conclusion",
            "Certificate of Compliance",
        ],
        "description": "A brief filed with an appellate court challenging or defending a lower court decision.",
    },
    BriefType.AMICUS_BRIEF: {
        "sections": [
            "Cover Page",
            "Table of Contents",
            "Table of Authorities",
            "Interest of Amicus Curiae",
            "Summary of Argument",
            "Argument",
            "Conclusion",
        ],
        "description": "A brief filed by a non-party (friend of the court) to provide additional perspective.",
    },
    BriefType.MEMORANDUM_OF_LAW: {
        "sections": [
            "Caption",
            "Preliminary Statement",
            "Statement of Facts",
            "Legal Standard",
            "Argument",
            "Conclusion",
        ],
        "description": "A document presenting legal arguments to a court on a specific motion.",
    },
    BriefType.MEMORANDUM_IN_SUPPORT: {
        "sections": [
            "Caption",
            "Introduction",
            "Statement of Facts",
            "Legal Standard",
            "Argument in Support",
            "Conclusion and Relief Requested",
        ],
        "description": "A memorandum supporting a specific motion filed with the court.",
    },
    BriefType.MEMORANDUM_IN_OPPOSITION: {
        "sections": [
            "Caption",
            "Introduction",
            "Counter-Statement of Facts",
            "Legal Standard",
            "Argument in Opposition",
            "Conclusion",
        ],
        "description": "A memorandum opposing a motion filed by the opposing party.",
    },
    BriefType.REPLY_BRIEF: {
        "sections": [
            "Caption",
            "Introduction",
            "Reply to Opposing Arguments",
            "Additional Authorities",
            "Conclusion",
        ],
        "description": "A reply brief responding to the opposition's arguments.",
    },
    BriefType.LEGAL_MEMORANDUM: {
        "sections": [
            "Heading",
            "Question Presented",
            "Brief Answer",
            "Statement of Facts",
            "Discussion",
            "Conclusion",
        ],
        "description": "An objective internal memo analyzing legal issues for a supervising attorney.",
    },
    BriefType.CASE_SUMMARY: {
        "sections": [
            "Case Information",
            "Procedural History",
            "Facts",
            "Issues",
            "Holding",
            "Reasoning",
            "Significance",
        ],
        "description": "A concise summary of a court case's key elements.",
    },
}

# Sample case details for testing/demo
SAMPLE_CASE_DETAILS = CaseDetails(
    case_name="Smith v. Acme Corporation",
    case_number="2024-CV-01234",
    court="United States District Court for the Western District of Texas",
    jurisdiction="Federal",
    client_position="Plaintiff",
    opposing_party="Acme Corporation",
)


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def _parse_json_response(response: str) -> Dict[str, Any]:
    """Parse a JSON response from the LLM, handling markdown code blocks.

    Args:
        response: Raw LLM response text that may contain JSON.

    Returns:
        Parsed dictionary from the JSON response.
    """
    text = response.strip()

    # Remove markdown code fences
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    # Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try to find JSON object in the text
    start = text.find("{")
    end = text.rfind("}") + 1
    if start != -1 and end > start:
        try:
            return json.loads(text[start:end])
        except json.JSONDecodeError:
            pass

    # Try to find JSON array
    start = text.find("[")
    end = text.rfind("]") + 1
    if start != -1 and end > start:
        try:
            return {"items": json.loads(text[start:end])}
        except json.JSONDecodeError:
            pass

    logger.warning("Failed to parse JSON response, returning raw text")
    return {"raw_text": text}


def _build_case_context(case_details: CaseDetails) -> str:
    """Build a context string from case details."""
    parts = [f"Case: {case_details.case_name}"]
    if case_details.case_number:
        parts.append(f"Case Number: {case_details.case_number}")
    if case_details.court:
        parts.append(f"Court: {case_details.court}")
    if case_details.jurisdiction:
        parts.append(f"Jurisdiction: {case_details.jurisdiction}")
    if case_details.client_position:
        parts.append(f"Client Position: {case_details.client_position}")
    if case_details.opposing_party:
        parts.append(f"Opposing Party: {case_details.opposing_party}")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def write_brief(
    brief_type: str,
    case_details: CaseDetails,
    facts: str,
    issues: str,
    arguments: str,
    model: str = "gemma4:latest",
) -> BriefResult:
    """Write a complete legal brief.

    Args:
        brief_type: Type of brief (from BriefType enum values).
        case_details: Case information.
        facts: Statement of facts.
        issues: Legal issues to address.
        arguments: Key arguments to make.
        model: LLM model to use.

    Returns:
        BriefResult with the generated brief.
    """
    config = load_config()

    try:
        bt = BriefType(brief_type)
    except ValueError:
        bt = BriefType.MEMORANDUM_OF_LAW

    template = BRIEF_TEMPLATES.get(bt, BRIEF_TEMPLATES[BriefType.MEMORANDUM_OF_LAW])
    case_context = _build_case_context(case_details)
    sections_list = template["sections"]

    prompt = f"""Write a complete {bt.value.replace('_', ' ').title()} with the following details:

{case_context}

STATEMENT OF FACTS:
{facts}

LEGAL ISSUES:
{issues}

KEY ARGUMENTS:
{arguments}

The brief must include these sections: {', '.join(sections_list)}

Respond in JSON format:
{{
    "title": "Title of the brief",
    "sections": [
        {{"title": "Section Title", "content": "Full section content", "order": 1}}
    ],
    "legal_issues": [
        {{"issue": "Legal issue", "rule": "Applicable rule", "analysis": "Analysis", "conclusion": "Conclusion"}}
    ],
    "warnings": ["Any caveats or areas needing attorney review"],
    "table_of_authorities": ["Case citations used"]
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )

    data = _parse_json_response(response)

    sections = []
    for i, s in enumerate(data.get("sections", [])):
        sections.append(BriefSection(
            title=s.get("title", f"Section {i+1}"),
            content=s.get("content", ""),
            order=s.get("order", i + 1),
        ))

    legal_issues = []
    for li in data.get("legal_issues", []):
        legal_issues.append(LegalIssue(
            issue=li.get("issue", ""),
            rule=li.get("rule", ""),
            analysis=li.get("analysis", ""),
            conclusion=li.get("conclusion", ""),
        ))

    full_text = "\n\n".join(s.content for s in sections)
    word_count = len(full_text.split())

    return BriefResult(
        brief_type=bt.value,
        title=data.get("title", f"{bt.value.replace('_', ' ').title()} - {case_details.case_name}"),
        sections=sections,
        legal_issues=legal_issues,
        word_count=word_count,
        warnings=data.get("warnings", []),
        table_of_authorities=data.get("table_of_authorities", []),
    )


def write_memorandum(
    case_details: CaseDetails,
    question_presented: str,
    facts: str,
    model: str = "gemma4:latest",
) -> BriefResult:
    """Write a legal memorandum (objective internal memo).

    Args:
        case_details: Case information.
        question_presented: The legal question to analyze.
        facts: Relevant facts.
        model: LLM model to use.

    Returns:
        BriefResult with the generated memorandum.
    """
    config = load_config()
    case_context = _build_case_context(case_details)

    prompt = f"""Write an objective legal memorandum with the following details:

{case_context}

QUESTION PRESENTED:
{question_presented}

STATEMENT OF FACTS:
{facts}

Structure the memorandum with these sections:
1. Heading (To, From, Date, Re)
2. Question Presented
3. Brief Answer
4. Statement of Facts
5. Discussion (using IRAC method for each issue)
6. Conclusion

Respond in JSON format:
{{
    "title": "Memorandum Re: [subject]",
    "sections": [
        {{"title": "Section Title", "content": "Full section content", "order": 1}}
    ],
    "legal_issues": [
        {{"issue": "Legal issue", "rule": "Applicable rule", "analysis": "Analysis", "conclusion": "Conclusion"}}
    ],
    "warnings": ["Areas needing further research or attorney review"],
    "table_of_authorities": ["Case citations used"]
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )

    data = _parse_json_response(response)

    sections = []
    for i, s in enumerate(data.get("sections", [])):
        sections.append(BriefSection(
            title=s.get("title", f"Section {i+1}"),
            content=s.get("content", ""),
            order=s.get("order", i + 1),
        ))

    legal_issues = []
    for li in data.get("legal_issues", []):
        legal_issues.append(LegalIssue(
            issue=li.get("issue", ""),
            rule=li.get("rule", ""),
            analysis=li.get("analysis", ""),
            conclusion=li.get("conclusion", ""),
        ))

    full_text = "\n\n".join(s.content for s in sections)
    word_count = len(full_text.split())

    return BriefResult(
        brief_type=BriefType.LEGAL_MEMORANDUM.value,
        title=data.get("title", f"Memorandum Re: {case_details.case_name}"),
        sections=sections,
        legal_issues=legal_issues,
        word_count=word_count,
        warnings=data.get("warnings", []),
        table_of_authorities=data.get("table_of_authorities", []),
    )


def write_irac_analysis(
    issue: str,
    facts: str,
    model: str = "gemma4:latest",
) -> LegalIssue:
    """Perform an IRAC (Issue, Rule, Application, Conclusion) analysis.

    Args:
        issue: The legal issue to analyze.
        facts: Relevant facts.
        model: LLM model to use.

    Returns:
        LegalIssue with structured IRAC analysis.
    """
    config = load_config()

    prompt = f"""Perform a detailed IRAC analysis for the following:

LEGAL ISSUE:
{issue}

RELEVANT FACTS:
{facts}

Respond in JSON format:
{{
    "issue": "Clear statement of the legal issue",
    "rule": "Statement of the applicable legal rule(s) with citations",
    "analysis": "Detailed application of the rule to the facts",
    "conclusion": "Clear conclusion based on the analysis"
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )

    data = _parse_json_response(response)

    return LegalIssue(
        issue=data.get("issue", issue),
        rule=data.get("rule", ""),
        analysis=data.get("analysis", ""),
        conclusion=data.get("conclusion", ""),
    )


def generate_table_of_authorities(
    brief_text: str,
    model: str = "gemma4:latest",
) -> List[str]:
    """Generate a Table of Authorities from brief text.

    Args:
        brief_text: The full text of the brief.
        model: LLM model to use.

    Returns:
        List of cited authorities in proper format.
    """
    config = load_config()

    prompt = f"""Extract and format a Table of Authorities from the following legal text.
Categorize citations into: Cases, Statutes, Constitutional Provisions, 
Secondary Sources, and Other Authorities.

Format each citation in proper Bluebook format.

LEGAL TEXT:
{brief_text}

Respond in JSON format:
{{
    "authorities": [
        "Properly formatted citation 1",
        "Properly formatted citation 2"
    ]
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )

    data = _parse_json_response(response)
    return data.get("authorities", data.get("items", []))


def improve_legal_writing(
    text: str,
    model: str = "gemma4:latest",
) -> Dict[str, Any]:
    """Improve and edit legal writing for clarity, precision, and style.

    Args:
        text: Legal text to improve.
        model: LLM model to use.

    Returns:
        Dictionary with improved text, changes made, and suggestions.
    """
    config = load_config()

    prompt = f"""Review and improve the following legal writing. Focus on:
1. Clarity and precision of language
2. Proper legal terminology
3. Logical flow and organization
4. Elimination of ambiguity
5. Conciseness without losing substance
6. Proper citation format (Bluebook)
7. Grammar and style

ORIGINAL TEXT:
{text}

Respond in JSON format:
{{
    "improved_text": "The improved version of the text",
    "changes": [
        "Description of each change made"
    ],
    "suggestions": [
        "Additional suggestions for the author"
    ],
    "readability_score": "Assessment of readability (e.g., Good, Needs Work, Excellent)",
    "legal_accuracy_notes": "Notes on legal accuracy concerns"
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )

    data = _parse_json_response(response)
    return {
        "improved_text": data.get("improved_text", text),
        "changes": data.get("changes", []),
        "suggestions": data.get("suggestions", []),
        "readability_score": data.get("readability_score", "N/A"),
        "legal_accuracy_notes": data.get("legal_accuracy_notes", ""),
    }


# ---------------------------------------------------------------------------
# Display Helpers
# ---------------------------------------------------------------------------

def format_brief_text(result: BriefResult) -> str:
    """Format a BriefResult as plain text for display or export.

    Args:
        result: The BriefResult to format.

    Returns:
        Formatted plain text representation of the brief.
    """
    lines = []
    lines.append("=" * 78)
    lines.append(result.title.center(78))
    lines.append("=" * 78)
    lines.append("")

    sorted_sections = sorted(result.sections, key=lambda s: s.order)
    for section in sorted_sections:
        lines.append(f"{'─' * 78}")
        lines.append(f"  {section.title.upper()}")
        lines.append(f"{'─' * 78}")
        lines.append(section.content)
        lines.append("")

    if result.legal_issues:
        lines.append(f"{'═' * 78}")
        lines.append("  LEGAL ISSUES ANALYSIS")
        lines.append(f"{'═' * 78}")
        for i, issue in enumerate(result.legal_issues, 1):
            lines.append(f"\n  Issue {i}: {issue.issue}")
            lines.append(f"  Rule: {issue.rule}")
            lines.append(f"  Analysis: {issue.analysis}")
            lines.append(f"  Conclusion: {issue.conclusion}")
            lines.append("")

    if result.table_of_authorities:
        lines.append(f"{'═' * 78}")
        lines.append("  TABLE OF AUTHORITIES")
        lines.append(f"{'═' * 78}")
        for auth in result.table_of_authorities:
            lines.append(f"  • {auth}")
        lines.append("")

    if result.warnings:
        lines.append(f"{'═' * 78}")
        lines.append("  ⚠  WARNINGS / AREAS FOR ATTORNEY REVIEW")
        lines.append(f"{'═' * 78}")
        for w in result.warnings:
            lines.append(f"  ⚠ {w}")
        lines.append("")

    lines.append(f"{'═' * 78}")
    lines.append(f"  Word Count: {result.word_count}")
    lines.append(f"  Brief Type: {result.brief_type.replace('_', ' ').title()}")
    lines.append(f"{'═' * 78}")

    return "\n".join(lines)


def format_irac_text(issue: LegalIssue) -> str:
    """Format an IRAC analysis as plain text.

    Args:
        issue: The LegalIssue to format.

    Returns:
        Formatted IRAC analysis text.
    """
    lines = [
        "=" * 60,
        "  IRAC ANALYSIS",
        "=" * 60,
        "",
        "ISSUE:",
        f"  {issue.issue}",
        "",
        "RULE:",
        f"  {issue.rule}",
        "",
        "APPLICATION:",
        f"  {issue.analysis}",
        "",
        "CONCLUSION:",
        f"  {issue.conclusion}",
        "",
        "=" * 60,
    ]
    return "\n".join(lines)


def display_brief_types() -> str:
    """Return a formatted string listing all available brief types.

    Returns:
        Formatted string of brief types and descriptions.
    """
    lines = ["Available Brief Types:", "=" * 50]
    for bt in BriefType:
        template = BRIEF_TEMPLATES.get(bt, {})
        desc = template.get("description", "No description available")
        lines.append(f"\n  {bt.value}")
        lines.append(f"  {desc}")
        sections = template.get("sections", [])
        if sections:
            lines.append(f"  Sections: {', '.join(sections)}")
    return "\n".join(lines)
