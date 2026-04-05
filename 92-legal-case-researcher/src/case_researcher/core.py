"""Core engine for Legal Case Researcher.

Provides AI-powered legal research capabilities using local LLMs.
All processing stays on-device — no data leaves the machine.
"""

import json
import re
import sys
import os
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from common.llm_client import chat, check_ollama_running

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

LEGAL_DISCLAIMER = (
    "⚠️  LEGAL DISCLAIMER: This tool is for research assistance only. "
    "It does NOT provide legal advice. All results should be verified by a "
    "qualified attorney. AI-generated analysis may contain inaccuracies. "
    "Always consult primary legal sources and confirm citations independently."
)

SYSTEM_PROMPT = (
    "You are an expert legal research assistant with deep knowledge of case law, "
    "statutes, and legal precedents across multiple jurisdictions. You help "
    "attorneys and legal professionals find relevant cases, analyze legal "
    "arguments, and extract citations. Always respond with accurate, well-structured "
    "information. When citing cases, use proper legal citation format (Bluebook). "
    "If you are unsure about a specific case or citation, clearly indicate that "
    "the information should be verified against primary sources. "
    "Respond ONLY with valid JSON when asked for structured output."
)

# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class CaseReference:
    """Represents a legal case citation."""
    case_name: str = ""
    citation: str = ""
    year: str = ""
    court: str = ""
    jurisdiction: str = ""
    relevance: str = ""
    key_holding: str = ""

@dataclass
class LegalArgument:
    """Analysis of a legal argument's strength and structure."""
    argument_summary: str = ""
    strength: str = "moderate"  # strong, moderate, weak
    supporting_points: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)
    counter_arguments: List[str] = field(default_factory=list)
    suggested_improvements: List[str] = field(default_factory=list)
    relevant_doctrines: List[str] = field(default_factory=list)
    confidence_score: float = 0.0

@dataclass
class ResearchResult:
    """Result from a case law research query."""
    query: str = ""
    jurisdiction: str = ""
    summary: str = ""
    relevant_cases: List[CaseReference] = field(default_factory=list)
    key_legal_principles: List[str] = field(default_factory=list)
    suggested_search_terms: List[str] = field(default_factory=list)
    analysis: str = ""

@dataclass
class PrecedentAnalysis:
    """Analysis of a legal precedent's applicability."""
    case_name: str = ""
    citation: str = ""
    relevance_score: float = 0.0
    factual_similarity: str = ""
    legal_similarity: str = ""
    distinguishing_factors: List[str] = field(default_factory=list)
    applicable_holdings: List[str] = field(default_factory=list)
    recommendation: str = ""

# ---------------------------------------------------------------------------
# Sample scenarios
# ---------------------------------------------------------------------------

SAMPLE_SCENARIOS: Dict[str, Dict[str, str]] = {
    "contract_breach": {
        "title": "Breach of Contract – Material Breach Analysis",
        "query": "What constitutes a material breach of contract and what remedies are available?",
        "jurisdiction": "federal",
        "facts": "Client entered a services contract with a vendor who delivered 60% of agreed services but missed critical deadlines, causing financial losses.",
    },
    "employment_discrimination": {
        "title": "Employment Discrimination – Title VII Claim",
        "query": "What are the elements required to establish a prima facie case of employment discrimination under Title VII?",
        "jurisdiction": "federal",
        "facts": "Employee was passed over for promotion three times despite superior qualifications compared to selected candidates of a different protected class.",
    },
    "intellectual_property": {
        "title": "Patent Infringement – Software Patents",
        "query": "What is the current standard for software patent eligibility after Alice Corp v. CLS Bank?",
        "jurisdiction": "federal",
        "facts": "A startup has developed a novel algorithm for natural language processing and wants to patent it, but competitors claim it is abstract.",
    },
    "medical_malpractice": {
        "title": "Medical Malpractice – Standard of Care",
        "query": "How is the standard of care established in medical malpractice cases?",
        "jurisdiction": "state",
        "facts": "A patient suffered complications after surgery where the surgeon deviated from standard procedural guidelines without documented justification.",
    },
    "fourth_amendment": {
        "title": "Fourth Amendment – Digital Privacy",
        "query": "What protections does the Fourth Amendment provide for digital data and electronic communications?",
        "jurisdiction": "federal",
        "facts": "Law enforcement obtained cell phone location data from a service provider without a warrant to track a suspect's movements over 60 days.",
    },
}

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def get_strength_color(strength: str) -> str:
    """Return a Rich-compatible color string for argument strength."""
    colors = {
        "strong": "green",
        "moderate": "yellow",
        "weak": "red",
    }
    return colors.get(strength.lower(), "white")


def get_strength_emoji(strength: str) -> str:
    """Return an emoji indicator for argument strength."""
    emojis = {
        "strong": "💪",
        "moderate": "⚖️",
        "weak": "⚠️",
    }
    return emojis.get(strength.lower(), "❓")


def _parse_json_response(response: str) -> Dict[str, Any]:
    """Parse a JSON response from the LLM, handling markdown code fences."""
    text = response.strip()
    # Strip ```json ... ``` wrappers
    match = re.search(r"```(?:json)?\s*\n?(.*?)```", text, re.DOTALL)
    if match:
        text = match.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find the first { ... } block
        brace_match = re.search(r"\{.*\}", text, re.DOTALL)
        if brace_match:
            try:
                return json.loads(brace_match.group(0))
            except json.JSONDecodeError:
                pass
        return {"raw_response": response, "parse_error": True}

# ---------------------------------------------------------------------------
# Core research functions
# ---------------------------------------------------------------------------

def research_case_law(
    query: str,
    jurisdiction: str = "federal",
    model: str = "gemma4:latest",
) -> ResearchResult:
    """Research relevant case law for a given legal query.

    Args:
        query: The legal research question.
        jurisdiction: Target jurisdiction (federal, state, etc.).
        model: Ollama model name.

    Returns:
        ResearchResult with relevant cases and analysis.
    """
    prompt = f"""Research the following legal question and provide relevant case law.

Legal Question: {query}
Jurisdiction: {jurisdiction}

Respond with a JSON object in this exact format:
{{
    "summary": "Brief summary of the legal landscape on this issue",
    "relevant_cases": [
        {{
            "case_name": "Full case name",
            "citation": "Legal citation (Bluebook format)",
            "year": "Year decided",
            "court": "Court name",
            "jurisdiction": "Jurisdiction",
            "relevance": "Why this case is relevant",
            "key_holding": "The key holding of the case"
        }}
    ],
    "key_legal_principles": ["Principle 1", "Principle 2"],
    "suggested_search_terms": ["Term 1", "Term 2"],
    "analysis": "Detailed analysis of how these cases apply"
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=0.3, max_tokens=4096)
    data = _parse_json_response(response)

    result = ResearchResult(query=query, jurisdiction=jurisdiction)
    if "parse_error" in data:
        result.summary = response
        return result

    result.summary = data.get("summary", "")
    result.analysis = data.get("analysis", "")
    result.key_legal_principles = data.get("key_legal_principles", [])
    result.suggested_search_terms = data.get("suggested_search_terms", [])

    for case_data in data.get("relevant_cases", []):
        result.relevant_cases.append(CaseReference(**{
            k: case_data.get(k, "") for k in CaseReference.__dataclass_fields__
        }))

    return result


def find_precedents(
    case_facts: str,
    legal_issue: str,
    model: str = "gemma4:latest",
) -> List[PrecedentAnalysis]:
    """Find relevant legal precedents for given case facts and legal issues.

    Args:
        case_facts: Description of the case facts.
        legal_issue: The legal issue to research.
        model: Ollama model name.

    Returns:
        List of PrecedentAnalysis objects.
    """
    prompt = f"""Analyze the following case facts and legal issue, then identify relevant precedents.

Case Facts: {case_facts}
Legal Issue: {legal_issue}

Respond with a JSON object in this exact format:
{{
    "precedents": [
        {{
            "case_name": "Full case name",
            "citation": "Legal citation",
            "relevance_score": 0.85,
            "factual_similarity": "How the facts are similar",
            "legal_similarity": "How the legal issues align",
            "distinguishing_factors": ["Factor 1", "Factor 2"],
            "applicable_holdings": ["Holding 1", "Holding 2"],
            "recommendation": "How to use this precedent"
        }}
    ]
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=0.3, max_tokens=4096)
    data = _parse_json_response(response)

    precedents: List[PrecedentAnalysis] = []
    if "parse_error" in data:
        return precedents

    for p in data.get("precedents", []):
        precedents.append(PrecedentAnalysis(
            case_name=p.get("case_name", ""),
            citation=p.get("citation", ""),
            relevance_score=float(p.get("relevance_score", 0.0)),
            factual_similarity=p.get("factual_similarity", ""),
            legal_similarity=p.get("legal_similarity", ""),
            distinguishing_factors=p.get("distinguishing_factors", []),
            applicable_holdings=p.get("applicable_holdings", []),
            recommendation=p.get("recommendation", ""),
        ))

    return precedents


def analyze_legal_argument(
    argument: str,
    model: str = "gemma4:latest",
) -> LegalArgument:
    """Analyze the strength and structure of a legal argument.

    Args:
        argument: The legal argument text to analyze.
        model: Ollama model name.

    Returns:
        LegalArgument with strength assessment and details.
    """
    prompt = f"""Analyze the following legal argument for strength, weaknesses, and potential improvements.

Legal Argument: {argument}

Respond with a JSON object in this exact format:
{{
    "argument_summary": "Brief summary of the argument",
    "strength": "strong|moderate|weak",
    "supporting_points": ["Point 1", "Point 2"],
    "weaknesses": ["Weakness 1", "Weakness 2"],
    "counter_arguments": ["Counter 1", "Counter 2"],
    "suggested_improvements": ["Improvement 1", "Improvement 2"],
    "relevant_doctrines": ["Doctrine 1", "Doctrine 2"],
    "confidence_score": 0.75
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=0.3, max_tokens=4096)
    data = _parse_json_response(response)

    if "parse_error" in data:
        return LegalArgument(argument_summary=response)

    return LegalArgument(
        argument_summary=data.get("argument_summary", ""),
        strength=data.get("strength", "moderate"),
        supporting_points=data.get("supporting_points", []),
        weaknesses=data.get("weaknesses", []),
        counter_arguments=data.get("counter_arguments", []),
        suggested_improvements=data.get("suggested_improvements", []),
        relevant_doctrines=data.get("relevant_doctrines", []),
        confidence_score=float(data.get("confidence_score", 0.0)),
    )


def extract_citations(
    text: str,
    model: str = "gemma4:latest",
) -> List[CaseReference]:
    """Extract legal case citations from a block of text.

    Args:
        text: Text containing legal citations.
        model: Ollama model name.

    Returns:
        List of CaseReference objects found in the text.
    """
    prompt = f"""Extract all legal case citations from the following text.

Text: {text}

Respond with a JSON object in this exact format:
{{
    "citations": [
        {{
            "case_name": "Full case name",
            "citation": "Legal citation",
            "year": "Year",
            "court": "Court",
            "jurisdiction": "Jurisdiction",
            "relevance": "Context in which the case was cited",
            "key_holding": "Key holding if determinable"
        }}
    ]
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=0.2, max_tokens=4096)
    data = _parse_json_response(response)

    citations: List[CaseReference] = []
    if "parse_error" in data:
        return citations

    for c in data.get("citations", []):
        citations.append(CaseReference(**{
            k: c.get(k, "") for k in CaseReference.__dataclass_fields__
        }))

    return citations


def summarize_case(
    case_text: str,
    model: str = "gemma4:latest",
) -> Dict[str, Any]:
    """Summarize a legal case document.

    Args:
        case_text: Full text or excerpt of a legal case.
        model: Ollama model name.

    Returns:
        Dictionary containing the structured case summary.
    """
    prompt = f"""Summarize the following legal case document, extracting key information.

Case Document:
{case_text}

Respond with a JSON object in this exact format:
{{
    "case_name": "Full case name",
    "citation": "Legal citation if available",
    "court": "Court that decided the case",
    "date_decided": "Date of decision",
    "judge": "Presiding judge or author of opinion",
    "parties": {{
        "plaintiff": "Plaintiff name",
        "defendant": "Defendant name"
    }},
    "procedural_history": "Brief procedural history",
    "facts": "Key facts of the case",
    "issues": ["Legal issue 1", "Legal issue 2"],
    "holding": "The court's holding",
    "reasoning": "The court's reasoning",
    "rule_of_law": "The legal rule established or applied",
    "significance": "Why this case is significant",
    "key_quotes": ["Notable quote 1", "Notable quote 2"],
    "dissent_summary": "Summary of any dissenting opinion, or null"
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = chat(messages, model=model, system_prompt=SYSTEM_PROMPT, temperature=0.2, max_tokens=4096)
    data = _parse_json_response(response)

    if "parse_error" in data:
        return {"summary": response, "parse_error": True}

    return data
