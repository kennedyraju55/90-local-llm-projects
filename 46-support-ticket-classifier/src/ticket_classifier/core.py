"""
Support Ticket Classifier - Core business logic.

Provides ticket classification, priority queue management, SLA tracking,
team routing, auto-response generation, and analytics computation.
"""

import csv
import json
import logging
import os
import sys
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_SLA_HOURS = {"critical": 1, "high": 4, "medium": 8, "low": 24}

DEFAULT_PRIORITY_WEIGHTS = {"critical": 4, "high": 3, "medium": 2, "low": 1}

DEFAULT_TEAM_ROUTING: dict[str, str] = {
    "billing": "finance-team",
    "technical": "engineering-team",
    "account": "account-management",
    "feature_request": "product-team",
    "general": "support-team",
}

DEFAULT_CATEGORIES = ["billing", "technical", "account", "feature_request", "general"]

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


def load_config(path: str = "config.yaml") -> dict:
    """Load configuration from a YAML file.

    Returns a dict with keys: model, categories, sla_hours, team_routing,
    priority_weights, and logging.  Missing keys are filled with defaults.
    """
    config: dict[str, Any] = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as fh:
                config = yaml.safe_load(fh) or {}
            logger.info("Loaded config from %s", path)
        except Exception as exc:
            logger.warning("Failed to load config from %s: %s", path, exc)
    else:
        logger.info("Config file %s not found – using defaults", path)

    config.setdefault("categories", DEFAULT_CATEGORIES)
    config.setdefault("sla_hours", DEFAULT_SLA_HOURS)
    config.setdefault("team_routing", DEFAULT_TEAM_ROUTING)
    config.setdefault("priority_weights", DEFAULT_PRIORITY_WEIGHTS)
    config.setdefault("model", {"name": "gemma3", "temperature": 0.2, "max_tokens": 2000})
    config.setdefault("logging", {"level": "INFO", "file": "ticket_classifier.log"})

    # Apply logging settings
    log_cfg = config["logging"]
    logging.basicConfig(
        level=getattr(logging, log_cfg.get("level", "INFO").upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    return config


# ---------------------------------------------------------------------------
# Ticket loading
# ---------------------------------------------------------------------------


def load_tickets(file_path: str) -> list[dict]:
    """Load support tickets from a CSV file.

    Raises ``FileNotFoundError`` when the path does not exist,
    ``ValueError`` when the file is empty, and ``RuntimeError`` on
    any other read error.
    """
    if not os.path.exists(file_path):
        logger.error("File not found: %s", file_path)
        raise FileNotFoundError(f"File '{file_path}' not found.")

    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        if not rows:
            logger.error("CSV file is empty: %s", file_path)
            raise ValueError(f"CSV file '{file_path}' is empty.")
        logger.info("Loaded %d tickets from %s", len(rows), file_path)
        return rows
    except (FileNotFoundError, ValueError):
        raise
    except Exception as exc:
        logger.error("Error reading CSV %s: %s", file_path, exc)
        raise RuntimeError(f"Error reading CSV: {exc}") from exc


# ---------------------------------------------------------------------------
# Column detection
# ---------------------------------------------------------------------------


def find_text_column(data: list[dict]) -> str:
    """Identify the column most likely containing ticket descriptions."""
    candidates = [
        "description", "subject", "message", "text",
        "content", "body", "issue", "summary",
    ]
    for col in data[0].keys():
        if col.lower() in candidates:
            logger.debug("Detected text column by name: %s", col)
            return col

    best_col = max(
        data[0].keys(),
        key=lambda c: sum(len(str(row.get(c, ""))) for row in data[:5]),
    )
    logger.debug("Detected text column by length heuristic: %s", best_col)
    return best_col


# ---------------------------------------------------------------------------
# Single-ticket classification
# ---------------------------------------------------------------------------


def classify_ticket(
    ticket_text: str,
    categories: list[str],
    *,
    temperature: float = 0.2,
) -> dict:
    """Classify a single support ticket via the LLM.

    Returns a dict with keys: category, priority, confidence,
    suggested_response.
    """
    categories_text = ", ".join(categories)

    system_prompt = (
        "You are a support ticket classifier. Classify the ticket into one of the "
        f"provided categories and assign a priority level. Categories: {categories_text}\n"
        "Respond ONLY with valid JSON:\n"
        '{"category": "one of the categories", "priority": "low|medium|high|critical", '
        '"confidence": 0.0-1.0, "suggested_response": "brief initial response to customer"}'
    )

    messages = [{"role": "user", "content": f"Classify this support ticket:\n\n{ticket_text}"}]
    response = chat(messages, system_prompt=system_prompt, temperature=temperature)
    logger.debug("LLM raw response: %s", response)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        if start >= 0 and end > start:
            result = json.loads(response[start:end])
            # Normalise category
            if result.get("category", "").lower() not in [c.lower() for c in categories]:
                result["category"] = categories[0]
            # Normalise priority
            valid_priorities = {"low", "medium", "high", "critical"}
            if result.get("priority", "").lower() not in valid_priorities:
                result["priority"] = "medium"
            # Normalise confidence
            try:
                result["confidence"] = float(result.get("confidence", 0.5))
            except (TypeError, ValueError):
                result["confidence"] = 0.5
            logger.info(
                "Classified ticket -> category=%s priority=%s confidence=%.2f",
                result["category"], result["priority"], result["confidence"],
            )
            return result
    except (json.JSONDecodeError, ValueError) as exc:
        logger.warning("Failed to parse LLM response: %s", exc)

    fallback = {
        "category": categories[0],
        "priority": "medium",
        "confidence": 0.5,
        "suggested_response": "We have received your ticket and will respond shortly.",
    }
    logger.info("Returning fallback classification")
    return fallback


# ---------------------------------------------------------------------------
# Batch classification
# ---------------------------------------------------------------------------


def classify_tickets_batch(
    tickets: list[dict],
    categories: list[str],
    text_col: str,
    *,
    temperature: float = 0.2,
    on_progress: Optional[Any] = None,
) -> list[dict]:
    """Classify a list of tickets. Returns parallel list of classification dicts.

    ``on_progress`` is an optional callback ``(index, total) -> None`` invoked
    after each ticket.
    """
    classifications: list[dict] = []
    total = len(tickets)
    for idx, ticket in enumerate(tickets):
        text = str(ticket.get(text_col, ""))
        clf = classify_ticket(text, categories, temperature=temperature)
        classifications.append(clf)
        if on_progress:
            on_progress(idx + 1, total)
    logger.info("Batch classification complete: %d tickets", total)
    return classifications


# ---------------------------------------------------------------------------
# Priority queue
# ---------------------------------------------------------------------------


def build_priority_queue(
    tickets: list[dict],
    classifications: list[dict],
    text_col: str,
    priority_weights: Optional[dict[str, int]] = None,
) -> list[dict]:
    """Return tickets sorted by priority (highest first).

    Each item contains: position, ticket_text, category, priority, confidence,
    suggested_response, and weight.
    """
    weights = priority_weights or DEFAULT_PRIORITY_WEIGHTS

    queue: list[dict] = []
    for ticket, clf in zip(tickets, classifications):
        priority = clf.get("priority", "medium").lower()
        queue.append({
            "ticket_text": str(ticket.get(text_col, ""))[:120],
            "category": clf.get("category", ""),
            "priority": priority,
            "confidence": clf.get("confidence", 0.5),
            "suggested_response": clf.get("suggested_response", ""),
            "weight": weights.get(priority, 1),
        })

    queue.sort(key=lambda x: (-x["weight"], -x["confidence"]))

    for pos, item in enumerate(queue, 1):
        item["position"] = pos

    logger.info("Built priority queue with %d items", len(queue))
    return queue


# ---------------------------------------------------------------------------
# SLA tracking
# ---------------------------------------------------------------------------


def compute_sla_deadlines(
    classifications: list[dict],
    sla_hours: Optional[dict[str, int]] = None,
    *,
    created_at: Optional[datetime] = None,
) -> list[dict]:
    """Compute SLA deadline for each classification.

    Returns list of dicts with: priority, sla_hours, deadline, remaining_hours.
    """
    hours_map = sla_hours or DEFAULT_SLA_HOURS
    now = created_at or datetime.now()

    results: list[dict] = []
    for clf in classifications:
        priority = clf.get("priority", "medium").lower()
        hours = hours_map.get(priority, 24)
        deadline = now + timedelta(hours=hours)
        remaining = max(0.0, (deadline - datetime.now()).total_seconds() / 3600)
        results.append({
            "priority": priority,
            "sla_hours": hours,
            "deadline": deadline.isoformat(),
            "remaining_hours": round(remaining, 2),
        })

    logger.info("Computed SLA deadlines for %d tickets", len(results))
    return results


# ---------------------------------------------------------------------------
# Team routing
# ---------------------------------------------------------------------------


def route_to_team(
    classification: dict,
    routing_rules: Optional[dict[str, str]] = None,
) -> str:
    """Determine the team responsible for a classified ticket."""
    rules = routing_rules or DEFAULT_TEAM_ROUTING
    category = classification.get("category", "general").lower()
    team = rules.get(category, "support-team")
    logger.debug("Routed category=%s -> team=%s", category, team)
    return team


# ---------------------------------------------------------------------------
# Auto-response generation
# ---------------------------------------------------------------------------


def generate_auto_response(ticket_text: str, classification: dict) -> str:
    """Generate a polished auto-response for the customer.

    Uses the ``suggested_response`` from the classification as a starting
    point and enriches it with priority and team information.
    """
    priority = classification.get("priority", "medium").lower()
    category = classification.get("category", "general")
    suggested = classification.get("suggested_response", "")

    sla = DEFAULT_SLA_HOURS.get(priority, 24)

    response_parts = [
        f"Thank you for contacting us regarding your {category} issue.",
        "",
        suggested if suggested else "We have received your ticket and will respond shortly.",
        "",
        f"Your ticket has been classified as **{priority}** priority.",
        f"Our team will respond within **{sla} hour(s)**.",
        "",
        "If your issue is urgent, please don't hesitate to call our support hotline.",
    ]

    return "\n".join(response_parts)


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------


def compute_analytics(
    classifications: list[dict],
    categories: list[str],
) -> dict:
    """Compute analytics over a batch of classifications.

    Returns dict with: total_tickets, category_distribution,
    priority_distribution, avg_confidence, sla_compliance (all within SLA),
    high_priority_count.
    """
    total = len(classifications)
    if total == 0:
        return {
            "total_tickets": 0,
            "category_distribution": {},
            "priority_distribution": {},
            "avg_confidence": 0.0,
            "sla_compliance": 0.0,
            "high_priority_count": 0,
        }

    # Category distribution
    cat_dist: dict[str, int] = {c: 0 for c in categories}
    pri_dist: dict[str, int] = {"low": 0, "medium": 0, "high": 0, "critical": 0}
    confidences: list[float] = []
    high_priority = 0

    for clf in classifications:
        cat = clf.get("category", "").lower()
        for c in categories:
            if c.lower() == cat:
                cat_dist[c] = cat_dist.get(c, 0) + 1
                break

        pri = clf.get("priority", "medium").lower()
        pri_dist[pri] = pri_dist.get(pri, 0) + 1

        if pri in ("high", "critical"):
            high_priority += 1

        try:
            confidences.append(float(clf.get("confidence", 0.5)))
        except (TypeError, ValueError):
            confidences.append(0.5)

    avg_conf = sum(confidences) / len(confidences) if confidences else 0.0

    # SLA compliance: percentage of tickets that are NOT critical
    # (simplified – real systems would check actual response times)
    sla_compliant = total - pri_dist.get("critical", 0)
    sla_compliance = (sla_compliant / total) * 100 if total else 0.0

    analytics = {
        "total_tickets": total,
        "category_distribution": cat_dist,
        "priority_distribution": pri_dist,
        "avg_confidence": round(avg_conf, 3),
        "sla_compliance": round(sla_compliance, 1),
        "high_priority_count": high_priority,
    }

    logger.info("Analytics: %s", analytics)
    return analytics
