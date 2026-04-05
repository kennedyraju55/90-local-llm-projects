"""Core business logic for the Policy Compliance Checker."""

from typing import Optional, List, Dict, Any, Tuple, Union
import json
import re
import logging

import click

from .utils import setup_sys_path

setup_sys_path()
from common.llm_client import chat, check_ollama_running

logger = logging.getLogger(__name__)

SEVERITY_COLORS = {
    "high": "red",
    "medium": "yellow",
    "low": "cyan",
}

COMPLIANCE_SYSTEM_PROMPT = """You are an expert policy compliance auditor. Analyze the provided document 
against the given policy rules. Return your analysis as valid JSON with this exact structure:

{
  "compliance_score": <integer 0-100>,
  "summary": "<brief overall compliance summary>",
  "violations": [
    {
      "rule": "<policy rule violated>",
      "severity": "high|medium|low",
      "description": "<what is wrong>",
      "location": "<where in the document>",
      "remediation": "<how to fix it>"
    }
  ],
  "compliant_areas": [
    {
      "rule": "<policy rule satisfied>",
      "description": "<how the document complies>"
    }
  ],
  "recommendations": [
    "<actionable recommendation string>"
  ]
}

Return ONLY valid JSON. No markdown, no code fences, no extra text."""


def read_file(filepath: str) -> str:
    """Read and return the contents of a file.

    Args:
        filepath: Path to the file to read.

    Returns:
        The file contents as a string.

    Raises:
        click.ClickException: If the file cannot be read.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise click.ClickException(f"File not found: {filepath}")
    except PermissionError:
        raise click.ClickException(f"Permission denied: {filepath}")
    except Exception as e:
        raise click.ClickException(f"Error reading {filepath}: {e}")


def check_compliance(document: str, policy: str, config: dict = None) -> dict:
    """Send document and policy to the LLM for compliance analysis.

    Args:
        document: The document text to check.
        policy: The policy rules to check against.
        config: Optional configuration dictionary.

    Returns:
        A dict containing compliance_score, violations, compliant_areas,
        recommendations, and summary.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    prompt = (
        f"## Policy Rules\n\n{policy}\n\n"
        f"## Document to Check\n\n{document}\n\n"
        "Analyze the document against the policy rules above and return "
        "the compliance report as JSON."
    )

    messages = [{"role": "user", "content": prompt}]
    response = chat(
        messages=messages,
        system_prompt=COMPLIANCE_SYSTEM_PROMPT,
        temperature=llm_config.get("temperature", 0.3),
        max_tokens=llm_config.get("max_tokens", 4096),
    )

    logger.info("Compliance check completed")
    return parse_compliance_response(response)


def parse_compliance_response(response: str) -> dict:
    """Parse the LLM JSON response into a compliance report dict.

    Args:
        response: Raw LLM response string (expected JSON).

    Returns:
        Parsed compliance report dictionary with guaranteed keys.
    """
    cleaned = response.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    cleaned = cleaned.strip()

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group())
            except json.JSONDecodeError:
                return _fallback_report(response)
        else:
            return _fallback_report(response)

    data.setdefault("compliance_score", 0)
    data.setdefault("summary", "No summary provided.")
    data.setdefault("violations", [])
    data.setdefault("compliant_areas", [])
    data.setdefault("recommendations", [])
    data["compliance_score"] = max(0, min(100, int(data["compliance_score"])))

    return data


def _fallback_report(raw: str) -> dict:
    """Return a fallback report when LLM output cannot be parsed."""
    return {
        "compliance_score": 0,
        "summary": "Unable to parse compliance report from LLM response.",
        "violations": [],
        "compliant_areas": [],
        "recommendations": [
            "Re-run the check or review the raw LLM output below.",
            raw[:500],
        ],
    }


def filter_violations(violations: list, severity: str) -> list:
    """Filter violations by severity level.

    Args:
        violations: List of violation dicts.
        severity: Severity filter — 'all', 'high', 'medium', or 'low'.

    Returns:
        Filtered list of violations.
    """
    if severity == "all":
        return violations
    return [v for v in violations if v.get("severity", "").lower() == severity]


def get_score_color(score: int) -> str:
    """Get the display color for a compliance score."""
    if score >= 80:
        return "green"
    elif score >= 50:
        return "yellow"
    return "red"


def get_score_label(score: int, config: dict = None) -> str:
    """Get a human-readable label for a compliance score."""
    config = config or {}
    thresholds = config.get("compliance", {}).get("score_thresholds", {"pass": 80, "warning": 50})
    if score >= thresholds.get("pass", 80):
        return "PASS"
    elif score >= thresholds.get("warning", 50):
        return "WARNING"
    return "FAIL"
