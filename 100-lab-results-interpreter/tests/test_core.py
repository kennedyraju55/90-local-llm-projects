"""
Tests for Lab Results Interpreter - Core Module
"""

import os
import sys
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.lab_results_interpreter.core import (
    DISCLAIMER,
    SYSTEM_PROMPT,
    REFERENCE_RANGES,
    LAB_PANELS,
    interpret_results,
    identify_abnormalities,
    suggest_followup_tests,
    explain_lab_value,
    get_reference_range,
    display_disclaimer,
    LabSession,
)
from src.lab_results_interpreter.config import load_config, DEFAULT_CONFIG


# ═══════════════════════════════════════════════════════════════════
# TestDisclaimer
# ═══════════════════════════════════════════════════════════════════


class TestDisclaimer:
    """Tests for the medical disclaimer."""

    def test_disclaimer_exists(self):
        """Disclaimer constant should be defined and non-empty."""
        assert DISCLAIMER
        assert len(DISCLAIMER) > 50

    def test_disclaimer_contains_warning(self):
        """Disclaimer should contain key warning language."""
        assert "NOT a substitute" in DISCLAIMER
        assert "healthcare provider" in DISCLAIMER.lower()

    def test_display_disclaimer_returns_string(self):
        """display_disclaimer() should return the disclaimer text."""
        result = display_disclaimer()
        assert result == DISCLAIMER
        assert isinstance(result, str)


# ═══════════════════════════════════════════════════════════════════
# TestReferenceRanges
# ═══════════════════════════════════════════════════════════════════


class TestReferenceRanges:
    """Tests for reference range data."""

    def test_reference_ranges_structure(self):
        """Each panel should have tests with range, unit, description."""
        for panel_name, tests in REFERENCE_RANGES.items():
            assert isinstance(tests, dict), f"Panel {panel_name} should be a dict"
            for test_name, info in tests.items():
                assert "range" in info, f"{panel_name}/{test_name} missing 'range'"
                assert "unit" in info, f"{panel_name}/{test_name} missing 'unit'"
                assert "description" in info, f"{panel_name}/{test_name} missing 'description'"

    def test_cbc_panel_values(self):
        """CBC panel should have key blood count tests."""
        cbc = REFERENCE_RANGES["CBC"]
        assert "WBC" in cbc
        assert "RBC" in cbc
        assert "Hemoglobin" in cbc
        assert "Platelets" in cbc
        assert cbc["WBC"]["range"] == "4.5-11.0"

    def test_bmp_panel_values(self):
        """BMP panel should have key metabolic tests."""
        bmp = REFERENCE_RANGES["BMP"]
        assert "Glucose" in bmp
        assert "Creatinine" in bmp
        assert "Sodium" in bmp
        assert bmp["Glucose"]["unit"] == "mg/dL"

    def test_all_expected_panels_exist(self):
        """All expected panels should be present in REFERENCE_RANGES."""
        expected = ["CBC", "BMP", "Lipid Panel", "Liver Panel", "Thyroid", "Urinalysis"]
        for panel in expected:
            assert panel in REFERENCE_RANGES, f"Missing panel: {panel}"

    def test_get_reference_range_found(self):
        """get_reference_range should return data for known tests."""
        result = get_reference_range("CBC", "WBC")
        assert result["range"] == "4.5-11.0"
        assert result["unit"] == "x10^3/µL"

    def test_get_reference_range_not_found(self):
        """get_reference_range should return empty dict for unknown tests."""
        result = get_reference_range("CBC", "NonexistentTest")
        assert result == {}

    def test_get_reference_range_unknown_panel(self):
        """get_reference_range should return empty dict for unknown panel."""
        result = get_reference_range("UnknownPanel", "WBC")
        assert result == {}


# ═══════════════════════════════════════════════════════════════════
# TestInterpretResults
# ═══════════════════════════════════════════════════════════════════


class TestInterpretResults:
    """Tests for interpret_results function."""

    @patch("src.lab_results_interpreter.core.chat")
    def test_interpret_results_basic(self, mock_chat):
        """interpret_results should call chat and return response."""
        mock_chat.return_value = "Your hemoglobin is slightly low."
        result = interpret_results(lab_results_text="Hemoglobin: 11.0 g/dL")
        assert result == "Your hemoglobin is slightly low."
        mock_chat.assert_called_once()

    @patch("src.lab_results_interpreter.core.chat")
    def test_interpret_results_with_panel(self, mock_chat):
        """interpret_results should include panel context when specified."""
        mock_chat.return_value = "CBC analysis complete."
        result = interpret_results(
            lab_results_text="WBC: 12.5",
            panel_type="CBC",
        )
        assert result == "CBC analysis complete."
        call_args = mock_chat.call_args
        messages = call_args[1].get("messages") or call_args[0][0]
        prompt_text = messages[-1]["content"]
        assert "CBC" in prompt_text

    @patch("src.lab_results_interpreter.core.chat")
    def test_interpret_results_with_context(self, mock_chat):
        """interpret_results should include patient context."""
        mock_chat.return_value = "Given the patient's age..."
        result = interpret_results(
            lab_results_text="Glucose: 130 mg/dL",
            patient_context="65-year-old female, type 2 diabetes",
        )
        assert result == "Given the patient's age..."
        call_args = mock_chat.call_args
        messages = call_args[1].get("messages") or call_args[0][0]
        prompt_text = messages[-1]["content"]
        assert "65-year-old" in prompt_text


# ═══════════════════════════════════════════════════════════════════
# TestIdentifyAbnormalities
# ═══════════════════════════════════════════════════════════════════


class TestIdentifyAbnormalities:
    """Tests for identify_abnormalities function."""

    @patch("src.lab_results_interpreter.core.chat")
    def test_identify_abnormalities_basic(self, mock_chat):
        """identify_abnormalities should call chat and return response."""
        mock_chat.return_value = "WBC is elevated at 15.0."
        result = identify_abnormalities(lab_results_text="WBC: 15.0 x10^3/µL")
        assert "elevated" in result
        mock_chat.assert_called_once()

    @patch("src.lab_results_interpreter.core.chat")
    def test_identify_abnormalities_with_panel(self, mock_chat):
        """identify_abnormalities should include panel reference ranges."""
        mock_chat.return_value = "Multiple abnormalities detected."
        result = identify_abnormalities(
            lab_results_text="WBC: 15.0, RBC: 3.0",
            panel_type="CBC",
        )
        assert result == "Multiple abnormalities detected."


# ═══════════════════════════════════════════════════════════════════
# TestSuggestFollowup
# ═══════════════════════════════════════════════════════════════════


class TestSuggestFollowup:
    """Tests for suggest_followup_tests function."""

    @patch("src.lab_results_interpreter.core.chat")
    def test_suggest_followup_basic(self, mock_chat):
        """suggest_followup_tests should call chat and return response."""
        mock_chat.return_value = "Recommend iron studies and reticulocyte count."
        result = suggest_followup_tests(lab_results_text="Hemoglobin: 9.0 g/dL")
        assert "iron studies" in result.lower()
        mock_chat.assert_called_once()

    @patch("src.lab_results_interpreter.core.chat")
    def test_suggest_followup_with_context(self, mock_chat):
        """suggest_followup_tests should include clinical context."""
        mock_chat.return_value = "Given fatigue symptoms, recommend thyroid panel."
        result = suggest_followup_tests(
            lab_results_text="TSH: 8.5 mIU/L",
            clinical_context="Patient reports fatigue and weight gain",
        )
        assert "thyroid" in result.lower()


# ═══════════════════════════════════════════════════════════════════
# TestExplainLabValue
# ═══════════════════════════════════════════════════════════════════


class TestExplainLabValue:
    """Tests for explain_lab_value function."""

    @patch("src.lab_results_interpreter.core.chat")
    def test_explain_lab_value_basic(self, mock_chat):
        """explain_lab_value should call chat and return response."""
        mock_chat.return_value = "Hemoglobin carries oxygen in your blood."
        result = explain_lab_value(test_name="Hemoglobin", value="14.0", unit="g/dL")
        assert "hemoglobin" in result.lower()
        mock_chat.assert_called_once()

    @patch("src.lab_results_interpreter.core.chat")
    def test_explain_lab_value_without_unit(self, mock_chat):
        """explain_lab_value should work without a unit specified."""
        mock_chat.return_value = "pH measures the acidity of urine."
        result = explain_lab_value(test_name="pH", value="5.0")
        assert result == "pH measures the acidity of urine."


# ═══════════════════════════════════════════════════════════════════
# TestLabSession
# ═══════════════════════════════════════════════════════════════════


class TestLabSession:
    """Tests for the LabSession class."""

    def test_session_initialization(self):
        """New session should have empty history."""
        session = LabSession()
        assert session.get_history() == []
        assert session.conversation_history == []
        assert session.created_at

    def test_add_interpretation(self):
        """add_interpretation should store entries."""
        session = LabSession()
        session.add_interpretation(
            lab_results="WBC: 12.0",
            interpretation="WBC is slightly elevated.",
            panel_type="CBC",
            patient_context="30-year-old male",
        )
        history = session.get_history()
        assert len(history) == 1
        assert history[0]["panel_type"] == "CBC"
        assert history[0]["lab_results"] == "WBC: 12.0"

    def test_multiple_interpretations(self):
        """Session should track multiple interpretations."""
        session = LabSession()
        session.add_interpretation("WBC: 12.0", "Elevated WBC", "CBC")
        session.add_interpretation("Glucose: 130", "High glucose", "BMP")
        assert len(session.get_history()) == 2
        assert len(session.conversation_history) == 4  # 2 user + 2 assistant

    def test_get_summary(self):
        """get_summary should return formatted summary."""
        session = LabSession()
        session.add_interpretation("WBC: 12.0", "Elevated", "CBC")
        session.add_interpretation("Glucose: 130", "High", "BMP")
        summary = session.get_summary()
        assert "Total Interpretations: 2" in summary
        assert "Lab Session Summary" in summary

    def test_session_empty_summary(self):
        """Empty session should still produce a valid summary."""
        session = LabSession()
        summary = session.get_summary()
        assert "Total Interpretations: 0" in summary


# ═══════════════════════════════════════════════════════════════════
# TestConfig
# ═══════════════════════════════════════════════════════════════════


class TestConfig:
    """Tests for configuration loading."""

    def test_default_config_values(self):
        """Default config should have expected keys and values."""
        assert DEFAULT_CONFIG["model"] == "gemma4"
        assert DEFAULT_CONFIG["temperature"] == 0.3
        assert DEFAULT_CONFIG["max_tokens"] == 2048
        assert DEFAULT_CONFIG["log_level"] == "INFO"

    def test_load_config_returns_dict(self):
        """load_config should return a dictionary."""
        config = load_config()
        assert isinstance(config, dict)
        assert "model" in config
        assert "temperature" in config

    def test_load_config_nonexistent_file(self):
        """load_config should fall back to defaults for missing file."""
        config = load_config(config_path="/nonexistent/config.yaml")
        assert config["model"] == "gemma4"


# ═══════════════════════════════════════════════════════════════════
# TestLabPanels
# ═══════════════════════════════════════════════════════════════════


class TestLabPanels:
    """Tests for LAB_PANELS list."""

    def test_panels_list_not_empty(self):
        """LAB_PANELS should contain panel names."""
        assert len(LAB_PANELS) >= 10

    def test_panels_contains_expected(self):
        """LAB_PANELS should include common panels."""
        expected = ["CBC", "BMP", "CMP", "Lipid Panel", "Thyroid"]
        for panel in expected:
            assert panel in LAB_PANELS, f"Missing panel: {panel}"
