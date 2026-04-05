"""
Tests for differential_diagnosis.core module.
"""

import pytest
from unittest.mock import patch, MagicMock
from differential_diagnosis.core import (
    DISCLAIMER,
    SYSTEM_PROMPT,
    BODY_SYSTEMS,
    URGENCY_KEYWORDS,
    URGENCY_LABELS,
    assess_urgency,
    get_affected_systems,
    generate_differential,
    rank_diagnoses,
    get_workup_recommendations,
    compare_diagnoses,
    display_disclaimer,
    load_config,
    DiagnosisSession,
)


# -----------------------------------------------------------------------
# Disclaimer tests
# -----------------------------------------------------------------------

class TestDisclaimer:
    def test_disclaimer_not_empty(self):
        assert DISCLAIMER is not None
        assert len(DISCLAIMER) > 0

    def test_disclaimer_contains_warning(self):
        assert "EDUCATIONAL" in DISCLAIMER
        assert "NOT" in DISCLAIMER
        assert "DISCLAIMER" in DISCLAIMER

    def test_disclaimer_mentions_emergency(self):
        assert "911" in DISCLAIMER or "emergency" in DISCLAIMER.lower()


# -----------------------------------------------------------------------
# Generate differential tests
# -----------------------------------------------------------------------

class TestGenerateDifferential:
    @patch("differential_diagnosis.core.chat")
    def test_returns_string(self, mock_chat):
        mock_chat.return_value = "1. Acute MI\n2. Unstable angina\n3. PE"
        result = generate_differential("chest pain, diaphoresis")
        assert isinstance(result, str)
        assert len(result) > 0

    @patch("differential_diagnosis.core.chat")
    def test_calls_chat(self, mock_chat):
        mock_chat.return_value = "Response"
        generate_differential("headache, fever")
        mock_chat.assert_called_once()

    @patch("differential_diagnosis.core.chat")
    def test_includes_system_prompt(self, mock_chat):
        mock_chat.return_value = "Response"
        generate_differential("cough, dyspnea")
        messages = mock_chat.call_args[0][0]
        assert messages[0]["role"] == "system"

    @patch("differential_diagnosis.core.chat")
    def test_passes_conversation_history(self, mock_chat):
        mock_chat.return_value = "Response"
        history = [{"role": "user", "content": "previous question"}]
        generate_differential("abdominal pain", conversation_history=history)
        call_args = mock_chat.call_args[0][0]
        assert any(m["content"] == "previous question" for m in call_args)

    @patch("differential_diagnosis.core.chat")
    def test_raises_on_error(self, mock_chat):
        mock_chat.side_effect = ConnectionError("Ollama down")
        with pytest.raises(ConnectionError):
            generate_differential("test symptoms")


# -----------------------------------------------------------------------
# Rank diagnoses tests
# -----------------------------------------------------------------------

class TestRankDiagnoses:
    @patch("differential_diagnosis.core.chat")
    def test_returns_string(self, mock_chat):
        mock_chat.return_value = "1. Diagnosis A (most likely)\n2. Diagnosis B"
        result = rank_diagnoses("Diagnosis A, Diagnosis B, Diagnosis C")
        assert isinstance(result, str)
        assert len(result) > 0

    @patch("differential_diagnosis.core.chat")
    def test_calls_chat(self, mock_chat):
        mock_chat.return_value = "Re-ranked list"
        rank_diagnoses("PE, DVT, Pneumonia")
        mock_chat.assert_called_once()


# -----------------------------------------------------------------------
# Workup recommendations tests
# -----------------------------------------------------------------------

class TestWorkupRecommendations:
    @patch("differential_diagnosis.core.chat")
    def test_returns_string(self, mock_chat):
        mock_chat.return_value = "Order troponin, ECG, CXR"
        result = get_workup_recommendations("Acute myocardial infarction")
        assert isinstance(result, str)
        assert len(result) > 0

    @patch("differential_diagnosis.core.chat")
    def test_calls_chat(self, mock_chat):
        mock_chat.return_value = "Workup response"
        get_workup_recommendations("Pulmonary embolism")
        mock_chat.assert_called_once()


# -----------------------------------------------------------------------
# Diagnosis session tests
# -----------------------------------------------------------------------

class TestDiagnosisSession:
    def test_empty_session(self):
        session = DiagnosisSession()
        assert session.get_history() == []
        summary = session.get_summary()
        assert summary["total_consultations"] == 0

    def test_add_entry(self):
        session = DiagnosisSession()
        session.add_entry("chest pain", "45M, smoker", "BP 160/95", 4, ["cardiovascular"], "Likely ACS")
        history = session.get_history()
        assert len(history) == 1
        assert history[0]["symptoms"] == "chest pain"
        assert history[0]["urgency"] == 4

    def test_multiple_entries(self):
        session = DiagnosisSession()
        session.add_entry("headache", "", "", 2, ["neurological"], "Tension headache likely")
        session.add_entry("chest pain", "45M", "tachycardia", 5, ["cardiovascular"], "ACS workup")
        assert len(session.get_history()) == 2

    def test_summary(self):
        session = DiagnosisSession()
        session.add_entry("headache", "", "", 2, ["neurological"], "Tension HA")
        session.add_entry("abdominal pain", "30F", "RLQ tender", 3, ["gastrointestinal"], "r/o appy")

        summary = session.get_summary()
        assert summary["total_consultations"] == 2
        assert summary["max_urgency"] == 3
        assert "neurological" in summary["systems_involved"]
        assert "gastrointestinal" in summary["systems_involved"]


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
# Additional tests for completeness
# -----------------------------------------------------------------------

class TestUrgencyAssessment:
    def test_emergency_level(self):
        level, label, advice = assess_urgency("chest pain and difficulty breathing")
        assert level == 5
        assert "Emergency" in label

    def test_low_level_default(self):
        level, label, advice = assess_urgency("feeling slightly off today")
        assert level == 1

    def test_returns_tuple_of_three(self):
        result = assess_urgency("headache")
        assert isinstance(result, tuple)
        assert len(result) == 3


class TestAffectedSystems:
    def test_cardiovascular(self):
        systems = get_affected_systems("chest pain and palpitations")
        assert "cardiovascular" in systems

    def test_unknown_defaults_to_general(self):
        systems = get_affected_systems("xyz completely unrelated")
        assert "general" in systems


class TestCompareDiagnoses:
    @patch("differential_diagnosis.core.chat")
    def test_returns_string(self, mock_chat):
        mock_chat.return_value = "PE is more likely because..."
        result = compare_diagnoses("PE", "Pneumothorax", "sudden dyspnea")
        assert isinstance(result, str)

    @patch("differential_diagnosis.core.chat")
    def test_calls_chat(self, mock_chat):
        mock_chat.return_value = "Comparison"
        compare_diagnoses("GERD", "PUD")
        mock_chat.assert_called_once()


class TestDisplayDisclaimer:
    @patch("rich.console.Console")
    def test_display_disclaimer_calls_print(self, mock_console_cls):
        mock_console = MagicMock()
        mock_console_cls.return_value = mock_console
        display_disclaimer()
        mock_console.print.assert_called_once()
