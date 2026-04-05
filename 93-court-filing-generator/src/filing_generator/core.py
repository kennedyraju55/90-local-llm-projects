"""Core module for Court Filing Generator.

Provides functions for generating court filings, motions, discovery requests,
and validating legal documents using a local LLM (Gemma 4 via Ollama).
All processing is 100% local - no data ever leaves the machine.
"""

import json
import logging
import sys
import os
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

# Add project root to path for common imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from common.llm_client import chat

logger = logging.getLogger(__name__)

# ─── Constants ──────────────────────────────────────────────────────────────────

LEGAL_DISCLAIMER = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                            LEGAL DISCLAIMER                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ This tool generates DRAFT legal documents using AI. All output is for      ║
║ informational and drafting assistance purposes ONLY.                       ║
║                                                                            ║
║ • Documents MUST be reviewed by a licensed attorney before filing          ║
║ • AI-generated content may contain errors or omissions                     ║
║ • Local rules and jurisdiction-specific requirements must be verified      ║
║ • This tool does NOT constitute legal advice                               ║
║ • The user assumes all responsibility for filed documents                  ║
║                                                                            ║
║ All processing occurs locally on your machine. No data is transmitted      ║
║ to external servers. Attorney-client privilege is preserved.               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

SYSTEM_PROMPT = """You are an expert legal document generation assistant. You help 
attorneys draft court filings, motions, and legal documents with precision and 
adherence to proper legal formatting standards.

Your responsibilities:
1. Generate properly formatted legal documents following court rules
2. Use precise legal terminology and citations
3. Structure documents with appropriate sections and headings
4. Include all required components (caption, body, signature block, certificate of service)
5. Follow Federal Rules of Civil Procedure and local court rules
6. Maintain professional tone appropriate for court submissions

Important guidelines:
- Always include a case caption with proper formatting
- Use numbered paragraphs in the body of filings
- Include appropriate legal citations
- Add a signature block and certificate of service
- Note any jurisdiction-specific requirements
- Flag any areas that need attorney review

You output well-structured JSON when asked for structured responses."""


# ─── Enums ──────────────────────────────────────────────────────────────────────

class FilingType(str, Enum):
    """Supported court filing types."""
    MOTION_TO_DISMISS = "motion_to_dismiss"
    MOTION_FOR_SUMMARY_JUDGMENT = "motion_for_summary_judgment"
    COMPLAINT = "complaint"
    ANSWER = "answer"
    MOTION_TO_COMPEL = "motion_to_compel"
    MOTION_IN_LIMINE = "motion_in_limine"
    SUBPOENA = "subpoena"
    DISCOVERY_REQUEST = "discovery_request"
    APPELLATE_BRIEF = "appellate_brief"
    STIPULATION = "stipulation"


# ─── Dataclasses ────────────────────────────────────────────────────────────────

@dataclass
class CaseInfo:
    """Information about a legal case."""
    case_number: str
    court: str
    parties: Dict[str, str]  # e.g., {"plaintiff": "Smith", "defendant": "Jones"}
    judge: str = ""
    jurisdiction: str = "federal"
    date_filed: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))


@dataclass
class FilingResult:
    """Result of a filing generation."""
    filing_type: str
    title: str
    content: str
    sections: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


# ─── Filing Templates ──────────────────────────────────────────────────────────

FILING_TEMPLATES: Dict[str, Dict[str, Any]] = {
    FilingType.MOTION_TO_DISMISS: {
        "title": "Motion to Dismiss",
        "sections": [
            "Caption",
            "Introduction",
            "Statement of Facts",
            "Legal Standard",
            "Argument",
            "Conclusion",
            "Prayer for Relief",
            "Signature Block",
            "Certificate of Service",
        ],
        "description": "A motion requesting the court to dismiss the case for failure to state a claim or other grounds under Rule 12(b).",
    },
    FilingType.MOTION_FOR_SUMMARY_JUDGMENT: {
        "title": "Motion for Summary Judgment",
        "sections": [
            "Caption",
            "Introduction",
            "Statement of Undisputed Material Facts",
            "Legal Standard",
            "Argument",
            "Conclusion",
            "Prayer for Relief",
            "Signature Block",
            "Certificate of Service",
        ],
        "description": "A motion arguing there are no genuine disputes of material fact and the movant is entitled to judgment as a matter of law under Rule 56.",
    },
    FilingType.COMPLAINT: {
        "title": "Complaint",
        "sections": [
            "Caption",
            "Parties",
            "Jurisdiction and Venue",
            "Factual Allegations",
            "Causes of Action",
            "Prayer for Relief",
            "Jury Demand",
            "Signature Block",
        ],
        "description": "The initial pleading that sets forth the plaintiff's claims against the defendant.",
    },
    FilingType.ANSWER: {
        "title": "Answer",
        "sections": [
            "Caption",
            "Introduction",
            "Responses to Allegations",
            "Affirmative Defenses",
            "Counterclaims",
            "Prayer for Relief",
            "Signature Block",
            "Certificate of Service",
        ],
        "description": "The defendant's response to the complaint, admitting or denying each allegation.",
    },
    FilingType.MOTION_TO_COMPEL: {
        "title": "Motion to Compel Discovery",
        "sections": [
            "Caption",
            "Introduction",
            "Background",
            "Discovery Requests at Issue",
            "Meet and Confer Statement",
            "Legal Standard",
            "Argument",
            "Prayer for Relief",
            "Signature Block",
            "Certificate of Service",
        ],
        "description": "A motion requesting the court to compel the opposing party to respond to discovery requests.",
    },
    FilingType.MOTION_IN_LIMINE: {
        "title": "Motion in Limine",
        "sections": [
            "Caption",
            "Introduction",
            "Statement of Facts",
            "Legal Standard",
            "Argument",
            "Conclusion",
            "Prayer for Relief",
            "Signature Block",
            "Certificate of Service",
        ],
        "description": "A pretrial motion to exclude or include certain evidence at trial.",
    },
    FilingType.SUBPOENA: {
        "title": "Subpoena",
        "sections": [
            "Caption",
            "Command",
            "Documents/Testimony Required",
            "Date, Time, and Location",
            "Fees and Mileage",
            "Signature Block",
        ],
        "description": "A court order compelling a witness to testify or produce documents.",
    },
    FilingType.DISCOVERY_REQUEST: {
        "title": "Discovery Request",
        "sections": [
            "Caption",
            "Definitions",
            "Instructions",
            "Interrogatories / Requests for Production / Requests for Admission",
            "Signature Block",
            "Certificate of Service",
        ],
        "description": "Formal discovery requests including interrogatories, requests for production, or requests for admission.",
    },
    FilingType.APPELLATE_BRIEF: {
        "title": "Appellate Brief",
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
            "Certificate of Service",
        ],
        "description": "A written legal argument submitted to an appellate court.",
    },
    FilingType.STIPULATION: {
        "title": "Stipulation",
        "sections": [
            "Caption",
            "Recitals",
            "Stipulated Facts / Agreements",
            "Terms and Conditions",
            "Signature Blocks (All Parties)",
        ],
        "description": "An agreement between parties on certain facts or procedures.",
    },
}

# Sample case info for testing / demo purposes
SAMPLE_CASE_INFO = CaseInfo(
    case_number="2025-CV-01234",
    court="United States District Court for the Western District of Texas",
    parties={
        "plaintiff": "Jane Doe",
        "defendant": "Acme Corporation",
    },
    judge="Hon. Maria Rodriguez",
    jurisdiction="federal",
    date_filed="2025-01-15",
)


# ─── Helper Functions ───────────────────────────────────────────────────────────

def _parse_json_response(response: str) -> Dict[str, Any]:
    """Parse a JSON response from the LLM, handling markdown code fences.

    Args:
        response: Raw LLM response text, possibly wrapped in ```json ... ```

    Returns:
        Parsed dictionary from the JSON content.

    Raises:
        json.JSONDecodeError: If the response cannot be parsed as JSON.
    """
    text = response.strip()

    # Strip markdown code fences
    if text.startswith("```"):
        lines = text.split("\n")
        # Remove first line (```json or ```)
        lines = lines[1:]
        # Remove last line if it's ```
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()

    # Try to find JSON object or array in the text
    for start_char, end_char in [("{", "}"), ("[", "]")]:
        start_idx = text.find(start_char)
        end_idx = text.rfind(end_char)
        if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
            candidate = text[start_idx : end_idx + 1]
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                continue

    # Last resort: try parsing the whole text
    return json.loads(text)


def format_filing_header(case_info: CaseInfo) -> str:
    """Format a standard court document header/caption.

    Args:
        case_info: Case information for the header.

    Returns:
        Formatted header string with court caption.
    """
    plaintiff = case_info.parties.get("plaintiff", "PLAINTIFF")
    defendant = case_info.parties.get("defendant", "DEFENDANT")

    separator = "=" * 60
    header = f"""{separator}
{case_info.court.upper()}
{separator}

{plaintiff.upper()},
                    Plaintiff,

        v.                              Case No. {case_info.case_number}

{defendant.upper()},
                    Defendant.

{separator}
"""
    if case_info.judge:
        header += f"Before: {case_info.judge}\n"
    header += f"Date Filed: {case_info.date_filed}\n"
    header += f"Jurisdiction: {case_info.jurisdiction.capitalize()}\n"
    header += separator + "\n"

    return header


# ─── Core Functions ─────────────────────────────────────────────────────────────

def generate_filing(
    filing_type: str,
    case_info: CaseInfo,
    facts: str,
    arguments: str,
    model: str = "gemma4:latest",
) -> FilingResult:
    """Generate a complete court filing document.

    Args:
        filing_type: Type of filing (use FilingType enum values).
        case_info: Case information.
        facts: Statement of relevant facts.
        arguments: Legal arguments to include.
        model: LLM model to use.

    Returns:
        FilingResult with the generated document.
    """
    # Resolve template
    try:
        ft = FilingType(filing_type)
    except ValueError:
        ft = None

    template = FILING_TEMPLATES.get(ft, {})
    template_title = template.get("title", filing_type.replace("_", " ").title())
    template_sections = template.get("sections", [])

    header = format_filing_header(case_info)

    prompt = f"""Generate a complete {template_title} for the following case.

Case Information:
- Case Number: {case_info.case_number}
- Court: {case_info.court}
- Plaintiff: {case_info.parties.get('plaintiff', 'N/A')}
- Defendant: {case_info.parties.get('defendant', 'N/A')}
- Judge: {case_info.judge}
- Jurisdiction: {case_info.jurisdiction}
- Date Filed: {case_info.date_filed}

Facts:
{facts}

Legal Arguments:
{arguments}

Required Sections: {', '.join(template_sections) if template_sections else 'Standard sections'}

Generate the complete document with proper legal formatting, numbered paragraphs,
appropriate citations, and all required sections. Include a signature block and 
certificate of service where appropriate.

Return your response as JSON with the following structure:
{{
    "title": "Document Title",
    "content": "Full document text with proper formatting",
    "sections": ["list", "of", "section", "names", "included"],
    "warnings": ["any warnings or areas needing attorney review"]
}}"""

    messages = [{"role": "user", "content": prompt}]
    logger.info("Generating %s for case %s", template_title, case_info.case_number)

    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=4096,
    )

    try:
        parsed = _parse_json_response(response)
        content = header + "\n" + parsed.get("content", response)
        return FilingResult(
            filing_type=filing_type,
            title=parsed.get("title", template_title),
            content=content,
            sections=parsed.get("sections", template_sections),
            warnings=parsed.get("warnings", [
                "This document was generated by AI and must be reviewed by a licensed attorney."
            ]),
        )
    except (json.JSONDecodeError, KeyError):
        logger.warning("Could not parse structured response, using raw text")
        return FilingResult(
            filing_type=filing_type,
            title=template_title,
            content=header + "\n" + response,
            sections=template_sections,
            warnings=[
                "This document was generated by AI and must be reviewed by a licensed attorney.",
                "Response could not be parsed as structured JSON; raw text is provided.",
            ],
        )


def generate_motion(
    motion_type: str,
    case_info: CaseInfo,
    grounds: str,
    model: str = "gemma4:latest",
) -> FilingResult:
    """Generate a legal motion document.

    Args:
        motion_type: Type of motion (e.g., 'motion_to_dismiss').
        case_info: Case information.
        grounds: Legal grounds for the motion.
        model: LLM model to use.

    Returns:
        FilingResult with the generated motion.
    """
    header = format_filing_header(case_info)

    prompt = f"""Generate a complete {motion_type.replace('_', ' ').title()} for the following case.

Case Information:
- Case Number: {case_info.case_number}
- Court: {case_info.court}
- Plaintiff: {case_info.parties.get('plaintiff', 'N/A')}
- Defendant: {case_info.parties.get('defendant', 'N/A')}
- Judge: {case_info.judge}

Grounds for the Motion:
{grounds}

Generate the motion with:
1. Proper caption and title
2. Introduction stating the relief sought
3. Statement of relevant facts
4. Legal standard section
5. Argument section with numbered points and legal citations
6. Conclusion and prayer for relief
7. Signature block
8. Certificate of service

Return your response as JSON:
{{
    "title": "Motion Title",
    "content": "Full motion text",
    "sections": ["sections included"],
    "warnings": ["areas needing review"]
}}"""

    messages = [{"role": "user", "content": prompt}]
    logger.info("Generating motion: %s for case %s", motion_type, case_info.case_number)

    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=4096,
    )

    try:
        parsed = _parse_json_response(response)
        return FilingResult(
            filing_type=motion_type,
            title=parsed.get("title", motion_type.replace("_", " ").title()),
            content=header + "\n" + parsed.get("content", response),
            sections=parsed.get("sections", []),
            warnings=parsed.get("warnings", [
                "This motion was generated by AI and must be reviewed by a licensed attorney."
            ]),
        )
    except (json.JSONDecodeError, KeyError):
        return FilingResult(
            filing_type=motion_type,
            title=motion_type.replace("_", " ").title(),
            content=header + "\n" + response,
            sections=[],
            warnings=[
                "This motion was generated by AI and must be reviewed by a licensed attorney.",
                "Response could not be parsed as structured JSON.",
            ],
        )


def generate_discovery_request(
    case_info: CaseInfo,
    discovery_type: str,
    items: List[str],
    model: str = "gemma4:latest",
) -> FilingResult:
    """Generate discovery requests (interrogatories, RFPs, or RFAs).

    Args:
        case_info: Case information.
        discovery_type: Type of discovery ('interrogatories', 'rfp', 'rfa').
        items: List of topics or items to request.
        model: LLM model to use.

    Returns:
        FilingResult with the generated discovery request.
    """
    header = format_filing_header(case_info)
    items_text = "\n".join(f"  {i+1}. {item}" for i, item in enumerate(items))

    discovery_labels = {
        "interrogatories": "Interrogatories",
        "rfp": "Requests for Production of Documents",
        "rfa": "Requests for Admission",
    }
    label = discovery_labels.get(discovery_type.lower(), discovery_type.title())

    prompt = f"""Generate formal {label} for the following case.

Case Information:
- Case Number: {case_info.case_number}
- Court: {case_info.court}
- Plaintiff: {case_info.parties.get('plaintiff', 'N/A')}
- Defendant: {case_info.parties.get('defendant', 'N/A')}

Topics / Items to Request:
{items_text}

Generate the discovery document with:
1. Proper caption
2. Definitions section
3. Instructions section
4. Numbered discovery requests (at least one per topic listed)
5. Signature block
6. Certificate of service

Return your response as JSON:
{{
    "title": "{label}",
    "content": "Full discovery document text",
    "sections": ["sections included"],
    "warnings": ["areas needing review"]
}}"""

    messages = [{"role": "user", "content": prompt}]
    logger.info("Generating %s for case %s", label, case_info.case_number)

    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=4096,
    )

    try:
        parsed = _parse_json_response(response)
        return FilingResult(
            filing_type="discovery_request",
            title=parsed.get("title", label),
            content=header + "\n" + parsed.get("content", response),
            sections=parsed.get("sections", []),
            warnings=parsed.get("warnings", [
                "Discovery requests must be reviewed by a licensed attorney."
            ]),
        )
    except (json.JSONDecodeError, KeyError):
        return FilingResult(
            filing_type="discovery_request",
            title=label,
            content=header + "\n" + response,
            sections=[],
            warnings=[
                "Discovery requests must be reviewed by a licensed attorney.",
                "Response could not be parsed as structured JSON.",
            ],
        )


def validate_filing(
    filing_text: str,
    model: str = "gemma4:latest",
) -> Dict[str, Any]:
    """Validate a court filing for completeness and common issues.

    Args:
        filing_text: The full text of the filing to validate.
        model: LLM model to use.

    Returns:
        Dictionary with validation results including score, issues, and suggestions.
    """
    prompt = f"""Analyze the following court filing for completeness, formatting issues,
and potential problems. Check for:

1. Proper caption/header
2. Correct legal formatting (numbered paragraphs, proper citations)
3. Required sections (introduction, body, conclusion, signature block, certificate of service)
4. Legal terminology accuracy
5. Logical consistency of arguments
6. Any missing elements required by court rules

Filing Text:
---
{filing_text[:3000]}
---

Return your analysis as JSON:
{{
    "is_valid": true/false,
    "score": 0-100,
    "issues": ["list of identified issues"],
    "missing_sections": ["any missing required sections"],
    "suggestions": ["improvement suggestions"],
    "citation_check": "assessment of legal citations"
}}"""

    messages = [{"role": "user", "content": prompt}]
    logger.info("Validating filing document")

    response = chat(
        messages=messages,
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=2048,
    )

    try:
        result = _parse_json_response(response)
        # Ensure required keys exist
        result.setdefault("is_valid", False)
        result.setdefault("score", 0)
        result.setdefault("issues", [])
        result.setdefault("missing_sections", [])
        result.setdefault("suggestions", [])
        result.setdefault("citation_check", "Not assessed")
        return result
    except (json.JSONDecodeError, KeyError):
        return {
            "is_valid": False,
            "score": 0,
            "issues": ["Could not parse validation response from LLM"],
            "missing_sections": [],
            "suggestions": ["Re-run validation or manually review the document"],
            "citation_check": "Not assessed",
            "raw_response": response,
        }
