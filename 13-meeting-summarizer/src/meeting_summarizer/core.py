"""Core business logic for Meeting Summarizer."""

import logging
from typing import Any

from .config import load_config
from .utils import get_llm_client, preprocess_transcript, parse_action_items, extract_section

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are an expert meeting analyst. Your job is to analyze meeting transcripts
and extract structured information. Always respond in the exact format requested.
Be thorough but concise. If information is not available in the transcript, say "Not mentioned"."""

SUMMARY_PROMPT_TEMPLATE = """Analyze the following meeting transcript and extract a structured summary.

Respond in EXACTLY this format (keep the section headers exactly as shown):

## ATTENDEES
- Name (Role if mentioned)

## AGENDA TOPICS
- Topic 1
- Topic 2

## KEY DECISIONS
- Decision 1
- Decision 2

## ACTION ITEMS
| Who | What | When |
|-----|------|------|
| Person | Task description | Deadline or "TBD" |

## FOLLOW-UPS
- Follow-up item 1
- Follow-up item 2

## SUMMARY
A 2-3 sentence overall summary of the meeting.

---

MEETING TRANSCRIPT:
{transcript}"""

SPEAKER_IDENTIFICATION_PROMPT = """Analyze this meeting transcript and identify all speakers.
For each speaker, provide:
- Name (as used in transcript)
- Role (if identifiable)
- Number of times they spoke
- Key contributions/topics they discussed

Return as a structured list.

Transcript:
{transcript}"""

DECISION_LOG_PROMPT = """Extract a detailed decision log from this meeting transcript.
For each decision, provide:
- Decision number
- Description of the decision
- Who proposed it
- Who approved/agreed
- Any conditions or caveats
- Impact assessment (if discussed)

Transcript:
{transcript}"""

FOLLOWUP_PROMPT = """Analyze this meeting transcript and create a follow-up reminder schedule.
For each follow-up item, provide:
- Description
- Responsible person
- Suggested deadline
- Priority (High/Medium/Low)
- Dependencies (if any)

Transcript:
{transcript}"""


def summarize_meeting(transcript: str, config: dict | None = None) -> str:
    """Send the transcript to the LLM for analysis and summarization."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    max_length = cfg.get("processing", {}).get("max_transcript_length", 15000)
    processed = preprocess_transcript(transcript, max_length)
    prompt = SUMMARY_PROMPT_TEMPLATE.format(transcript=processed)

    messages = [{"role": "user", "content": prompt}]
    return chat(
        messages=messages,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )


def identify_speakers(transcript: str, config: dict | None = None) -> str:
    """Identify and profile speakers from the transcript."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    max_length = cfg.get("processing", {}).get("max_transcript_length", 15000)
    processed = preprocess_transcript(transcript, max_length)

    messages = [{"role": "user", "content": SPEAKER_IDENTIFICATION_PROMPT.format(transcript=processed)}]
    return chat(
        messages=messages,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )


def extract_decision_log(transcript: str, config: dict | None = None) -> str:
    """Extract a detailed decision log from the transcript."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    max_length = cfg.get("processing", {}).get("max_transcript_length", 15000)
    processed = preprocess_transcript(transcript, max_length)

    messages = [{"role": "user", "content": DECISION_LOG_PROMPT.format(transcript=processed)}]
    return chat(
        messages=messages,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )


def generate_followup_reminders(transcript: str, config: dict | None = None) -> str:
    """Generate follow-up reminders with priorities and deadlines."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    max_length = cfg.get("processing", {}).get("max_transcript_length", 15000)
    processed = preprocess_transcript(transcript, max_length)

    messages = [{"role": "user", "content": FOLLOWUP_PROMPT.format(transcript=processed)}]
    return chat(
        messages=messages,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )


def save_summary(summary: str, output_path: str) -> None:
    """Save the meeting summary to a file."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)
