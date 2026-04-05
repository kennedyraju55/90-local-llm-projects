"""
Patient Intake Summarizer - Core Module

AI-powered intake form summarization with medical history extraction,
risk factor identification, and pre-visit summary generation.

⚠️ DISCLAIMER: AI-generated summaries are for CLINICAL DECISION SUPPORT only.
All summaries MUST be reviewed and verified by a licensed physician before
being used for patient care decisions.
"""

from typing import Optional, List, Dict, Any
import os
import sys
import json
import logging
from datetime import datetime

# ---------------------------------------------------------------------------
# Path setup for shared common module
# ---------------------------------------------------------------------------
_common_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.insert(0, os.path.abspath(_common_path))

from common.llm_client import chat, check_ollama_running  # noqa: E402

from .config import load_config  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logger = logging.getLogger("patient_intake_summarizer")


def _setup_logging(level: str = "INFO") -> None:
    """Configure logging for the patient intake summarizer."""
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
CONFIG = load_config()
_setup_logging(CONFIG.get("log_level", "INFO"))

# ---------------------------------------------------------------------------
# Disclaimer
# ---------------------------------------------------------------------------

DISCLAIMER = """
⚠️  CLINICAL DISCLAIMER  ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This tool generates AI-assisted summaries for CLINICAL DECISION SUPPORT only.
All output MUST be reviewed and verified by a licensed physician.

• AI-generated summaries are NOT a substitute for clinical judgment.
• Do NOT use these summaries as the sole basis for treatment decisions.
• ALWAYS verify extracted information against original intake documents.
• This tool runs 100% locally — no patient data leaves this machine (HIPAA-friendly).
• The developers assume no liability for clinical decisions based on this output.

By using this tool, you acknowledge that all summaries require physician review
before being incorporated into patient care workflows.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a clinical intake summarization assistant designed to help healthcare \
staff process patient intake forms efficiently.

IMPORTANT RULES:
1. You are an AI assistant — all output MUST be reviewed by a licensed physician.
2. Summarize intake information accurately and concisely.
3. Preserve all clinically relevant details without embellishment.
4. Flag any inconsistencies or concerning findings.
5. Use standard medical terminology where appropriate.
6. Never fabricate or infer information not present in the intake form.
7. Clearly indicate when information is missing or incomplete.

When summarizing intake forms:
- Extract and categorize demographic information, chief complaint, and medical history.
- Identify current medications, allergies, and family history.
- Note social history factors relevant to care (smoking, alcohol, occupation).
- Highlight any red-flag findings or urgent concerns.
- Organize output in a structured, scannable clinical format.

Always end your summary with a note that this is an AI-generated summary requiring physician review."""

# ---------------------------------------------------------------------------
# Intake categories
# ---------------------------------------------------------------------------

INTAKE_CATEGORIES: dict[str, str] = {
    "demographics": "Patient demographics (name, age, sex, DOB, contact info)",
    "chief_complaint": "Primary reason for the visit",
    "medical_history": "Past medical history and chronic conditions",
    "surgical_history": "Previous surgeries and procedures",
    "medications": "Current medications, dosages, and frequency",
    "allergies": "Known allergies and adverse reactions",
    "family_history": "Relevant family medical history",
    "social_history": "Lifestyle factors (smoking, alcohol, occupation, exercise)",
    "review_of_systems": "Systematic review of organ systems",
}


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def summarize_intake(
    intake_text: str,
    summary_format: str = "structured",
    focus_areas: list[str] | None = None,
    conversation_history: list[dict] | None = None,
) -> str:
    """Summarize patient intake form text into a concise clinical summary.

    Args:
        intake_text: Raw text from the patient intake form.
        summary_format: One of 'brief', 'detailed', or 'structured'.
        focus_areas: Optional list of INTAKE_CATEGORIES keys to focus on.
        conversation_history: Optional prior messages for multi-turn context.

    Returns:
        AI-generated clinical summary text.
    """
    if conversation_history is None:
        conversation_history = []

    focus_instruction = ""
    if focus_areas:
        valid = [a for a in focus_areas if a in INTAKE_CATEGORIES]
        if valid:
            focus_instruction = (
                f"\n\nFocus especially on: {', '.join(valid)}. "
                "Still include other categories but keep them brief."
            )

    format_instructions = {
        "brief": "Provide a concise 3-5 sentence summary of the key clinical findings.",
        "detailed": "Provide a comprehensive summary covering all categories in narrative form.",
        "structured": (
            "Organize the summary with clear section headers for each category: "
            + ", ".join(INTAKE_CATEGORIES.keys())
            + ". Use bullet points under each section."
        ),
    }
    fmt = format_instructions.get(summary_format, format_instructions["structured"])

    user_prompt = (
        f"Please summarize the following patient intake form.\n\n"
        f"FORMAT: {fmt}{focus_instruction}\n\n"
        f"--- INTAKE FORM ---\n{intake_text}\n--- END ---"
    )

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(conversation_history)
    messages.append({"role": "user", "content": user_prompt})

    logger.info(
        "Summarizing intake (format=%s, focus=%s, history=%d msgs)",
        summary_format,
        focus_areas,
        len(conversation_history),
    )

    try:
        response = chat(messages)
        logger.info("Received intake summary (%d chars)", len(response))
        return response
    except Exception as exc:
        logger.error("Intake summarization failed: %s", exc)
        raise


def extract_medical_history(intake_text: str) -> Dict[str, Any]:
    """Extract and categorize medical history from intake text.

    Args:
        intake_text: Raw intake form text.

    Returns:
        Dictionary with keys from INTAKE_CATEGORIES and extracted content.
    """
    categories_list = "\n".join(
        f"- {key}: {desc}" for key, desc in INTAKE_CATEGORIES.items()
    )

    user_prompt = (
        f"Extract and categorize the following patient intake form into these categories. "
        f"Return a JSON object with these exact keys. If a category has no information, "
        f"set its value to \"Not provided\".\n\n"
        f"Categories:\n{categories_list}\n\n"
        f"--- INTAKE FORM ---\n{intake_text}\n--- END ---\n\n"
        f"Return ONLY valid JSON, no other text."
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    logger.info("Extracting medical history from intake text")

    try:
        response = chat(messages)
        # Attempt to parse JSON from the response
        try:
            result = json.loads(response)
        except json.JSONDecodeError:
            # Try extracting JSON block from markdown
            import re
            match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", response, re.DOTALL)
            if match:
                result = json.loads(match.group(1))
            else:
                result = {cat: response for cat in INTAKE_CATEGORIES}

        logger.info("Extracted medical history (%d categories)", len(result))
        return result
    except Exception as exc:
        logger.error("Medical history extraction failed: %s", exc)
        raise


def generate_pre_visit_summary(
    intake_data: dict[str, Any],
    appointment_type: str = "general",
) -> str:
    """Generate a pre-visit summary for the physician based on intake data.

    Args:
        intake_data: Dictionary of categorized intake information.
        appointment_type: Type of appointment (e.g., 'general', 'follow-up',
            'specialist', 'annual_physical', 'urgent').

    Returns:
        Pre-visit summary text for the physician.
    """
    intake_str = "\n".join(
        f"**{key}**: {value}" for key, value in intake_data.items()
    )

    user_prompt = (
        f"Generate a concise pre-visit summary for the physician.\n\n"
        f"Appointment Type: {appointment_type}\n\n"
        f"Patient Intake Data:\n{intake_str}\n\n"
        f"Include:\n"
        f"1. Key findings requiring attention\n"
        f"2. Suggested discussion points\n"
        f"3. Any red flags or concerns\n"
        f"4. Relevant history highlights for this appointment type\n"
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    logger.info("Generating pre-visit summary (type=%s)", appointment_type)

    try:
        response = chat(messages)
        logger.info("Generated pre-visit summary (%d chars)", len(response))
        return response
    except Exception as exc:
        logger.error("Pre-visit summary generation failed: %s", exc)
        raise


def identify_risk_factors(intake_text: str) -> List[str]:
    """Identify clinical risk factors from the intake text.

    Args:
        intake_text: Raw intake form text.

    Returns:
        List of identified risk factor strings.
    """
    user_prompt = (
        f"Analyze the following patient intake form and identify all clinical risk factors. "
        f"Return a JSON array of strings, each describing one risk factor. "
        f"Consider: age, family history, lifestyle factors, chronic conditions, "
        f"medication interactions, and social determinants of health.\n\n"
        f"--- INTAKE FORM ---\n{intake_text}\n--- END ---\n\n"
        f"Return ONLY a valid JSON array, no other text."
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    logger.info("Identifying risk factors from intake text")

    try:
        response = chat(messages)
        try:
            result = json.loads(response)
            if isinstance(result, list):
                return [str(r) for r in result]
        except json.JSONDecodeError:
            import re
            match = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", response, re.DOTALL)
            if match:
                result = json.loads(match.group(1))
                return [str(r) for r in result]
            # Fall back to line-by-line parsing
            lines = [
                line.strip().lstrip("•-*").strip()
                for line in response.strip().split("\n")
                if line.strip() and not line.strip().startswith("#")
            ]
            return [l for l in lines if l]

        logger.info("Identified %d risk factors", len(result))
        return result
    except Exception as exc:
        logger.error("Risk factor identification failed: %s", exc)
        raise


def flag_missing_info(intake_text: str) -> List[str]:
    """Flag missing or incomplete information in the intake form.

    Args:
        intake_text: Raw intake form text.

    Returns:
        List of strings describing missing information items.
    """
    categories_list = "\n".join(
        f"- {key}: {desc}" for key, desc in INTAKE_CATEGORIES.items()
    )

    user_prompt = (
        f"Review the following patient intake form and identify any missing or "
        f"incomplete information that should be collected before the visit. "
        f"Check against these standard intake categories:\n{categories_list}\n\n"
        f"Return a JSON array of strings, each describing one missing item.\n\n"
        f"--- INTAKE FORM ---\n{intake_text}\n--- END ---\n\n"
        f"Return ONLY a valid JSON array, no other text."
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    logger.info("Flagging missing information in intake form")

    try:
        response = chat(messages)
        try:
            result = json.loads(response)
            if isinstance(result, list):
                return [str(r) for r in result]
        except json.JSONDecodeError:
            import re
            match = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", response, re.DOTALL)
            if match:
                result = json.loads(match.group(1))
                return [str(r) for r in result]
            lines = [
                line.strip().lstrip("•-*").strip()
                for line in response.strip().split("\n")
                if line.strip() and not line.strip().startswith("#")
            ]
            return [l for l in lines if l]

        logger.info("Flagged %d missing items", len(result))
        return result
    except Exception as exc:
        logger.error("Missing info flagging failed: %s", exc)
        raise


# ---------------------------------------------------------------------------
# Intake session tracker
# ---------------------------------------------------------------------------

class IntakeSession:
    """Track intake summaries across a session."""

    def __init__(self) -> None:
        """Initialize the intake session."""
        self.summaries: list[dict] = []

    def add_summary(
        self,
        intake_text: str,
        summary: str,
        summary_format: str = "structured",
        focus_areas: list[str] | None = None,
    ) -> None:
        """Add an intake summary entry to the session.

        Args:
            intake_text: Original intake text.
            summary: Generated summary.
            summary_format: Format used for summarization.
            focus_areas: Focus areas requested.
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "intake_text": intake_text,
            "summary": summary,
            "summary_format": summary_format,
            "focus_areas": focus_areas or [],
        }
        self.summaries.append(entry)
        logger.info("Added session summary (total: %d)", len(self.summaries))

    def get_summaries(self) -> list[dict]:
        """Get all session summaries."""
        return list(self.summaries)

    def get_summary(self) -> dict:
        """Get an aggregate summary of the session."""
        if not self.summaries:
            return {
                "total_summaries": 0,
                "formats_used": [],
                "all_focus_areas": [],
            }

        formats: list[str] = []
        all_areas: list[str] = []

        for entry in self.summaries:
            fmt = entry.get("summary_format", "structured")
            if fmt not in formats:
                formats.append(fmt)
            for area in entry.get("focus_areas", []):
                if area not in all_areas:
                    all_areas.append(area)

        return {
            "total_summaries": len(self.summaries),
            "formats_used": formats,
            "all_focus_areas": all_areas,
        }


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def display_disclaimer() -> None:
    """Display the clinical disclaimer using rich formatting."""
    from rich.console import Console
    from rich.panel import Panel

    console = Console()
    console.print(Panel(DISCLAIMER, title="⚕️  Clinical Disclaimer", border_style="red"))
