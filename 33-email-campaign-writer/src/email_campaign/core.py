#!/usr/bin/env python3
"""Core logic for Email Campaign Writer."""

import os
import re
import sys
import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from common.llm_client import chat, check_ollama_running  # noqa: E402

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_CONFIG: Optional[dict] = None


def _find_config_path() -> str:
    """Locate config.yaml relative to this file."""
    return os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")


def load_config() -> dict:
    """Load and cache application configuration from config.yaml."""
    global _CONFIG
    if _CONFIG is not None:
        return _CONFIG

    config_path = _find_config_path()
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as fh:
            _CONFIG = yaml.safe_load(fh) or {}
            logger.info("Loaded config from %s", config_path)
    else:
        logger.warning("Config file not found at %s; using defaults", config_path)
        _CONFIG = {}
    return _CONFIG


def _get_llm_config() -> dict:
    """Return the LLM section of the config with defaults."""
    cfg = load_config().get("llm", {})
    return {
        "model": cfg.get("model", "llama3"),
        "temperature": cfg.get("temperature", 0.7),
        "max_tokens": cfg.get("max_tokens", 4096),
    }


def _get_campaign_config() -> dict:
    """Return the campaign section of the config with defaults."""
    cfg = load_config().get("campaign", {})
    return {
        "default_type": cfg.get("default_type", "promotional"),
        "default_emails": cfg.get("default_emails", 3),
        "max_emails": cfg.get("max_emails", 10),
        "metrics": cfg.get("metrics", {}),
    }


def setup_logging() -> None:
    """Configure logging from config.yaml."""
    level_name = load_config().get("logging", {}).get("level", "INFO")
    logging.basicConfig(
        level=getattr(logging, level_name.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CAMPAIGN_TYPES = [
    "welcome",
    "promotional",
    "nurture",
    "re-engagement",
    "product-launch",
]

# Default send-day spacing per campaign type (day offsets for each email index)
_DEFAULT_SEND_DAYS: dict[str, list[int]] = {
    "welcome": [0, 1, 3, 5, 7, 10, 14, 18, 21, 28],
    "promotional": [0, 2, 4, 7, 10, 14, 17, 21, 25, 30],
    "nurture": [0, 3, 7, 10, 14, 21, 28, 35, 42, 49],
    "re-engagement": [0, 3, 7, 14, 21, 30, 37, 44, 51, 60],
    "product-launch": [0, 1, 3, 5, 7, 10, 14, 17, 21, 28],
}


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------


@dataclass
class Email:
    """Represents a single email in a campaign sequence."""

    subject_a: str
    subject_b: str
    preview_text: str
    body: str
    cta_text: str
    cta_url: str = ""
    send_day: int = 0
    personalization_tokens: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Post init."""
        if not self.personalization_tokens:
            self.personalization_tokens = extract_personalization_tokens(self.body)


@dataclass
class Campaign:
    """Represents a full email campaign."""

    name: str
    product: str
    audience: str
    campaign_type: str
    emails: list[Email] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())


# ---------------------------------------------------------------------------
# Prompt building
# ---------------------------------------------------------------------------


def build_prompt(product: str, audience: str, num_emails: int, campaign_type: str) -> str:
    """Build the email campaign generation prompt."""
    return (
        f"Create a {num_emails}-email marketing campaign sequence for:\n\n"
        f"Product/Service: {product}\n"
        f"Target Audience: {audience}\n"
        f"Campaign Type: {campaign_type}\n\n"
        f"For EACH email in the sequence, provide:\n"
        f"1. **Email Number** and **Subject Line** (with 2 A/B variants)\n"
        f"2. **Preview Text** (the snippet shown in inbox)\n"
        f"3. **Body** (full email copy with personalization placeholders like {{{{first_name}}}})\n"
        f"4. **Call to Action** (button text and purpose)\n"
        f"5. **Send Timing** (suggested day/time relative to previous email)\n\n"
        f"Make each email build on the previous one to create a cohesive journey.\n"
        f"Use proven copywriting frameworks (AIDA, PAS, etc.).\n"
        f"Include compelling subject lines with high open-rate potential.\n"
    )


# ---------------------------------------------------------------------------
# LLM interaction
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = (
    "You are an expert email marketing copywriter with deep knowledge of "
    "conversion optimization, A/B testing, and customer journey mapping. "
    "You write compelling emails that drive engagement and conversions."
)


def generate_campaign(product: str, audience: str, num_emails: int, campaign_type: str) -> str:
    """Generate an email campaign using the LLM and return raw text."""
    llm_cfg = _get_llm_config()
    user_prompt = build_prompt(product, audience, num_emails, campaign_type)
    messages = [{"role": "user", "content": user_prompt}]
    logger.info(
        "Generating campaign: product=%s audience=%s emails=%d type=%s",
        product,
        audience,
        num_emails,
        campaign_type,
    )
    return chat(
        messages,
        system_prompt=_SYSTEM_PROMPT,
        temperature=llm_cfg["temperature"],
        max_tokens=llm_cfg["max_tokens"],
    )


def generate_subject_variants(product: str, audience: str, num_variants: int = 3) -> list[str]:
    """Generate A/B subject-line variants for testing.

    Returns a list of subject-line strings.
    """
    prompt = (
        f"Generate {num_variants} compelling email subject line variants for:\n"
        f"Product/Service: {product}\n"
        f"Target Audience: {audience}\n\n"
        f"Return ONLY the subject lines, one per line, numbered 1-{num_variants}.\n"
        f"Focus on high open-rate potential using curiosity, urgency, and personalization."
    )
    messages = [{"role": "user", "content": prompt}]
    llm_cfg = _get_llm_config()
    raw = chat(
        messages,
        system_prompt=_SYSTEM_PROMPT,
        temperature=llm_cfg["temperature"],
        max_tokens=512,
    )
    lines = [
        re.sub(r"^\d+[\.\)]\s*", "", line).strip()
        for line in raw.strip().splitlines()
        if line.strip()
    ]
    return lines[:num_variants]


# ---------------------------------------------------------------------------
# Campaign building helpers
# ---------------------------------------------------------------------------


def build_email_sequence(
    product: str,
    audience: str,
    num_emails: int,
    campaign_type: str,
) -> Campaign:
    """Generate a full campaign and return a structured Campaign object.

    Calls the LLM, then wraps the raw output into Email dataclasses with
    reasonable defaults for fields the LLM may not explicitly return.
    """
    raw_text = generate_campaign(product, audience, num_emails, campaign_type)
    send_days = _DEFAULT_SEND_DAYS.get(campaign_type, _DEFAULT_SEND_DAYS["promotional"])

    emails: list[Email] = []
    for idx in range(num_emails):
        day = send_days[idx] if idx < len(send_days) else send_days[-1] + (idx * 3)
        email = Email(
            subject_a=f"Email {idx + 1} - Subject A",
            subject_b=f"Email {idx + 1} - Subject B",
            preview_text=f"Preview for email {idx + 1}",
            body=raw_text if idx == 0 else f"(See full campaign above — email {idx + 1})",
            cta_text="Learn More",
            send_day=day,
        )
        emails.append(email)

    campaign = Campaign(
        name=f"{campaign_type.title()} Campaign for {product}",
        product=product,
        audience=audience,
        campaign_type=campaign_type,
        emails=emails,
    )
    logger.info("Built campaign with %d emails", len(emails))
    return campaign


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------


def extract_personalization_tokens(template: str) -> list[str]:
    """Find all ``{{token}}`` placeholders in an email body.

    Returns a sorted, deduplicated list of token names.
    """
    tokens = re.findall(r"\{\{(\w+)\}\}", template)
    return sorted(set(tokens))


def preview_html(email_body: str) -> str:
    """Wrap an email body in a minimal responsive HTML email template."""
    escaped = email_body.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    paragraphs = "\n".join(
        f"<p style=\"margin:0 0 16px 0;line-height:1.6;\">{line}</p>"
        if line.strip()
        else "<br>"
        for line in escaped.splitlines()
    )
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Email Preview</title>
</head>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,Helvetica,sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;">
    <tr>
      <td align="center" style="padding:40px 0;">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0"
               style="background:#ffffff;border-radius:8px;overflow:hidden;">
          <tr>
            <td style="padding:32px 40px;">
              {paragraphs}
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""


def render_email(email: Email, user_data: dict[str, str]) -> str:
    """Replace personalization tokens with actual user data.

    Tokens not found in *user_data* are left untouched.
    """
    result = email.body
    for token, value in user_data.items():
        result = result.replace(f"{{{{{token}}}}}", str(value))
    return result


def calculate_sequence_timeline(campaign: Campaign) -> list[tuple[int, str]]:
    """Return a list of ``(day_number, email_subject)`` for the send schedule."""
    return [(email.send_day, email.subject_a) for email in campaign.emails]


def estimate_campaign_metrics(campaign: Campaign) -> dict[str, Any]:
    """Estimate open/click rates based on campaign type and config metrics.

    Returns a dict with per-email and aggregate estimates.
    """
    metrics_cfg = _get_campaign_config().get("metrics", {})
    type_metrics = metrics_cfg.get(campaign.campaign_type, {})
    avg_open = type_metrics.get("avg_open_rate", 0.25)
    avg_click = type_metrics.get("avg_click_rate", 0.03)

    per_email: list[dict[str, Any]] = []
    for idx, email in enumerate(campaign.emails):
        decay = 1.0 - (idx * 0.03)
        decay = max(decay, 0.5)
        per_email.append(
            {
                "email_number": idx + 1,
                "subject": email.subject_a,
                "estimated_open_rate": round(avg_open * decay, 4),
                "estimated_click_rate": round(avg_click * decay, 4),
            }
        )

    total_open = sum(e["estimated_open_rate"] for e in per_email) / max(len(per_email), 1)
    total_click = sum(e["estimated_click_rate"] for e in per_email) / max(len(per_email), 1)

    return {
        "campaign_type": campaign.campaign_type,
        "num_emails": len(campaign.emails),
        "avg_open_rate": round(total_open, 4),
        "avg_click_rate": round(total_click, 4),
        "per_email": per_email,
    }
