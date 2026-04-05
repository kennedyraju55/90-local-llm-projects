"""
Tests for medical_report_writer.core module.
"""

import pytest
from unittest.mock import patch, MagicMock
from medical_report_writer.core import (
    DISCLAIMER,
    SYSTEM_PROMPT,
    REPORT_TYPES,
    generate_report,
    generate_discharge_summary,
    generate_referral_letter,
    format_report,
    extract_key_findings,
    display_disclaimer,
    ReportSession,
)
from medical_report_writer.config import load_config


# -----------------------------------------------------------------------
# Disclaimer tests
# -----------------------------------------------------------------------

class TestDisclaimer:
    def test_disclaimer_not_empty(self):
        assert DISCLAIMER is not None
        assert len(DISCLAIMER) > 0

    def test_disclaimer_contains_physician_review(self):
        assert "PHYSICIAN" in DISCLAIMER
        assert "reviewed" in DISCLAIMER.lower() or "REVIEW" in DISCLAIMER

    def test_disclaimer_mentions_hipaa(self):
        assert "HIPAA" in DISCLAIMER or "locally" in DISCLAIMER.lower()


# -----------------------------------------------------------------------
# Report types tests
# -----------------------------------------------------------------------

class TestReportTypes:
    def test_all_report_types_present(self):
        expected = {
            "discharge_summary", "referral_letter", "consultation_note",
            "operative_report", "progress_note", "transfer_summary",
        }
        assert set(REPORT_TYPES.keys()) == expected

    def test_each_type_has_required_fields(self):
        for key, info in REPORT_TYPES.items():
            assert "name" in info, f"Report type '{key}' missing name"
            assert "description" in info, f"Report type '{key}' missing description"
            assert "sections" in info, f"Report type '{key}' missing sections"

    def test_report_type_names_are_strings(self):
        for key, info in REPORT_TYPES.items():
            assert isinstance(info["name"], str)
            assert isinstance(info["description"], str)
            assert len(info["name"]) > 0
            assert len(info["description"]) > 0


# -----------------------------------------------------------------------
# Generate report tests
# -----------------------------------------------------------------------

class TestGenerateReport:
    @patch("medical_report_writer.core.chat")
    def test_generate_report_returns_string(self, mock_chat):
        mock_chat.return_value = "DISCHARGE SUMMARY\n\nPatient was admitted..."
        result = generate_report("Patient data here", "discharge_summary")
        assert isinstance(result, str)
        assert len(result) > 0

    @patch("medical_report_writer.core.chat")
    def test_generate_report_calls_chat(self, mock_chat):
        mock_chat.return_value = "Report content"
        generate_report("Clinical data", "progress_note")
        mock_chat.assert_called_once()

    @patch("medical_report_writer.core.chat")
    def test_generate_report_includes_system_prompt(self, mock_chat):
        mock_chat.return_value = "Report"
        generate_report("Data", "progress_note")
        messages = mock_chat.call_args[0][0]
        assert messages[0]["role"] == "system"

    def test_generate_report_invalid_type(self):
        with pytest.raises(ValueError, match="Unknown report type"):
            generate_report("data", "invalid_type")


# -----------------------------------------------------------------------
# Discharge summary tests
# -----------------------------------------------------------------------

class TestDischargeSummary:
    @patch("medical_report_writer.core.chat")
    def test_generate_discharge_summary_returns_string(self, mock_chat):
        mock_chat.return_value = "Discharge Summary for patient..."
        result = generate_discharge_summary(
            "Admitted 2024-01-15", "Treated with antibiotics", "Discharge with meds"
        )
        assert isinstance(result, str)

    @patch("medical_report_writer.core.chat")
    def test_discharge_summary_passes_all_data(self, mock_chat):
        mock_chat.return_value = "Summary"
        generate_discharge_summary("admission", "course", "discharge")
        messages = mock_chat.call_args[0][0]
        user_msg = messages[-1]["content"]
        assert "admission" in user_msg.lower() or "ADMISSION" in user_msg


# -----------------------------------------------------------------------
# Referral letter tests
# -----------------------------------------------------------------------

class TestReferralLetter:
    @patch("medical_report_writer.core.chat")
    def test_generate_referral_letter_returns_string(self, mock_chat):
        mock_chat.return_value = "Dear Dr. Smith,\n\nI am referring..."
        result = generate_referral_letter(
            "John Doe, 45M", "Persistent chest pain", "ECG abnormal"
        )
        assert isinstance(result, str)

    @patch("medical_report_writer.core.chat")
    def test_referral_letter_with_physician(self, mock_chat):
        mock_chat.return_value = "Referral letter content"
        generate_referral_letter("Patient info", "Reason", "Findings", "Dr. Johnson")
        messages = mock_chat.call_args[0][0]
        user_msg = messages[-1]["content"]
        assert "Dr. Johnson" in user_msg


# -----------------------------------------------------------------------
# Report session tests
# -----------------------------------------------------------------------

class TestReportSession:
    def test_empty_session(self):
        session = ReportSession()
        assert session.get_reports() == []
        summary = session.get_summary()
        assert summary["total_reports"] == 0

    def test_add_report(self):
        session = ReportSession()
        session.add_report("progress_note", "clinical data", "generated report")
        reports = session.get_reports()
        assert len(reports) == 1
        assert reports[0]["report_type"] == "progress_note"
        assert reports[0]["generated_report"] == "generated report"

    def test_multiple_reports(self):
        session = ReportSession()
        session.add_report("progress_note", "data1", "report1")
        session.add_report("discharge_summary", "data2", "report2")
        assert len(session.get_reports()) == 2

    def test_session_summary(self):
        session = ReportSession()
        session.add_report("progress_note", "data1", "report1")
        session.add_report("discharge_summary", "data2", "report2")
        session.add_report("progress_note", "data3", "report3")

        summary = session.get_summary()
        assert summary["total_reports"] == 3
        assert "progress_note" in summary["report_types"]
        assert "discharge_summary" in summary["report_types"]


# -----------------------------------------------------------------------
# Format report tests
# -----------------------------------------------------------------------

class TestFormatReport:
    def test_standard_format(self):
        raw = "  Line 1  \n  Line 2  \n"
        result = format_report(raw, "standard")
        assert "Line 1" in result
        assert not result.split("\n")[0].endswith("  ")

    def test_compact_format_removes_blank_lines(self):
        raw = "Line 1\n\n\n\nLine 2"
        result = format_report(raw, "compact")
        assert "\n\n\n" not in result

    def test_empty_report(self):
        assert format_report("", "standard") == ""
        assert format_report("   ", "standard") == "   "


# -----------------------------------------------------------------------
# Extract key findings tests
# -----------------------------------------------------------------------

class TestExtractKeyFindings:
    def test_extracts_bullet_points(self):
        report = "Overview\n- Finding one\n- Finding two\nConclusion"
        findings = extract_key_findings(report)
        assert any("Finding one" in f for f in findings)

    def test_extracts_keyword_lines(self):
        report = "Header\nDiagnosis: Pneumonia\nNotes"
        findings = extract_key_findings(report)
        assert any("Diagnosis" in f for f in findings)

    def test_empty_report(self):
        assert extract_key_findings("") == []


# -----------------------------------------------------------------------
# Config loading tests
# -----------------------------------------------------------------------

class TestConfig:
    def test_load_config_returns_dict(self):
        config = load_config()
        assert isinstance(config, dict)

    def test_default_values(self):
        config = load_config()
        assert "model" in config
        assert "temperature" in config
        assert "max_tokens" in config


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
