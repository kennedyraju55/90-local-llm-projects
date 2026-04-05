"""
Tests for patient_intake_summarizer.core module.
"""

import pytest
from unittest.mock import patch, MagicMock
from patient_intake_summarizer.core import (
    DISCLAIMER,
    SYSTEM_PROMPT,
    INTAKE_CATEGORIES,
    summarize_intake,
    extract_medical_history,
    generate_pre_visit_summary,
    identify_risk_factors,
    flag_missing_info,
    display_disclaimer,
    IntakeSession,
)
from patient_intake_summarizer.config import load_config


# -----------------------------------------------------------------------
# Disclaimer tests
# -----------------------------------------------------------------------

class TestDisclaimer:
    def test_disclaimer_not_empty(self):
        assert DISCLAIMER is not None
        assert len(DISCLAIMER) > 0

    def test_disclaimer_contains_warning(self):
        assert "DISCLAIMER" in DISCLAIMER
        assert "physician" in DISCLAIMER.lower()
        assert "NOT" in DISCLAIMER

    def test_disclaimer_mentions_hipaa(self):
        assert "HIPAA" in DISCLAIMER or "locally" in DISCLAIMER.lower()


# -----------------------------------------------------------------------
# Intake categories tests
# -----------------------------------------------------------------------

class TestIntakeCategories:
    def test_all_categories_present(self):
        expected = {
            "demographics", "chief_complaint", "medical_history",
            "surgical_history", "medications", "allergies",
            "family_history", "social_history", "review_of_systems",
        }
        assert set(INTAKE_CATEGORIES.keys()) == expected

    def test_each_category_has_description(self):
        for key, desc in INTAKE_CATEGORIES.items():
            assert isinstance(desc, str), f"Category '{key}' has non-string description"
            assert len(desc) > 0, f"Category '{key}' has empty description"

    def test_categories_are_strings(self):
        for key in INTAKE_CATEGORIES:
            assert isinstance(key, str)


# -----------------------------------------------------------------------
# Summarize intake tests
# -----------------------------------------------------------------------

class TestSummarizeIntake:
    @patch("patient_intake_summarizer.core.chat")
    def test_summarize_returns_string(self, mock_chat):
        mock_chat.return_value = "Patient is a 52-year-old female presenting with lower back pain."
        result = summarize_intake("Patient: Jane Doe, 52F, back pain")
        assert isinstance(result, str)
        assert len(result) > 0

    @patch("patient_intake_summarizer.core.chat")
    def test_summarize_calls_chat(self, mock_chat):
        mock_chat.return_value = "Summary response"
        summarize_intake("intake text")
        mock_chat.assert_called_once()

    @patch("patient_intake_summarizer.core.chat")
    def test_summarize_includes_system_prompt(self, mock_chat):
        mock_chat.return_value = "Summary"
        summarize_intake("test intake")
        messages = mock_chat.call_args[0][0]
        assert messages[0]["role"] == "system"

    @patch("patient_intake_summarizer.core.chat")
    def test_summarize_raises_on_error(self, mock_chat):
        mock_chat.side_effect = ConnectionError("Ollama down")
        with pytest.raises(ConnectionError):
            summarize_intake("test")


# -----------------------------------------------------------------------
# Extract medical history tests
# -----------------------------------------------------------------------

class TestExtractHistory:
    @patch("patient_intake_summarizer.core.chat")
    def test_extract_returns_dict(self, mock_chat):
        mock_chat.return_value = '{"demographics": "Jane Doe, 52F", "chief_complaint": "back pain"}'
        result = extract_medical_history("Patient: Jane Doe, 52F, back pain")
        assert isinstance(result, dict)

    @patch("patient_intake_summarizer.core.chat")
    def test_extract_calls_chat(self, mock_chat):
        mock_chat.return_value = '{"demographics": "test"}'
        extract_medical_history("test intake")
        mock_chat.assert_called_once()


# -----------------------------------------------------------------------
# Risk factors tests
# -----------------------------------------------------------------------

class TestRiskFactors:
    @patch("patient_intake_summarizer.core.chat")
    def test_risk_factors_returns_list(self, mock_chat):
        mock_chat.return_value = '["Family history of cardiac disease", "Sedentary lifestyle"]'
        result = identify_risk_factors("Father had MI at 60, patient is sedentary")
        assert isinstance(result, list)

    @patch("patient_intake_summarizer.core.chat")
    def test_risk_factors_calls_chat(self, mock_chat):
        mock_chat.return_value = '["Risk 1"]'
        identify_risk_factors("test intake")
        mock_chat.assert_called_once()


# -----------------------------------------------------------------------
# Intake session tests
# -----------------------------------------------------------------------

class TestIntakeSession:
    def test_empty_session(self):
        session = IntakeSession()
        assert session.get_summaries() == []
        summary = session.get_summary()
        assert summary["total_summaries"] == 0

    def test_add_summary(self):
        session = IntakeSession()
        session.add_summary("intake text", "summary text", "structured", ["demographics"])
        summaries = session.get_summaries()
        assert len(summaries) == 1
        assert summaries[0]["intake_text"] == "intake text"
        assert summaries[0]["summary"] == "summary text"

    def test_multiple_summaries(self):
        session = IntakeSession()
        session.add_summary("intake 1", "summary 1", "brief")
        session.add_summary("intake 2", "summary 2", "detailed")
        assert len(session.get_summaries()) == 2

    def test_session_summary(self):
        session = IntakeSession()
        session.add_summary("intake 1", "summary 1", "brief", ["demographics"])
        session.add_summary("intake 2", "summary 2", "detailed", ["medications", "allergies"])

        summary = session.get_summary()
        assert summary["total_summaries"] == 2
        assert "brief" in summary["formats_used"]
        assert "detailed" in summary["formats_used"]
        assert "demographics" in summary["all_focus_areas"]
        assert "medications" in summary["all_focus_areas"]


# -----------------------------------------------------------------------
# Config tests
# -----------------------------------------------------------------------

class TestConfig:
    def test_load_config_returns_dict(self):
        config = load_config()
        assert isinstance(config, dict)

    def test_default_model(self):
        config = load_config()
        assert "model" in config


# -----------------------------------------------------------------------
# Display disclaimer tests
# -----------------------------------------------------------------------

class TestDisplayDisclaimer:
    @patch("rich.console.Console")
    def test_display_disclaimer_calls_print(self, mock_console_cls):
        mock_console = MagicMock()
        mock_console_cls.return_value = mock_console
        display_disclaimer()
        mock_console.print.assert_called_once()
