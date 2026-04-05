"""Tests for Medical Literature Summarizer core logic."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock

from src.medical_summarizer.core import (
    SECTIONS, summarize_paper, extract_section, extract_pico,
    rate_evidence_quality, format_citation,
)
from src.medical_summarizer.utils import read_paper
from src.medical_summarizer.config import load_config

SAMPLE_PAPER = """\
Title: Effects of Aspirin on Cardiovascular Mortality in Elderly Patients
Authors: Jane Smith, MD; John Doe, PhD

Abstract:
This randomized controlled trial examined low-dose aspirin effects on
cardiovascular mortality in adults aged 65+. N=5000, p=0.003, 95% CI: 0.78-0.92.

Methodology:
Double-blind, placebo-controlled RCT. 100mg aspirin vs placebo.

Results:
15% relative risk reduction (HR=0.85, 95% CI: 0.78-0.92, p=0.003).

Conclusions:
Low-dose aspirin significantly reduces cardiovascular events in elderly.

Limitations:
Predominantly Caucasian population. Self-reported adherence.
"""


class TestReadPaper:
    def test_read_valid(self, tmp_path):
        f = tmp_path / "paper.txt"
        f.write_text(SAMPLE_PAPER, encoding="utf-8")
        assert "Aspirin" in read_paper(str(f))

    def test_read_missing(self):
        with pytest.raises(FileNotFoundError):
            read_paper("nonexistent.txt")

    def test_read_empty(self, tmp_path):
        f = tmp_path / "empty.txt"
        f.write_text("", encoding="utf-8")
        with pytest.raises(ValueError):
            read_paper(str(f))


class TestSummarizePaper:
    @patch("src.medical_summarizer.core.get_llm_client")
    def test_returns_all_sections(self, mock_get):
        mock_chat = MagicMock(return_value="Mocked response.")
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        results = summarize_paper(SAMPLE_PAPER, "standard")
        expected_keys = {key for key, _, _ in SECTIONS}
        assert set(results.keys()) == expected_keys

    @patch("src.medical_summarizer.core.get_llm_client")
    def test_calls_llm_per_section(self, mock_get):
        mock_chat = MagicMock(return_value="Response.")
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        summarize_paper(SAMPLE_PAPER, "standard")
        assert mock_chat.call_count == len(SECTIONS)

    @patch("src.medical_summarizer.core.get_llm_client")
    def test_handles_llm_error(self, mock_get):
        mock_chat = MagicMock(side_effect=Exception("LLM failed"))
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        results = summarize_paper(SAMPLE_PAPER, "standard")
        for value in results.values():
            assert "Error" in value


class TestExtractSection:
    @patch("src.medical_summarizer.core.get_llm_client")
    def test_uses_system_prompt(self, mock_get):
        mock_chat = MagicMock(return_value="Content.")
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        extract_section(SAMPLE_PAPER, "methodology", "Describe methodology.", "standard")
        assert "expert medical" in mock_chat.call_args.kwargs["system_prompt"].lower()

    @patch("src.medical_summarizer.core.get_llm_client")
    def test_brief_level(self, mock_get):
        mock_chat = MagicMock(return_value="Brief.")
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        extract_section(SAMPLE_PAPER, "conclusions", "Summarize.", "brief")
        assert "concise" in mock_chat.call_args.kwargs["system_prompt"].lower()


class TestPICO:
    @patch("src.medical_summarizer.core.get_llm_client")
    def test_extract_pico(self, mock_get):
        mock_chat = MagicMock(return_value="P: Elderly patients\nI: Aspirin")
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        result = extract_pico(SAMPLE_PAPER)
        assert isinstance(result, str)
        mock_chat.assert_called_once()


class TestEvidenceQuality:
    @patch("src.medical_summarizer.core.get_llm_client")
    def test_rate_evidence(self, mock_get):
        mock_chat = MagicMock(return_value="Study Design: 4/5")
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        result = rate_evidence_quality(SAMPLE_PAPER)
        assert isinstance(result, str)


class TestCitation:
    @patch("src.medical_summarizer.core.get_llm_client")
    def test_format_citation(self, mock_get):
        mock_chat = MagicMock(return_value="Smith, J. (2024).")
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        result = format_citation(SAMPLE_PAPER, "APA")
        assert isinstance(result, str)


class TestConfig:
    def test_default_config(self):
        assert load_config()["llm"]["model"] == "gemma4"

    @patch.dict(os.environ, {"MEDICAL_SUMMARIZER_MODEL": "llama3"})
    def test_env_override(self):
        assert load_config()["llm"]["model"] == "llama3"
