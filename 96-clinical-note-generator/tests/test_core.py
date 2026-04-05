"""Tests for clinical_note_generator.core module."""

import pytest
from unittest.mock import patch, MagicMock
from clinical_note_generator.core import (
    DISCLAIMER,
    SYSTEM_PROMPT,
    NOTE_TEMPLATES,
    SPECIALTY_PROMPTS,
    generate_soap_note,
    generate_note_section,
    refine_note,
    extract_diagnoses,
    NoteSession,
    load_config,
    display_disclaimer,
)


class TestDisclaimer:
    def test_disclaimer_not_empty(self):
        assert DISCLAIMER is not None
        assert len(DISCLAIMER) > 0

    def test_disclaimer_contains_warning(self):
        assert "EDUCATIONAL" in DISCLAIMER or "INFORMATIONAL" in DISCLAIMER
        assert "DISCLAIMER" in DISCLAIMER

    def test_disclaimer_mentions_physician_review(self):
        assert "physician" in DISCLAIMER.lower() or "review" in DISCLAIMER.lower()


class TestNoteTemplates:
    def test_templates_exist(self):
        assert len(NOTE_TEMPLATES) > 0

    def test_general_template_exists(self):
        assert "general" in NOTE_TEMPLATES

    def test_all_templates_have_descriptions(self):
        for key, value in NOTE_TEMPLATES.items():
            assert isinstance(value, str)
            assert len(value) > 0


class TestSpecialties:
    def test_specialties_exist(self):
        assert len(SPECIALTY_PROMPTS) > 0

    def test_internal_medicine_exists(self):
        assert "internal_medicine" in SPECIALTY_PROMPTS

    def test_all_specialties_have_prompts(self):
        for key, value in SPECIALTY_PROMPTS.items():
            assert isinstance(value, str)
            assert len(value) > 0


class TestGenerateSoapNote:
    @patch("clinical_note_generator.core.chat")
    def test_returns_string(self, mock_chat):
        mock_chat.return_value = "S: Patient presents with headache.\nO: Vitals stable.\nA: Tension headache.\nP: Acetaminophen PRN."
        result = generate_soap_note("Patient with headache for 2 days")
        assert isinstance(result, str)
        assert len(result) > 0

    @patch("clinical_note_generator.core.chat")
    def test_calls_chat(self, mock_chat):
        mock_chat.return_value = "SOAP note content"
        generate_soap_note("Patient encounter")
        mock_chat.assert_called_once()

    @patch("clinical_note_generator.core.chat")
    def test_with_demographics(self, mock_chat):
        mock_chat.return_value = "SOAP note"
        generate_soap_note("encounter", patient_demographics={"age": "45", "sex": "Male"})
        call_args = mock_chat.call_args[0][0]
        user_msg = [m for m in call_args if m["role"] == "user"][0]
        assert "45" in user_msg["content"]

    @patch("clinical_note_generator.core.chat")
    def test_includes_system_prompt(self, mock_chat):
        mock_chat.return_value = "Note"
        generate_soap_note("encounter")
        messages = mock_chat.call_args[0][0]
        assert messages[0]["role"] == "system"

    @patch("clinical_note_generator.core.chat")
    def test_raises_on_error(self, mock_chat):
        mock_chat.side_effect = ConnectionError("Ollama down")
        with pytest.raises(ConnectionError):
            generate_soap_note("test")


class TestGenerateNoteSection:
    @patch("clinical_note_generator.core.chat")
    def test_generates_subjective(self, mock_chat):
        mock_chat.return_value = "Patient reports headache for 2 days."
        result = generate_note_section("headache patient", "S")
        assert isinstance(result, str)

    @patch("clinical_note_generator.core.chat")
    def test_generates_plan(self, mock_chat):
        mock_chat.return_value = "1. Acetaminophen PRN\n2. Follow up in 1 week"
        result = generate_note_section("headache patient", "P")
        assert isinstance(result, str)


class TestRefineNote:
    @patch("clinical_note_generator.core.chat")
    def test_refine_returns_string(self, mock_chat):
        mock_chat.return_value = "Refined note content"
        result = refine_note("Original note", "Add more detail")
        assert isinstance(result, str)

    @patch("clinical_note_generator.core.chat")
    def test_refine_calls_chat(self, mock_chat):
        mock_chat.return_value = "Refined"
        refine_note("note", "feedback")
        mock_chat.assert_called_once()


class TestExtractDiagnoses:
    @patch("clinical_note_generator.core.chat")
    def test_returns_list(self, mock_chat):
        mock_chat.return_value = "1. Tension headache\n2. Migraine"
        result = extract_diagnoses("A: Tension headache vs migraine")
        assert isinstance(result, list)

    @patch("clinical_note_generator.core.chat")
    def test_handles_empty(self, mock_chat):
        mock_chat.return_value = ""
        result = extract_diagnoses("No assessment")
        assert isinstance(result, list)


class TestNoteSession:
    def test_empty_session(self):
        session = NoteSession()
        assert session.get_notes() == []
        assert session.get_summary()["total_notes"] == 0

    def test_add_note(self):
        session = NoteSession()
        session.add_note("encounter", "SOAP note", "general", "internal_medicine")
        assert len(session.get_notes()) == 1

    def test_multiple_notes(self):
        session = NoteSession()
        session.add_note("enc1", "note1", "general", "internal_medicine")
        session.add_note("enc2", "note2", "urgent", "emergency")
        assert len(session.get_notes()) == 2

    def test_summary(self):
        session = NoteSession()
        session.add_note("enc1", "note1", "general", "internal_medicine")
        session.add_note("enc2", "note2", "urgent", "emergency")
        summary = session.get_summary()
        assert summary["total_notes"] == 2
        assert "general" in summary["note_types"]

    def test_note_has_timestamp(self):
        session = NoteSession()
        session.add_note("enc", "note", "general", "internal_medicine")
        assert "timestamp" in session.get_notes()[0]


class TestConfig:
    def test_load_config_returns_dict(self):
        config = load_config()
        assert isinstance(config, dict)

    def test_default_model(self):
        config = load_config()
        assert "model" in config

    def test_default_temperature(self):
        config = load_config()
        assert "temperature" in config
