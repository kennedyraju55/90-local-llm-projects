"""Tests for Legal Document Summarizer core logic."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock

from src.legal_summarizer.core import (
    summarize_document,
    extract_clauses,
    score_risks,
    generate_export_markdown,
)
from src.legal_summarizer.utils import (
    read_text_file,
    read_document,
    truncate_text,
)
from src.legal_summarizer.config import load_config, DEFAULT_CONFIG


SAMPLE_CONTRACT = """SERVICES AGREEMENT

This Services Agreement ("Agreement") is entered into as of January 1, 2025,
by and between Acme Corporation ("Client") and Legal Solutions LLC ("Provider").

1. SERVICES: Provider agrees to deliver consulting services as described in Exhibit A.
2. TERM: This Agreement is effective from January 1, 2025 through December 31, 2025.
3. COMPENSATION: Client shall pay Provider $5,000 per month, due on the 1st of each month.
4. TERMINATION: Either party may terminate with 30 days written notice.
5. CONFIDENTIALITY: Both parties agree to maintain confidentiality of proprietary information.
6. PENALTIES: Late payments shall incur a 1.5% monthly interest charge.
"""

SAMPLE_SUMMARY = """## Parties Involved
- **Acme Corporation** (Client)
- **Legal Solutions LLC** (Provider)

## Key Clauses
- Services clause defining consulting scope
- Term and duration clause

## Obligations
- Provider must deliver consulting services per Exhibit A
- Client must pay $5,000/month

## Important Dates
- Effective Date: January 1, 2025

## Termination Conditions
- Either party may terminate with 30 days written notice

## Penalties & Liabilities
- Late payments incur 1.5% monthly interest
"""


class TestReadTextFile:
    """Tests for reading text files."""

    def test_read_valid_text_file(self, tmp_path):
        filepath = tmp_path / "contract.txt"
        filepath.write_text(SAMPLE_CONTRACT, encoding="utf-8")
        content = read_text_file(str(filepath))
        assert "SERVICES AGREEMENT" in content
        assert "Acme Corporation" in content

    def test_read_file_not_found(self):
        with pytest.raises(FileNotFoundError, match="File not found"):
            read_text_file("nonexistent_file.txt")

    def test_read_empty_file(self, tmp_path):
        filepath = tmp_path / "empty.txt"
        filepath.write_text("", encoding="utf-8")
        with pytest.raises(ValueError, match="File is empty"):
            read_text_file(str(filepath))

    def test_read_whitespace_only_file(self, tmp_path):
        filepath = tmp_path / "whitespace.txt"
        filepath.write_text("   \n\n  \t  ", encoding="utf-8")
        with pytest.raises(ValueError, match="File is empty"):
            read_text_file(str(filepath))


class TestReadDocument:
    """Tests for the document reading dispatcher."""

    def test_read_txt_file(self, tmp_path):
        filepath = tmp_path / "agreement.txt"
        filepath.write_text(SAMPLE_CONTRACT, encoding="utf-8")
        content = read_document(str(filepath))
        assert "SERVICES AGREEMENT" in content

    def test_read_unknown_extension_as_text(self, tmp_path):
        filepath = tmp_path / "contract.doc"
        filepath.write_text(SAMPLE_CONTRACT, encoding="utf-8")
        content = read_document(str(filepath))
        assert "SERVICES AGREEMENT" in content

    def test_read_pdf_dispatches_correctly(self, tmp_path):
        filepath = tmp_path / "contract.pdf"
        filepath.write_bytes(b"fake")
        with patch("src.legal_summarizer.utils.read_pdf_file", return_value=SAMPLE_CONTRACT) as mock_pdf:
            content = read_document(str(filepath))
            mock_pdf.assert_called_once_with(str(filepath))
            assert "SERVICES AGREEMENT" in content


class TestTruncateText:
    """Tests for text truncation utility."""

    def test_short_text_unchanged(self):
        result = truncate_text("short text", 1000)
        assert result == "short text"

    def test_long_text_truncated(self):
        long_text = "x" * 20000
        result = truncate_text(long_text, 12000)
        assert len(result) < 20000
        assert "truncated" in result.lower()


class TestSummarizeDocument:
    """Tests for the LLM summarization function."""

    @patch("src.legal_summarizer.core.get_llm_client")
    def test_summarize_returns_llm_response(self, mock_get_client):
        mock_chat = MagicMock(return_value=SAMPLE_SUMMARY)
        mock_get_client.return_value = (mock_chat, MagicMock(), MagicMock())

        result = summarize_document(SAMPLE_CONTRACT, "bullet")
        assert "Parties Involved" in result
        assert "Key Clauses" in result
        mock_chat.assert_called_once()

    @patch("src.legal_summarizer.core.get_llm_client")
    def test_summarize_passes_correct_parameters(self, mock_get_client):
        mock_chat = MagicMock(return_value=SAMPLE_SUMMARY)
        mock_get_client.return_value = (mock_chat, MagicMock(), MagicMock())

        summarize_document(SAMPLE_CONTRACT, "detailed")
        call_kwargs = mock_chat.call_args
        assert call_kwargs.kwargs["temperature"] == 0.3
        assert call_kwargs.kwargs["max_tokens"] == 4096

    @patch("src.legal_summarizer.core.get_llm_client")
    def test_summarize_truncates_long_documents(self, mock_get_client):
        mock_chat = MagicMock(return_value=SAMPLE_SUMMARY)
        mock_get_client.return_value = (mock_chat, MagicMock(), MagicMock())

        long_text = "x" * 20000
        summarize_document(long_text, "bullet")
        call_args = mock_chat.call_args
        messages = call_args.kwargs.get("messages") or call_args[0][0]
        message_content = messages[0]["content"]
        assert "truncated" in message_content.lower()


class TestExtractClauses:
    """Tests for clause extraction."""

    @patch("src.legal_summarizer.core.get_llm_client")
    def test_extract_clauses_calls_llm(self, mock_get_client):
        mock_chat = MagicMock(return_value="Clause 1: Services\nClause 2: Payment")
        mock_get_client.return_value = (mock_chat, MagicMock(), MagicMock())

        result = extract_clauses(SAMPLE_CONTRACT)
        assert isinstance(result, str)
        mock_chat.assert_called_once()


class TestScoreRisks:
    """Tests for risk scoring."""

    @patch("src.legal_summarizer.core.get_llm_client")
    def test_score_risks_calls_llm(self, mock_get_client):
        mock_chat = MagicMock(return_value="Financial Risk: 3/10")
        mock_get_client.return_value = (mock_chat, MagicMock(), MagicMock())

        result = score_risks(SAMPLE_CONTRACT)
        assert isinstance(result, str)
        mock_chat.assert_called_once()


class TestGenerateExportMarkdown:
    """Tests for markdown export."""

    def test_basic_export(self):
        md = generate_export_markdown(SAMPLE_SUMMARY, filepath="contract.txt")
        assert "Legal Document Analysis Report" in md
        assert "contract.txt" in md
        assert "Parties Involved" in md

    def test_export_with_all_sections(self):
        md = generate_export_markdown(SAMPLE_SUMMARY, "clauses", "risks", "file.pdf")
        assert "Clause Extraction" in md
        assert "Risk Analysis" in md


class TestConfig:
    """Tests for configuration management."""

    def test_default_config_loaded(self):
        config = load_config()
        assert config["llm"]["model"] == "gemma4"
        assert config["llm"]["temperature"] == 0.3

    def test_config_from_yaml(self, tmp_path):
        config_file = tmp_path / "config.yaml"
        config_file.write_text("llm:\n  temperature: 0.5\n", encoding="utf-8")
        config = load_config(str(config_file))
        assert config["llm"]["temperature"] == 0.5

    @patch.dict(os.environ, {"LEGAL_SUMMARIZER_MODEL": "llama3"})
    def test_env_override(self):
        config = load_config()
        assert config["llm"]["model"] == "llama3"
