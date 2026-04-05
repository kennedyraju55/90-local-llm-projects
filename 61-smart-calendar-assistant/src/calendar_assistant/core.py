#!/usr/bin/env python3
"""Core business logic for Smart Calendar Assistant."""

import sys
import os
import json
import logging
from datetime import datetime, timedelta, time
from typing import Any, Dict, List, Optional, Tuple, Union
from zoneinfo import ZoneInfo

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = {
    "app": {"name": "Smart Calendar Assistant", "version": "1.0.0", "log_level": "INFO", "data_dir": "./data"},
    "calendar": {
        "default_timezone": "UTC",
        "working_hours": {"start": "09:00", "end": "17:00"},
        "break_duration_minutes": 15,
        "min_meeting_gap_minutes": 10,
        "priority_levels": {"critical": 5, "high": 4, "medium": 3, "low": 2, "optional": 1},
    },
    "llm": {"model": "llama3", "temperature": 0.6, "system_prompt": "You are an expert calendar and productivity assistant."},
}


def load_config(config_path: Optional[str] = None) -> dict:
    """Load configuration from a YAML file, falling back to defaults."""
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')
    config_path = os.path.abspath(config_path)

    if os.path.exists(config_path):
        logger.info("Loading config from %s", config_path)
        with open(config_path, "r", encoding="utf-8") as fh:
            loaded = yaml.safe_load(fh) or {}
        # Merge with defaults (shallow per top-level key)
        merged = {}
        for key in DEFAULT_CONFIG:
            if key in loaded and isinstance(loaded[key], dict):
                merged[key] = {**DEFAULT_CONFIG[key], **loaded[key]}
            else:
                merged[key] = DEFAULT_CONFIG.get(key, loaded.get(key))
        return merged
    logger.warning("Config file not found at %s – using defaults", config_path)
    return DEFAULT_CONFIG


_config: dict = {}


def get_config() -> dict:
    """Return the cached application config, loading it on first access."""
    global _config
    if not _config:
        _config = load_config()
    return _config

# ---------------------------------------------------------------------------
# Schedule helpers
# ---------------------------------------------------------------------------


def load_schedule(file_path: str) -> list[dict]:
    """Load schedule events from a JSON file.

    Each event is expected to have at least: title, start, end.
    Optional fields: priority, attendees, location, description.
    """
    logger.info("Loading schedule from %s", file_path)
    if not os.path.exists(file_path):
        logger.error("Schedule file not found: %s", file_path)
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            events = json.load(fh)
        if not isinstance(events, list):
            logger.error("Schedule file must contain a JSON array")
            return []
        logger.info("Loaded %d events", len(events))
        return events
    except json.JSONDecodeError as exc:
        logger.error("Invalid JSON in schedule file: %s", exc)
        return []


def display_schedule(events: list[dict]) -> str:
    """Return a human-readable text representation of the schedule."""
    if not events:
        return "No events in schedule."
    lines: list[str] = []
    for i, event in enumerate(events, 1):
        title = event.get("title", "Untitled")
        start = event.get("start", "N/A")
        end = event.get("end", "N/A")
        priority = event.get("priority", "medium")
        lines.append(f"{i}. [{priority.upper()}] {title}  ({start} → {end})")
    return "\n".join(lines)

# ---------------------------------------------------------------------------
# LLM-powered features (original)
# ---------------------------------------------------------------------------


def optimize_schedule(events: list[dict]) -> str:
    """Use the LLM to suggest an optimized ordering / grouping of events."""
    if not events:
        return "No events to optimize."
    config = get_config()
    prompt = (
        f"{config['llm']['system_prompt']}\n\n"
        "Analyze and optimize the following schedule. Suggest improvements for "
        "time management, grouping related meetings, adding breaks, and reducing "
        "context switching.\n\n"
        f"Schedule:\n{json.dumps(events, indent=2)}\n\n"
        f"Working hours: {config['calendar']['working_hours']['start']} – "
        f"{config['calendar']['working_hours']['end']}\n"
        f"Minimum break between meetings: {config['calendar']['break_duration_minutes']} min\n\n"
        "Provide a detailed optimized schedule with reasoning."
    )
    logger.info("Requesting schedule optimization from LLM")
    return generate(prompt)


def suggest_meeting_time(events: list[dict], meeting_duration: int = 30, attendees: Optional[str] = None) -> str:
    """Use the LLM to suggest the best time slot for a new meeting."""
    config = get_config()
    prompt = (
        f"{config['llm']['system_prompt']}\n\n"
        "Given the current schedule, suggest the best time for a new meeting.\n\n"
        f"Current schedule:\n{json.dumps(events, indent=2)}\n"
        f"Meeting duration: {meeting_duration} minutes\n"
    )
    if attendees:
        prompt += f"Attendees: {attendees}\n"
    prompt += (
        f"\nWorking hours: {config['calendar']['working_hours']['start']} – "
        f"{config['calendar']['working_hours']['end']}\n"
        f"Minimum gap between meetings: {config['calendar']['min_meeting_gap_minutes']} min\n\n"
        "Suggest optimal time slots with reasoning."
    )
    logger.info("Requesting meeting time suggestion from LLM")
    return generate(prompt)


def analyze_workload(events: list[dict]) -> str:
    """Use the LLM to analyze workload distribution across the schedule."""
    if not events:
        return "No events to analyze."
    config = get_config()
    prompt = (
        f"{config['llm']['system_prompt']}\n\n"
        "Analyze the workload distribution in the following schedule. "
        "Identify overloaded periods, suggest improvements, and rate the "
        "overall work-life balance.\n\n"
        f"Schedule:\n{json.dumps(events, indent=2)}\n\n"
        f"Working hours: {config['calendar']['working_hours']['start']} – "
        f"{config['calendar']['working_hours']['end']}\n\n"
        "Provide a detailed workload analysis with recommendations."
    )
    logger.info("Requesting workload analysis from LLM")
    return generate(prompt)

# ---------------------------------------------------------------------------
# New pure-Python enhanced features
# ---------------------------------------------------------------------------


def _parse_dt(value: str, tz: Optional[ZoneInfo] = None) -> datetime:
    """Parse an ISO-ish datetime string, attaching *tz* when the string is naive."""
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"):
        try:
            dt = datetime.strptime(value, fmt)
            if tz and dt.tzinfo is None:
                dt = dt.replace(tzinfo=tz)
            return dt
        except ValueError:
            continue
    raise ValueError(f"Unable to parse datetime string: {value!r}")


def detect_conflicts(events: list[dict], timezone: Optional[str] = None) -> list[tuple[dict, dict]]:
    """Detect overlapping events and return a list of conflicting pairs.

    Parameters
    ----------
    events : list of dicts with 'start' and 'end' keys.
    timezone : IANA timezone name (e.g. 'America/New_York'). Falls back to config default.

    Returns
    -------
    List of (event_a, event_b) tuples that overlap.
    """
    config = get_config()
    tz_name = timezone or config["calendar"]["default_timezone"]
    tz = ZoneInfo(tz_name)
    logger.info("Detecting conflicts in %d events (tz=%s)", len(events), tz_name)

    parsed: list[tuple[datetime, datetime, dict]] = []
    for ev in events:
        try:
            start = _parse_dt(ev["start"], tz)
            end = _parse_dt(ev["end"], tz)
            parsed.append((start, end, ev))
        except (KeyError, ValueError) as exc:
            logger.warning("Skipping event due to parse error: %s – %s", ev, exc)

    parsed.sort(key=lambda x: x[0])

    conflicts: list[tuple[dict, dict]] = []
    for i in range(len(parsed)):
        for j in range(i + 1, len(parsed)):
            s_i, e_i, ev_i = parsed[i]
            s_j, e_j, ev_j = parsed[j]
            if s_j >= e_i:
                break  # no further overlap possible (sorted)
            conflicts.append((ev_i, ev_j))
            logger.debug("Conflict: '%s' overlaps with '%s'", ev_i.get("title"), ev_j.get("title"))

    logger.info("Found %d conflict(s)", len(conflicts))
    return conflicts


def score_priority(event: dict) -> int:
    """Return a numeric priority score for an event.

    Scoring factors:
    - Explicit priority label (critical=5 … optional=1)
    - Number of attendees (more attendees → higher importance)
    - Duration (longer meetings score slightly higher)
    """
    config = get_config()
    levels = config["calendar"]["priority_levels"]
    label = event.get("priority", "medium").lower()
    base_score = levels.get(label, levels.get("medium", 3))

    # Attendee bonus
    attendees = event.get("attendees", [])
    if isinstance(attendees, str):
        attendees = [a.strip() for a in attendees.split(",") if a.strip()]
    attendee_bonus = min(len(attendees), 5)  # cap at 5

    # Duration bonus (per 30-min block, max 3)
    try:
        tz = ZoneInfo(config["calendar"]["default_timezone"])
        start = _parse_dt(event["start"], tz)
        end = _parse_dt(event["end"], tz)
        duration_minutes = (end - start).total_seconds() / 60
        duration_bonus = min(int(duration_minutes // 30), 3)
    except (KeyError, ValueError):
        duration_bonus = 0

    total = base_score + attendee_bonus + duration_bonus
    logger.debug("Priority score for '%s': %d (base=%d, att=%d, dur=%d)",
                 event.get("title", "?"), total, base_score, attendee_bonus, duration_bonus)
    return total


def generate_daily_agenda(events: list[dict], date: Optional[str] = None, timezone: Optional[str] = None) -> list[dict]:
    """Filter and sort events for a given date, returning them as an ordered agenda.

    Parameters
    ----------
    events : full list of events.
    date : ISO date string (YYYY-MM-DD). Defaults to today.
    timezone : IANA timezone name.

    Returns
    -------
    List of events for that day, sorted by start time, with a 'priority_score' field added.
    """
    config = get_config()
    tz_name = timezone or config["calendar"]["default_timezone"]
    tz = ZoneInfo(tz_name)

    if date is None:
        target_date = datetime.now(tz).date()
    else:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()

    logger.info("Generating agenda for %s (tz=%s)", target_date.isoformat(), tz_name)

    agenda: list[dict] = []
    for ev in events:
        try:
            start = _parse_dt(ev["start"], tz)
            if start.date() == target_date:
                enriched = {**ev, "priority_score": score_priority(ev)}
                agenda.append(enriched)
        except (KeyError, ValueError) as exc:
            logger.warning("Skipping event: %s – %s", ev, exc)

    agenda.sort(key=lambda e: _parse_dt(e["start"], tz))
    logger.info("Agenda contains %d event(s)", len(agenda))
    return agenda


def convert_timezone(events: list[dict], from_tz: str, to_tz: str) -> list[dict]:
    """Convert event start/end times from one timezone to another.

    Returns new event dicts with converted times (ISO format strings).
    """
    src = ZoneInfo(from_tz)
    dst = ZoneInfo(to_tz)
    converted: list[dict] = []
    for ev in events:
        try:
            start = _parse_dt(ev["start"], src).astimezone(dst)
            end = _parse_dt(ev["end"], src).astimezone(dst)
            converted.append({
                **ev,
                "start": start.strftime("%Y-%m-%dT%H:%M:%S"),
                "end": end.strftime("%Y-%m-%dT%H:%M:%S"),
                "timezone": to_tz,
            })
        except (KeyError, ValueError) as exc:
            logger.warning("Skipping event during tz conversion: %s – %s", ev, exc)
    return converted
