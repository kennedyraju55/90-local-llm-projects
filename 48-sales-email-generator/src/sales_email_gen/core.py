"""
Sales Email Generator - Core business logic.

Provides email generation, prospect research, follow-up sequences,
personalization scoring, and template management.
"""

import logging
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running  # noqa: E402

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Default configuration
# ---------------------------------------------------------------------------

DEFAULT_CONFIG_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "config.yaml"
)

TONE_DESCRIPTIONS: dict[str, str] = {
    "professional": "Formal, business-appropriate, respectful",
    "casual": "Friendly, conversational, approachable",
    "persuasive": "Compelling, benefit-focused, action-oriented",
    "consultative": "Advisory, problem-solving, thought-leadership",
}

TEMPLATE_LIBRARY: dict[str, dict] = {
    "cold_outreach": {
        "description": "First contact with a new prospect",
        "word_count": "150-200",
        "structure": (
            "1. Attention-grabbing opener referencing prospect's company\n"
            "2. Brief value proposition\n"
            "3. Social proof or relevant metric\n"
            "4. Clear, low-commitment CTA"
        ),
    },
    "follow_up": {
        "description": "Follow up after initial contact",
        "word_count": "100-150",
        "structure": (
            "1. Reference previous interaction\n"
            "2. Add new value or insight\n"
            "3. Restate benefit\n"
            "4. Specific next-step CTA"
        ),
    },
    "demo_request": {
        "description": "Invite prospect to a product demo",
        "word_count": "120-180",
        "structure": (
            "1. Personalized opener\n"
            "2. Highlight key feature relevant to prospect\n"
            "3. Demo offer with specific time options\n"
            "4. Easy scheduling CTA"
        ),
    },
    "case_study": {
        "description": "Share relevant case study",
        "word_count": "150-200",
        "structure": (
            "1. Connect prospect's challenge to case study\n"
            "2. Brief case study summary with metrics\n"
            "3. Draw parallel to prospect's situation\n"
            "4. Offer to discuss results"
        ),
    },
    "break_up": {
        "description": "Final follow-up before closing the loop",
        "word_count": "80-120",
        "structure": (
            "1. Acknowledge silence\n"
            "2. Briefly restate value\n"
            "3. Leave door open\n"
            "4. Simple yes/no CTA"
        ),
    },
}

SEQUENCE_TYPES = ["intro", "value_add", "case_study", "break_up"]

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


def load_config(path: Optional[str] = None) -> dict:
    """Load configuration from a YAML file.

    Falls back to sensible defaults when the file cannot be found.
    """
    config_path = path or os.environ.get("CONFIG_PATH", DEFAULT_CONFIG_PATH)
    config_path = str(Path(config_path).resolve())

    if os.path.exists(config_path):
        logger.info("Loading config from %s", config_path)
        with open(config_path, "r", encoding="utf-8") as fh:
            return yaml.safe_load(fh) or {}

    logger.warning("Config file not found at %s – using defaults", config_path)
    return {}


def _setup_logging(config: dict) -> None:
    """Configure logging from the config dict."""
    log_cfg = config.get("logging", {})
    level = getattr(logging, log_cfg.get("level", "INFO").upper(), logging.INFO)
    handlers: list[logging.Handler] = [logging.StreamHandler()]
    log_file = log_cfg.get("file")
    if log_file:
        handlers.append(logging.FileHandler(log_file))
    logging.basicConfig(level=level, handlers=handlers,
                        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _parse_email_response(response: str, fallback_subject: str = "Follow Up") -> dict:
    """Parse an LLM response into ``{subject, body}``."""
    lines = response.strip().split("\n")
    subject = ""
    body_start = 0
    for i, line in enumerate(lines):
        if line.lower().startswith("subject:"):
            subject = line.split(":", 1)[1].strip()
            body_start = i + 1
            break

    body = "\n".join(lines[body_start:]).strip()
    return {"subject": subject or fallback_subject, "body": body or response}


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------


def generate_email(
    prospect: str,
    product: str,
    tone: str,
    context: str = "",
    follow_up: bool = False,
) -> dict:
    """Generate a personalised sales email via the LLM.

    Returns:
        ``{"subject": str, "body": str}``
    """
    logger.info(
        "Generating %s email for prospect=%s product=%s tone=%s",
        "follow-up" if follow_up else "initial",
        prospect,
        product,
        tone,
    )

    config = load_config()
    model_cfg = config.get("model", {})
    tone_desc = TONE_DESCRIPTIONS.get(tone, TONE_DESCRIPTIONS["professional"])

    system_prompt = (
        f"You are an expert sales copywriter. Write a {tone} sales email. "
        f"Tone guidelines: {tone_desc}. "
        "The email should be concise (150-250 words), personalized, and include "
        "a clear call to action. "
        "Return the email with a subject line, greeting, body, and sign-off. "
        "Format: Start with 'Subject: ...' on the first line."
    )

    email_type = "follow-up" if follow_up else "initial outreach"
    context_text = f"\nAdditional context: {context}" if context else ""

    messages = [
        {
            "role": "user",
            "content": (
                f"Write a {email_type} sales email.\n\n"
                f"Prospect: {prospect}\n"
                f"Product/Service: {product}\n"
                f"Tone: {tone}{context_text}\n\n"
                "Make it personalized based on the prospect's role and company. "
                "Include a specific value proposition relevant to their situation."
            ),
        }
    ]

    response = chat(
        messages,
        system_prompt=system_prompt,
        temperature=model_cfg.get("temperature", 0.7),
        max_tokens=model_cfg.get("max_tokens", 2000),
    )

    result = _parse_email_response(response)
    logger.info("Email generated – subject: %s", result["subject"])
    return result


def generate_variants(
    prospect: str,
    product: str,
    tone: str,
    count: int = 3,
) -> list[dict]:
    """Generate multiple email variants for A/B testing."""
    logger.info("Generating %d variants for prospect=%s", count, prospect)
    variants: list[dict] = []

    for i in range(count):
        system_prompt = (
            f"You are a sales copywriter. Write variant #{i + 1} of a sales email. "
            f"Each variant should use a different angle/hook but same {tone} tone. "
            "Start with 'Subject: ...' on the first line. Keep it 100-200 words."
        )

        messages = [
            {
                "role": "user",
                "content": (
                    f"Prospect: {prospect}\nProduct: {product}\n"
                    f"Write a unique email variant #{i + 1} with a different approach."
                ),
            }
        ]

        response = chat(messages, system_prompt=system_prompt, temperature=0.8)
        result = _parse_email_response(response, fallback_subject=f"Variant {i + 1}")
        variants.append(result)

    logger.info("Generated %d variants", len(variants))
    return variants


def research_prospect(prospect_info: str) -> dict:
    """Use the LLM to generate a research profile for the prospect.

    Returns:
        ``{"pain_points": [...], "talking_points": [...], "industry_context": str}``
    """
    logger.info("Researching prospect: %s", prospect_info)

    system_prompt = (
        "You are a B2B sales research analyst. Given prospect information, "
        "generate a research profile. Return EXACTLY this format:\n"
        "PAIN_POINTS:\n- point1\n- point2\n- point3\n"
        "TALKING_POINTS:\n- point1\n- point2\n- point3\n"
        "INDUSTRY_CONTEXT:\nA brief paragraph about their industry."
    )

    messages = [
        {
            "role": "user",
            "content": f"Research this prospect and create a sales profile:\n{prospect_info}",
        }
    ]

    response = chat(messages, system_prompt=system_prompt, temperature=0.5)

    pain_points: list[str] = []
    talking_points: list[str] = []
    industry_context = ""

    section = ""
    for line in response.strip().split("\n"):
        stripped = line.strip()
        upper = stripped.upper()
        if "PAIN_POINTS" in upper or "PAIN POINTS" in upper:
            section = "pain"
            continue
        elif "TALKING_POINTS" in upper or "TALKING POINTS" in upper:
            section = "talk"
            continue
        elif "INDUSTRY_CONTEXT" in upper or "INDUSTRY CONTEXT" in upper:
            section = "industry"
            continue

        if stripped.startswith("- "):
            item = stripped[2:].strip()
            if section == "pain":
                pain_points.append(item)
            elif section == "talk":
                talking_points.append(item)
        elif section == "industry" and stripped:
            industry_context += (" " + stripped) if industry_context else stripped

    result = {
        "pain_points": pain_points,
        "talking_points": talking_points,
        "industry_context": industry_context.strip(),
    }
    logger.info(
        "Research complete – %d pain points, %d talking points",
        len(pain_points),
        len(talking_points),
    )
    return result


def generate_follow_up_sequence(
    prospect: str,
    product: str,
    tone: str,
    num_emails: int = 4,
) -> list[dict]:
    """Generate a multi-email follow-up sequence.

    The sequence follows: intro → value-add → case-study → break-up.
    Each email dict includes ``step``, ``subject``, ``body``, and ``delay_days``.
    """
    logger.info("Generating %d-email sequence for %s", num_emails, prospect)

    config = load_config()
    seq_cfg = config.get("sequence", {})
    delay_days = seq_cfg.get("delay_days", [0, 3, 7, 14])

    steps = SEQUENCE_TYPES[:num_emails]
    tone_desc = TONE_DESCRIPTIONS.get(tone, TONE_DESCRIPTIONS["professional"])
    sequence: list[dict] = []

    for idx, step in enumerate(steps):
        step_label = step.replace("_", " ").title()
        system_prompt = (
            f"You are a sales copywriter writing email {idx + 1} of {num_emails} "
            f"in a follow-up sequence. This is the '{step_label}' email. "
            f"Tone: {tone} – {tone_desc}. "
            "Start with 'Subject: ...' on the first line. Keep it 100-200 words."
        )

        prev_context = ""
        if idx > 0:
            prev_context = (
                f"\nPrevious email subject was: '{sequence[-1]['subject']}'. "
                "Reference it naturally."
            )

        messages = [
            {
                "role": "user",
                "content": (
                    f"Prospect: {prospect}\nProduct: {product}\n"
                    f"Write the {step_label} email (#{idx + 1} of {num_emails}).{prev_context}"
                ),
            }
        ]

        response = chat(messages, system_prompt=system_prompt, temperature=0.7)
        parsed = _parse_email_response(response, fallback_subject=step_label)
        parsed["step"] = step
        parsed["delay_days"] = delay_days[idx] if idx < len(delay_days) else (idx * 7)
        sequence.append(parsed)

    logger.info("Sequence generated with %d emails", len(sequence))
    return sequence


def score_personalization(email_body: str, prospect_info: str) -> dict:
    """Score how personalised an email body is on a 0-100 scale.

    Returns:
        ``{"score": int, "suggestions": [str, ...]}``
    """
    logger.info("Scoring personalisation for prospect: %s", prospect_info)

    system_prompt = (
        "You are a sales email quality analyst. Score the personalisation of this "
        "email on a 0-100 scale. Return EXACTLY this format:\n"
        "SCORE: <number>\n"
        "SUGGESTIONS:\n- suggestion1\n- suggestion2\n- suggestion3"
    )

    messages = [
        {
            "role": "user",
            "content": (
                f"Prospect info: {prospect_info}\n\n"
                f"Email body:\n{email_body}\n\n"
                "Score how personalized this email is for the prospect."
            ),
        }
    ]

    response = chat(messages, system_prompt=system_prompt, temperature=0.3)

    score = 50  # default
    suggestions: list[str] = []

    for line in response.strip().split("\n"):
        stripped = line.strip()
        if stripped.upper().startswith("SCORE"):
            numbers = re.findall(r"\d+", stripped)
            if numbers:
                score = min(int(numbers[0]), 100)
        elif stripped.startswith("- "):
            suggestions.append(stripped[2:].strip())

    result = {"score": score, "suggestions": suggestions}
    logger.info("Personalisation score: %d", score)
    return result


# ---------------------------------------------------------------------------
# Template helpers
# ---------------------------------------------------------------------------


def get_template(template_name: str) -> dict:
    """Return a template definition by name.

    Raises:
        KeyError: If the template name is not found.
    """
    if template_name not in TEMPLATE_LIBRARY:
        raise KeyError(
            f"Template '{template_name}' not found. "
            f"Available: {', '.join(TEMPLATE_LIBRARY)}"
        )
    return TEMPLATE_LIBRARY[template_name]


def list_templates() -> list[str]:
    """Return all available template names."""
    return list(TEMPLATE_LIBRARY.keys())
