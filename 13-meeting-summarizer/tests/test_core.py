"""Tests for Meeting Summarizer core logic."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock

from src.meeting_summarizer.core import summarize_meeting, save_summary
from src.meeting_summarizer.utils import (
    read_transcript, preprocess_transcript, parse_action_items, extract_section,
)
from src.meeting_summarizer.config import load_config

SAMPLE_TRANSCRIPT = """Meeting: Weekly Team Sync
Attendees: Alice (PM), Bob (Dev), Carol (Design)
Alice: Let's discuss the Q1 roadmap.
Bob: I've drafted the technical spec.
Alice: Great. We'll go with Option B for the pricing page.
Bob: I'll update documentation by next Wednesday.
"""

SAMPLE_LLM_RESPONSE = """## ATTENDEES
- Alice (PM)
- Bob (Dev)
- Carol (Design)

## AGENDA TOPICS
- Q1 roadmap

## KEY DECISIONS
- Go with Option B for the pricing page

## ACTION ITEMS
| Who | What | When |
|-----|------|------|
| Bob | Share technical spec | Friday |
| Bob | Update documentation | Next Wednesday |

## FOLLOW-UPS
- Carol to schedule a design review

## SUMMARY
The team discussed the Q1 roadmap and decided on Option B for pricing.
"""


class TestReadTranscript:
    def test_read_valid_file(self, tmp_path):
        f = tmp_path / "meeting.txt"
        f.write_text("Hello meeting.", encoding="utf-8")
        assert read_transcript(str(f)) == "Hello meeting."

    def test_read_missing_file(self):
        with pytest.raises(FileNotFoundError):
            read_transcript("nonexistent.txt")

    def test_read_empty_file(self, tmp_path):
        f = tmp_path / "empty.txt"
        f.write_text("", encoding="utf-8")
        with pytest.raises(ValueError):
            read_transcript(str(f))


class TestPreprocessTranscript:
    def test_short_unchanged(self):
        assert preprocess_transcript("short text") == "short text"

    def test_long_truncated(self):
        result = preprocess_transcript("x" * 20000, 15000)
        assert "[...transcript truncated...]" in result


class TestParseActionItems:
    def test_parse_valid(self):
        items = parse_action_items(SAMPLE_LLM_RESPONSE)
        assert len(items) == 2
        assert items[0]["who"] == "Bob"

    def test_parse_empty(self):
        assert parse_action_items("## SUMMARY\nDone.") == []


class TestExtractSection:
    def test_extract_attendees(self):
        result = extract_section(SAMPLE_LLM_RESPONSE, "ATTENDEES")
        assert "Alice (PM)" in result

    def test_extract_missing(self):
        assert extract_section(SAMPLE_LLM_RESPONSE, "NONEXISTENT") == "Not mentioned"


class TestSummarizeMeeting:
    @patch("src.meeting_summarizer.core.get_llm_client")
    def test_summarize_calls_llm(self, mock_get):
        mock_chat = MagicMock(return_value=SAMPLE_LLM_RESPONSE)
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        result = summarize_meeting(SAMPLE_TRANSCRIPT)
        assert "ATTENDEES" in result
        mock_chat.assert_called_once()


class TestSaveSummary:
    def test_save_creates_file(self, tmp_path):
        output = tmp_path / "output.md"
        save_summary(SAMPLE_LLM_RESPONSE, str(output))
        assert output.exists()
        assert "ATTENDEES" in output.read_text()


class TestConfig:
    def test_default_config(self):
        config = load_config()
        assert config["llm"]["model"] == "gemma4"

    @patch.dict(os.environ, {"MEETING_SUMMARIZER_MODEL": "llama3"})
    def test_env_override(self):
        assert load_config()["llm"]["model"] == "llama3"
