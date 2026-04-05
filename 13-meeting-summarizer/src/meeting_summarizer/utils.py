"""Utility helpers for Meeting Summarizer."""

import logging
import os
import sys

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_llm_client():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
    from common.llm_client import chat, generate, check_ollama_running
    return chat, generate, check_ollama_running


def read_transcript(file_path: str) -> str:
    """Read a meeting transcript from a text file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Transcript file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        raise ValueError("Transcript file is empty or contains only whitespace.")

    return content


def preprocess_transcript(transcript: str, max_length: int = 15000) -> str:
    """Preprocess and truncate transcript if needed."""
    transcript = transcript.strip()
    if len(transcript) > max_length:
        logger.info("Truncating transcript from %d to %d chars", len(transcript), max_length)
        transcript = transcript[:max_length] + "\n\n[...transcript truncated...]"
    return transcript


def parse_action_items(summary: str) -> list[dict]:
    """Parse action items from the structured summary."""
    action_items = []
    in_action_section = False

    for line in summary.split("\n"):
        stripped = line.strip()
        if "## ACTION ITEMS" in stripped:
            in_action_section = True
            continue
        if in_action_section and stripped.startswith("## "):
            break
        if in_action_section and "|" in stripped:
            parts = [p.strip() for p in stripped.split("|")]
            parts = [p for p in parts if p]
            if len(parts) >= 3 and parts[0] not in ("Who", "---", "-----"):
                if not all(c in "-" for c in parts[0]):
                    action_items.append({"who": parts[0], "what": parts[1], "when": parts[2]})

    return action_items


def extract_section(summary: str, section_name: str) -> str:
    """Extract a specific section's content from the structured summary."""
    lines = summary.split("\n")
    section_lines = []
    in_section = False

    for line in lines:
        stripped = line.strip()
        if f"## {section_name}" in stripped:
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section:
            section_lines.append(line)

    content = "\n".join(section_lines).strip()
    return content if content else "Not mentioned"
