"""Tests for Deposition Summarizer core logic."""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock

from src.deposition_summarizer.core import (
    _parse_json_response,
    summarize_deposition,
    find_admissions,
    find_contradictions,
    extract_testimony,
    generate_follow_up_questions,
    build_timeline,
    get_significance_color,
    get_significance_emoji,
    KeyAdmission,
    Contradiction,
    ImportantTestimony,
    WitnessProfile,
    DepositionSummary,
    SAMPLE_TRANSCRIPT,
    LEGAL_DISCLAIMER,
)
from src.deposition_summarizer.config import load_config, DEFAULT_CONFIG


# ---------------------------------------------------------------------------
# Sample mock responses
# ---------------------------------------------------------------------------

MOCK_SUMMARY_JSON = json.dumps({
    "title": "Deposition of John Smith",
    "witness": "John Smith",
    "date": "March 15, 2024",
    "duration": "3 hours",
    "overall_summary": "John Smith testified about the equipment failure at Westfield Manufacturing.",
    "key_admissions": [
        {
            "speaker": "John Smith",
            "statement": "I did not file a formal work order that day.",
            "page_line": "p.4, ln.5",
            "significance": "high",
        }
    ],
    "contradictions": [
        {
            "statement_a": "Everything appeared to be operating normally.",
            "statement_b": "The safety valve on unit 4B seemed a bit worn.",
            "page_line_a": "p.2, ln.10",
            "page_line_b": "p.3, ln.5",
            "explanation": "Witness first said everything was normal, then admitted noticing worn valve.",
        }
    ],
    "important_testimony": [
        {
            "speaker": "John Smith",
            "topic": "Safety valve condition",
            "summary": "Admitted the safety valve appeared worn but did not file a work order.",
            "page_line": "p.3, ln.5-10",
            "relevance": "critical",
        }
    ],
    "witness_profile": {
        "name": "John Smith",
        "role": "Director of Operations",
        "credibility_notes": ["Evasive on documentation questions"],
        "demeanor_notes": ["Became defensive when pressed on safety policies"],
    },
    "topics_covered": ["safety valve", "pressure gauges", "maintenance documentation"],
    "follow_up_questions": [
        "Why wasn't the work order filed within 24 hours as required?",
        "Were there other equipment concerns you did not document?",
    ],
    "timeline": [
        {"date": "January 2020", "event": "Smith started as Director of Operations"},
        {"date": "September 14, 2023, 2 PM", "event": "Walkthrough of Line 4"},
        {"date": "September 14, 2023, 11:45 PM", "event": "Notified of equipment failure"},
    ],
})

MOCK_ADMISSIONS_JSON = json.dumps([
    {
        "speaker": "John Smith",
        "statement": "No, I did not file a formal work order that day.",
        "page_line": "p.4, ln.5",
        "significance": "high",
    },
    {
        "speaker": "John Smith",
        "statement": "We often handle minor issues informally.",
        "page_line": "p.3, ln.20",
        "significance": "medium",
    },
])

MOCK_CONTRADICTIONS_JSON = json.dumps([
    {
        "statement_a": "Everything appeared to be operating normally.",
        "statement_b": "The safety valve seemed a bit worn.",
        "page_line_a": "p.2",
        "page_line_b": "p.3",
        "explanation": "Claims normal operation but admits defect.",
    }
])

MOCK_TESTIMONY_JSON = json.dumps([
    {
        "speaker": "John Smith",
        "topic": "pressure",
        "summary": "Pressure gauges were within 150-200 PSI range at 2 PM.",
        "page_line": "p.2, ln.20",
        "relevance": "high",
    }
])

MOCK_QUESTIONS_JSON = json.dumps([
    "Why was the work order not filed?",
    "Who else knew about the worn valve?",
    "Were pressure readings logged automatically?",
])

MOCK_TIMELINE_JSON = json.dumps([
    {"date": "January 2020", "event": "Smith became Director of Operations"},
    {"date": "September 14, 2023", "event": "Equipment failure on Line 4"},
])


# ---------------------------------------------------------------------------
# Tests for _parse_json_response
# ---------------------------------------------------------------------------

class TestParseJsonResponse:
    """Tests for the JSON parsing helper."""

    def test_valid_json(self):
        data = _parse_json_response('{"key": "value"}')
        assert data == {"key": "value"}

    def test_valid_json_array(self):
        data = _parse_json_response('[1, 2, 3]')
        assert data == [1, 2, 3]

    def test_json_in_code_block(self):
        text = '```json\n{"key": "value"}\n```'
        data = _parse_json_response(text)
        assert data == {"key": "value"}

    def test_json_in_plain_code_block(self):
        text = 'Here is the result:\n```\n[1, 2, 3]\n```\nDone.'
        data = _parse_json_response(text)
        assert data == [1, 2, 3]

    def test_json_embedded_in_text(self):
        text = 'Here is the analysis:\n{"key": "value"}\nEnd of analysis.'
        data = _parse_json_response(text)
        assert data == {"key": "value"}

    def test_invalid_json_raises(self):
        with pytest.raises(ValueError, match="Could not parse JSON"):
            _parse_json_response("This is not JSON at all")

    def test_empty_string_raises(self):
        with pytest.raises(ValueError):
            _parse_json_response("")


# ---------------------------------------------------------------------------
# Tests for summarize_deposition
# ---------------------------------------------------------------------------

class TestSummarizeDeposition:
    """Tests for full deposition summary."""

    @patch("src.deposition_summarizer.core.chat")
    def test_summarize_returns_summary_object(self, mock_chat):
        mock_chat.return_value = MOCK_SUMMARY_JSON
        result = summarize_deposition("some transcript text")

        assert isinstance(result, DepositionSummary)
        assert result.witness == "John Smith"
        assert result.title == "Deposition of John Smith"
        assert len(result.key_admissions) == 1
        assert len(result.contradictions) == 1
        assert len(result.important_testimony) == 1
        assert len(result.timeline) == 3
        mock_chat.assert_called_once()

    @patch("src.deposition_summarizer.core.chat")
    def test_summarize_handles_unparseable_response(self, mock_chat):
        mock_chat.return_value = "This is just a plain text summary with no JSON."
        result = summarize_deposition("transcript")

        assert isinstance(result, DepositionSummary)
        assert "plain text summary" in result.overall_summary

    @patch("src.deposition_summarizer.core.chat")
    def test_summarize_passes_model(self, mock_chat):
        mock_chat.return_value = MOCK_SUMMARY_JSON
        summarize_deposition("transcript", model="custom-model")

        call_kwargs = mock_chat.call_args
        assert call_kwargs.kwargs["model"] == "custom-model"


# ---------------------------------------------------------------------------
# Tests for find_admissions
# ---------------------------------------------------------------------------

class TestFindAdmissions:
    """Tests for admission extraction."""

    @patch("src.deposition_summarizer.core.chat")
    def test_find_admissions_returns_list(self, mock_chat):
        mock_chat.return_value = MOCK_ADMISSIONS_JSON
        results = find_admissions("transcript text")

        assert len(results) == 2
        assert isinstance(results[0], KeyAdmission)
        assert results[0].speaker == "John Smith"
        assert results[0].significance == "high"

    @patch("src.deposition_summarizer.core.chat")
    def test_find_admissions_handles_empty(self, mock_chat):
        mock_chat.return_value = "[]"
        results = find_admissions("transcript")
        assert results == []

    @patch("src.deposition_summarizer.core.chat")
    def test_find_admissions_handles_bad_json(self, mock_chat):
        mock_chat.return_value = "No admissions found in this transcript."
        results = find_admissions("transcript")
        assert results == []


# ---------------------------------------------------------------------------
# Tests for find_contradictions
# ---------------------------------------------------------------------------

class TestFindContradictions:
    """Tests for contradiction detection."""

    @patch("src.deposition_summarizer.core.chat")
    def test_find_contradictions_returns_list(self, mock_chat):
        mock_chat.return_value = MOCK_CONTRADICTIONS_JSON
        results = find_contradictions("transcript text")

        assert len(results) == 1
        assert isinstance(results[0], Contradiction)
        assert "normally" in results[0].statement_a

    @patch("src.deposition_summarizer.core.chat")
    def test_find_contradictions_handles_wrapped_json(self, mock_chat):
        wrapped = json.dumps({"contradictions": json.loads(MOCK_CONTRADICTIONS_JSON)})
        mock_chat.return_value = wrapped
        results = find_contradictions("transcript")
        assert len(results) == 1


# ---------------------------------------------------------------------------
# Tests for extract_testimony
# ---------------------------------------------------------------------------

class TestExtractTestimony:
    """Tests for testimony extraction."""

    @patch("src.deposition_summarizer.core.chat")
    def test_extract_testimony_returns_list(self, mock_chat):
        mock_chat.return_value = MOCK_TESTIMONY_JSON
        results = extract_testimony("transcript", "pressure")

        assert len(results) == 1
        assert isinstance(results[0], ImportantTestimony)
        assert results[0].topic == "pressure"

    @patch("src.deposition_summarizer.core.chat")
    def test_extract_testimony_handles_no_results(self, mock_chat):
        mock_chat.return_value = "[]"
        results = extract_testimony("transcript", "unrelated topic")
        assert results == []


# ---------------------------------------------------------------------------
# Tests for generate_follow_up_questions
# ---------------------------------------------------------------------------

class TestGenerateFollowUpQuestions:
    """Tests for follow-up question generation."""

    @patch("src.deposition_summarizer.core.chat")
    def test_returns_list_of_strings(self, mock_chat):
        mock_chat.return_value = MOCK_QUESTIONS_JSON
        results = generate_follow_up_questions("transcript")

        assert len(results) == 3
        assert all(isinstance(q, str) for q in results)
        assert "work order" in results[0].lower()

    @patch("src.deposition_summarizer.core.chat")
    def test_handles_bad_response(self, mock_chat):
        mock_chat.return_value = "I cannot generate questions."
        results = generate_follow_up_questions("transcript")
        assert results == []


# ---------------------------------------------------------------------------
# Tests for build_timeline
# ---------------------------------------------------------------------------

class TestBuildTimeline:
    """Tests for timeline extraction."""

    @patch("src.deposition_summarizer.core.chat")
    def test_build_timeline_returns_list(self, mock_chat):
        mock_chat.return_value = MOCK_TIMELINE_JSON
        results = build_timeline("transcript")

        assert len(results) == 2
        assert "date" in results[0]
        assert "event" in results[0]

    @patch("src.deposition_summarizer.core.chat")
    def test_build_timeline_handles_empty(self, mock_chat):
        mock_chat.return_value = "[]"
        results = build_timeline("transcript")
        assert results == []


# ---------------------------------------------------------------------------
# Tests for data structures
# ---------------------------------------------------------------------------

class TestDataStructures:
    """Tests for dataclass defaults and creation."""

    def test_key_admission_defaults(self):
        adm = KeyAdmission(speaker="Test", statement="I admit it")
        assert adm.page_line == ""
        assert adm.significance == "medium"

    def test_contradiction_defaults(self):
        con = Contradiction(statement_a="A", statement_b="B")
        assert con.page_line_a == ""
        assert con.explanation == ""

    def test_important_testimony_defaults(self):
        t = ImportantTestimony(speaker="Witness", topic="Topic", summary="Summary")
        assert t.relevance == "medium"
        assert t.page_line == ""

    def test_witness_profile_defaults(self):
        wp = WitnessProfile()
        assert wp.name == ""
        assert wp.credibility_notes == []
        assert wp.demeanor_notes == []

    def test_deposition_summary_defaults(self):
        ds = DepositionSummary()
        assert ds.title == ""
        assert ds.key_admissions == []
        assert ds.contradictions == []
        assert ds.timeline == []
        assert isinstance(ds.witness_profile, WitnessProfile)

    def test_deposition_summary_with_data(self):
        adm = KeyAdmission(speaker="W", statement="S", significance="high")
        ds = DepositionSummary(title="Test", key_admissions=[adm])
        assert len(ds.key_admissions) == 1
        assert ds.key_admissions[0].significance == "high"


# ---------------------------------------------------------------------------
# Tests for sample transcript and display helpers
# ---------------------------------------------------------------------------

class TestSampleAndHelpers:
    """Tests for SAMPLE_TRANSCRIPT and display helpers."""

    def test_sample_transcript_exists(self):
        assert SAMPLE_TRANSCRIPT is not None
        assert len(SAMPLE_TRANSCRIPT) > 100
        assert "DEPOSITION" in SAMPLE_TRANSCRIPT

    def test_legal_disclaimer_exists(self):
        assert LEGAL_DISCLAIMER is not None
        assert "DISCLAIMER" in LEGAL_DISCLAIMER

    def test_get_significance_color(self):
        assert get_significance_color("low") == "green"
        assert get_significance_color("medium") == "yellow"
        assert get_significance_color("high") == "red"
        assert get_significance_color("critical") == "bold red"
        assert get_significance_color("unknown") == "white"

    def test_get_significance_emoji(self):
        assert get_significance_emoji("low") == "🟢"
        assert get_significance_emoji("medium") == "🟡"
        assert get_significance_emoji("high") == "🔴"
        assert get_significance_emoji("critical") == "🚨"
        assert get_significance_emoji("unknown") == "⚪"


# ---------------------------------------------------------------------------
# Tests for configuration
# ---------------------------------------------------------------------------

class TestConfig:
    """Tests for configuration management."""

    def test_default_config_loaded(self):
        config = load_config()
        assert config["llm"]["model"] == "gemma4:latest"
        assert config["llm"]["temperature"] == 0.3
        assert config["llm"]["max_tokens"] == 4096

    def test_config_from_yaml(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("llm:\n  temperature: 0.5\n", encoding="utf-8")
        config = load_config(str(config_file))
        assert config["llm"]["temperature"] == 0.5

    @patch.dict(os.environ, {"DEPOSITION_SUMMARIZER_MODEL": "llama3"})
    def test_env_override_model(self):
        config = load_config()
        assert config["llm"]["model"] == "llama3"

    @patch.dict(os.environ, {"DEPOSITION_SUMMARIZER_TEMPERATURE": "0.9"})
    def test_env_override_temperature(self):
        config = load_config()
        assert config["llm"]["temperature"] == 0.9

    def test_default_config_has_all_keys(self):
        assert "llm" in DEFAULT_CONFIG
        assert "analysis" in DEFAULT_CONFIG
        assert "logging" in DEFAULT_CONFIG
        assert "app" in DEFAULT_CONFIG
