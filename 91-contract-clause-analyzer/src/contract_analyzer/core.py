"""
Contract Clause Analyzer - Core logic for analyzing contract clauses.

⚖️ LEGAL DISCLAIMER: This tool provides AI-assisted contract analysis for 
informational purposes only. It is NOT legal advice. Always consult with a 
qualified attorney before making legal decisions based on contract analysis.

🔒 PRIVACY: All processing happens locally via Ollama. No data ever leaves your machine.
Attorney-client privilege is fully protected.
"""

import json
import logging
import os
import sys
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from common.llm_client import chat, generate, check_ollama_running

logger = logging.getLogger(__name__)

LEGAL_DISCLAIMER = (
    "⚖️ LEGAL DISCLAIMER\n\n"
    "This tool provides AI-assisted contract analysis for informational purposes only.\n"
    "It is NOT legal advice. Always consult with a qualified attorney before making\n"
    "legal decisions based on contract analysis.\n\n"
    "🔒 All processing happens locally. No data ever leaves your machine.\n"
    "Attorney-client privilege is fully protected."
)


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ClauseType(str, Enum):
    INDEMNIFICATION = "indemnification"
    LIMITATION_OF_LIABILITY = "limitation_of_liability"
    TERMINATION = "termination"
    CONFIDENTIALITY = "confidentiality"
    NON_COMPETE = "non_compete"
    INTELLECTUAL_PROPERTY = "intellectual_property"
    PAYMENT_TERMS = "payment_terms"
    WARRANTY = "warranty"
    FORCE_MAJEURE = "force_majeure"
    DISPUTE_RESOLUTION = "dispute_resolution"
    GOVERNING_LAW = "governing_law"
    ASSIGNMENT = "assignment"
    SEVERABILITY = "severability"
    AMENDMENT = "amendment"
    OTHER = "other"


@dataclass
class ClauseAnalysis:
    """Analysis result for a single contract clause."""
    clause_type: str
    risk_level: str
    summary: str
    obligations: List[str] = field(default_factory=list)
    deadlines: List[str] = field(default_factory=list)
    red_flags: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    key_terms: List[str] = field(default_factory=list)


@dataclass
class ContractAnalysis:
    """Complete contract analysis result."""
    title: str
    overall_risk: str
    clause_analyses: List[ClauseAnalysis] = field(default_factory=list)
    summary: str = ""
    total_clauses: int = 0
    high_risk_count: int = 0
    obligations_count: int = 0
    deadlines_count: int = 0
    red_flags_count: int = 0


SYSTEM_PROMPT = """You are an expert contract analyst AI assistant. Your role is to analyze contract clauses with precision and identify:

1. **Clause Type**: Categorize each clause (indemnification, termination, confidentiality, etc.)
2. **Risk Level**: Assess risk as LOW, MEDIUM, HIGH, or CRITICAL
3. **Obligations**: List all obligations and duties imposed
4. **Deadlines**: Extract all time-sensitive requirements
5. **Red Flags**: Identify problematic or unusual terms
6. **Recommendations**: Suggest improvements or negotiation points

IMPORTANT RULES:
- Be thorough and precise in your analysis
- Flag any one-sided or unusually broad terms
- Identify missing standard protections
- Note any ambiguous language that could be problematic
- Always specify which party bears each obligation
- You are NOT providing legal advice - only analytical assistance
- Format your response as structured JSON when asked"""


CLAUSE_ANALYSIS_PROMPT = """Analyze the following contract clause and provide a detailed assessment.

CONTRACT CLAUSE:
{clause_text}

Respond in the following JSON format:
{{
    "clause_type": "one of: indemnification, limitation_of_liability, termination, confidentiality, non_compete, intellectual_property, payment_terms, warranty, force_majeure, dispute_resolution, governing_law, assignment, severability, amendment, other",
    "risk_level": "one of: low, medium, high, critical",
    "summary": "brief summary of the clause",
    "obligations": ["list of obligations imposed"],
    "deadlines": ["list of deadlines or time-sensitive items"],
    "red_flags": ["list of concerning terms or provisions"],
    "recommendations": ["list of suggested improvements"],
    "key_terms": ["important defined terms used"]
}}

Provide ONLY the JSON response, no additional text."""


FULL_CONTRACT_PROMPT = """Analyze the following complete contract. Identify all major clauses and provide a comprehensive analysis.

CONTRACT TEXT:
{contract_text}

For each clause found, provide analysis in this JSON format:
{{
    "title": "contract title or type",
    "overall_risk": "low/medium/high/critical",
    "summary": "overall contract summary",
    "clauses": [
        {{
            "clause_type": "type",
            "risk_level": "level",
            "summary": "summary",
            "obligations": ["obligations"],
            "deadlines": ["deadlines"],
            "red_flags": ["red flags"],
            "recommendations": ["recommendations"],
            "key_terms": ["key terms"]
        }}
    ]
}}

Provide ONLY the JSON response, no additional text."""


RISK_COMPARISON_PROMPT = """Compare the following two contract clauses and identify the key differences, which is more favorable for each party, and potential negotiation points.

CLAUSE A:
{clause_a}

CLAUSE B:
{clause_b}

Provide analysis in JSON format:
{{
    "differences": ["key differences"],
    "favorable_to_party_a": ["points favorable to first party"],
    "favorable_to_party_b": ["points favorable to second party"],
    "negotiation_points": ["suggested negotiation items"],
    "recommendation": "overall recommendation"
}}

Provide ONLY the JSON response."""


def _parse_json_response(response: str) -> Dict[str, Any]:
    """Parse JSON from LLM response, handling markdown code blocks."""
    text = response.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = lines[1:]  # Remove opening ```json or ```
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find JSON object in the text
        start = text.find("{")
        end = text.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end])
            except json.JSONDecodeError:
                pass
        logger.warning("Failed to parse JSON response from LLM")
        return {"error": "Failed to parse response", "raw_response": response}


def analyze_clause(clause_text: str, model: str = "gemma4:latest") -> ClauseAnalysis:
    """
    Analyze a single contract clause for risks, obligations, and red flags.
    
    Args:
        clause_text: The contract clause text to analyze
        model: Ollama model to use
        
    Returns:
        ClauseAnalysis with detailed breakdown
    """
    prompt = CLAUSE_ANALYSIS_PROMPT.format(clause_text=clause_text)
    response = chat(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=2048
    )
    
    data = _parse_json_response(response)
    
    return ClauseAnalysis(
        clause_type=data.get("clause_type", "other"),
        risk_level=data.get("risk_level", "medium"),
        summary=data.get("summary", "Analysis unavailable"),
        obligations=data.get("obligations", []),
        deadlines=data.get("deadlines", []),
        red_flags=data.get("red_flags", []),
        recommendations=data.get("recommendations", []),
        key_terms=data.get("key_terms", [])
    )


def analyze_contract(contract_text: str, model: str = "gemma4:latest") -> ContractAnalysis:
    """
    Analyze a complete contract document.
    
    Args:
        contract_text: The full contract text
        model: Ollama model to use
        
    Returns:
        ContractAnalysis with all clause analyses
    """
    prompt = FULL_CONTRACT_PROMPT.format(contract_text=contract_text)
    response = chat(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=4096
    )
    
    data = _parse_json_response(response)
    
    clause_analyses = []
    for clause_data in data.get("clauses", []):
        clause_analyses.append(ClauseAnalysis(
            clause_type=clause_data.get("clause_type", "other"),
            risk_level=clause_data.get("risk_level", "medium"),
            summary=clause_data.get("summary", ""),
            obligations=clause_data.get("obligations", []),
            deadlines=clause_data.get("deadlines", []),
            red_flags=clause_data.get("red_flags", []),
            recommendations=clause_data.get("recommendations", []),
            key_terms=clause_data.get("key_terms", [])
        ))
    
    high_risk = sum(1 for c in clause_analyses if c.risk_level in ("high", "critical"))
    total_obligations = sum(len(c.obligations) for c in clause_analyses)
    total_deadlines = sum(len(c.deadlines) for c in clause_analyses)
    total_red_flags = sum(len(c.red_flags) for c in clause_analyses)
    
    return ContractAnalysis(
        title=data.get("title", "Untitled Contract"),
        overall_risk=data.get("overall_risk", "medium"),
        clause_analyses=clause_analyses,
        summary=data.get("summary", ""),
        total_clauses=len(clause_analyses),
        high_risk_count=high_risk,
        obligations_count=total_obligations,
        deadlines_count=total_deadlines,
        red_flags_count=total_red_flags
    )


def compare_clauses(clause_a: str, clause_b: str, model: str = "gemma4:latest") -> Dict[str, Any]:
    """
    Compare two contract clauses and identify differences.
    
    Args:
        clause_a: First clause text
        clause_b: Second clause text
        model: Ollama model to use
        
    Returns:
        Dictionary with comparison results
    """
    prompt = RISK_COMPARISON_PROMPT.format(clause_a=clause_a, clause_b=clause_b)
    response = chat(
        messages=[{"role": "user", "content": prompt}],
        model=model,
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=2048
    )
    
    return _parse_json_response(response)


def get_risk_color(risk_level: str) -> str:
    """Get display color for a risk level."""
    colors = {
        "low": "green",
        "medium": "yellow",
        "high": "red",
        "critical": "bold red"
    }
    return colors.get(risk_level.lower(), "white")


def get_risk_emoji(risk_level: str) -> str:
    """Get emoji for a risk level."""
    emojis = {
        "low": "🟢",
        "medium": "🟡",
        "high": "🔴",
        "critical": "🚨"
    }
    return emojis.get(risk_level.lower(), "⚪")


SAMPLE_CLAUSES = {
    "indemnification": (
        "Party A shall indemnify, defend, and hold harmless Party B, its officers, directors, "
        "employees, and agents from and against any and all claims, damages, losses, costs, and "
        "expenses (including reasonable attorneys' fees) arising out of or relating to Party A's "
        "breach of this Agreement or any negligent or wrongful act or omission of Party A."
    ),
    "termination": (
        "Either party may terminate this Agreement upon thirty (30) days' prior written notice "
        "to the other party. In the event of a material breach, the non-breaching party may "
        "terminate immediately upon written notice. Upon termination, all licenses granted "
        "hereunder shall immediately cease, and each party shall return or destroy all "
        "confidential information of the other party within fifteen (15) days."
    ),
    "non_compete": (
        "During the term of this Agreement and for a period of two (2) years following its "
        "termination, Party A shall not, directly or indirectly, engage in any business that "
        "competes with Party B's business within a 100-mile radius of any Party B location, "
        "nor shall Party A solicit any employees or customers of Party B."
    ),
    "limitation_of_liability": (
        "IN NO EVENT SHALL EITHER PARTY'S TOTAL AGGREGATE LIABILITY ARISING OUT OF OR RELATED "
        "TO THIS AGREEMENT EXCEED THE AMOUNTS PAID BY PARTY A TO PARTY B DURING THE TWELVE (12) "
        "MONTH PERIOD IMMEDIATELY PRECEDING THE EVENT GIVING RISE TO THE CLAIM. IN NO EVENT SHALL "
        "EITHER PARTY BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE "
        "DAMAGES."
    ),
    "confidentiality": (
        "Each party agrees to maintain the confidentiality of all Confidential Information received "
        "from the other party and to use such information solely for the purposes of this Agreement. "
        "Confidential Information shall be protected using the same degree of care used to protect "
        "the receiving party's own confidential information, but in no event less than reasonable care. "
        "This obligation shall survive for five (5) years following termination of this Agreement."
    )
}
