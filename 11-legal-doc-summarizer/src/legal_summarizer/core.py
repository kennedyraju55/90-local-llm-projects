"""Core business logic for Legal Document Summarizer."""

import logging
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from .config import load_config
from .utils import get_llm_client, truncate_text, read_document

logger = logging.getLogger(__name__)

LEGAL_SYSTEM_PROMPT = """You are an expert legal document analyst. Your task is to analyze legal documents
and extract structured information. Be precise, thorough, and use plain language to explain legal terms.

When analyzing a document, always extract and organize the following sections:

1. **Parties Involved** - List all parties mentioned with their roles (e.g., Buyer, Seller, Licensor).
2. **Key Clauses** - Summarize each major clause or section of the document.
3. **Obligations** - List obligations for each party, clearly stating who must do what.
4. **Important Dates** - Extract all dates including effective date, deadlines, renewal dates, expiration.
5. **Termination Conditions** - How and when can the agreement be terminated by either party.
6. **Penalties & Liabilities** - Any penalties, damages, indemnification, or liability limitations.

If a section has no relevant information in the document, state "Not specified in the document."
Use clear headings and organize the output logically."""

FORMAT_INSTRUCTIONS = {
    "bullet": "Format your response using bullet points for each section. Use markdown headings (##) for section titles.",
    "narrative": "Format your response as a flowing narrative summary, using paragraphs. Use markdown headings (##) for section titles.",
    "detailed": (
        "Format your response with maximum detail. Include direct quotes from the document where relevant. "
        "Use markdown headings (##) for section titles and sub-headings (###) for subsections. "
        "Add a risk assessment note at the end highlighting any concerning clauses."
    ),
}

CLAUSE_EXTRACTION_PROMPT = """Extract all distinct clauses from this legal document. For each clause, provide:
- Clause number/name
- Brief summary (1-2 sentences)
- Category (one of: Payment, Termination, Confidentiality, Liability, IP, Compliance, Other)
- Risk level (Low, Medium, High) with brief justification

Return as a structured list with clear separators between clauses.

Document:
{text}"""

RISK_SCORING_PROMPT = """Analyze this legal document for risk factors. Score each area from 0-10 (10 = highest risk):

1. Financial Risk - penalties, unlimited liability, payment terms
2. Termination Risk - lock-in, auto-renewal, difficult exit
3. IP Risk - ownership, licensing, assignment of rights
4. Compliance Risk - regulatory obligations, audit rights
5. Confidentiality Risk - scope of NDA, duration, penalties

For each area, provide the score and a brief justification.
Also provide an overall risk score (0-100) and top 3 risk concerns.

Document:
{text}"""

COMPARISON_PROMPT = """Compare the following {count} legal documents. For each, identify:
1. Document type and parties
2. Key differences in terms
3. Most favorable terms (and for which party)
4. Risk comparison

Documents:
{documents}

Provide a structured comparison table and summary."""


def summarize_document(text: str, output_format: str = "bullet", config: dict | None = None) -> str:
    """Send document text to the LLM for analysis and summarization.

    Args:
        text: The document text to analyze.
        output_format: One of 'bullet', 'narrative', or 'detailed'.
        config: Optional configuration dict.

    Returns:
        The LLM-generated summary string.
    """
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    format_instruction = FORMAT_INSTRUCTIONS.get(output_format, FORMAT_INSTRUCTIONS["bullet"])
    max_chars = cfg.get("processing", {}).get("max_document_chars", 12000)
    text = truncate_text(text, max_chars)

    messages = [
        {
            "role": "user",
            "content": (
                f"Analyze the following legal document and extract all key information.\n\n"
                f"{format_instruction}\n\n"
                f"--- DOCUMENT START ---\n{text}\n--- DOCUMENT END ---"
            ),
        }
    ]

    response = chat(
        messages=messages,
        system_prompt=LEGAL_SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )

    return response


def extract_clauses(text: str, config: dict | None = None) -> str:
    """Extract and categorize individual clauses from a legal document.

    Args:
        text: The document text.
        config: Optional configuration dict.

    Returns:
        Structured clause extraction from the LLM.
    """
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    max_chars = cfg.get("processing", {}).get("max_document_chars", 12000)
    text = truncate_text(text, max_chars)

    messages = [{"role": "user", "content": CLAUSE_EXTRACTION_PROMPT.format(text=text)}]

    return chat(
        messages=messages,
        system_prompt=LEGAL_SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )


def score_risks(text: str, config: dict | None = None) -> str:
    """Analyze document for risk factors and return risk scores.

    Args:
        text: The document text.
        config: Optional configuration dict.

    Returns:
        Risk analysis with scores from the LLM.
    """
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    max_chars = cfg.get("processing", {}).get("max_document_chars", 12000)
    text = truncate_text(text, max_chars)

    messages = [{"role": "user", "content": RISK_SCORING_PROMPT.format(text=text)}]

    return chat(
        messages=messages,
        system_prompt=LEGAL_SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )


def compare_documents(file_paths: list[str], config: dict | None = None) -> str:
    """Compare multiple legal documents side by side.

    Args:
        file_paths: List of paths to document files.
        config: Optional configuration dict.

    Returns:
        Comparison analysis from the LLM.
    """
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    documents_text = []
    for i, path in enumerate(file_paths, 1):
        text = read_document(path)
        max_chars = cfg.get("processing", {}).get("max_document_chars", 12000) // len(file_paths)
        text = truncate_text(text, max_chars)
        documents_text.append(f"--- DOCUMENT {i} ---\n{text}\n--- END DOCUMENT {i} ---")

    combined = "\n\n".join(documents_text)
    messages = [
        {
            "role": "user",
            "content": COMPARISON_PROMPT.format(count=len(file_paths), documents=combined),
        }
    ]

    return chat(
        messages=messages,
        system_prompt=LEGAL_SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )


def generate_export_markdown(summary: str, clauses: str | None = None,
                              risk_analysis: str | None = None, filepath: str = "") -> str:
    """Generate PDF-ready markdown export combining all analyses.

    Args:
        summary: The document summary.
        clauses: Optional clause extraction.
        risk_analysis: Optional risk analysis.
        filepath: Original file path for header.

    Returns:
        Complete markdown document ready for PDF conversion.
    """
    sections = [f"# Legal Document Analysis Report\n\n**Source:** {filepath}\n"]
    sections.append("## Document Summary\n\n" + summary)

    if clauses:
        sections.append("\n## Clause Extraction\n\n" + clauses)

    if risk_analysis:
        sections.append("\n## Risk Analysis\n\n" + risk_analysis)

    sections.append("\n---\n*Generated by Legal Document Summarizer*")
    return "\n".join(sections)
