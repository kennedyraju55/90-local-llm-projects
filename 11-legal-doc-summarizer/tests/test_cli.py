"""Tests for Legal Document Summarizer CLI."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.legal_summarizer.cli import cli


SAMPLE_CONTRACT = """SERVICES AGREEMENT

This Services Agreement is entered into by Acme Corporation and Legal Solutions LLC.
1. SERVICES: Provider agrees to deliver consulting services.
2. TERM: Effective from January 1, 2025 through December 31, 2025.
3. COMPENSATION: Client shall pay $5,000 per month.
"""

SAMPLE_SUMMARY = "## Summary\nThis is a test summary."


class TestCLI:
    """Tests for the Click CLI interface."""

    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Legal Document Summarizer" in result.output

    def test_summarize_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["summarize", "--help"])
        assert result.exit_code == 0
        assert "--file" in result.output

    def test_summarize_missing_file_option(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["summarize"])
        assert result.exit_code != 0

    @patch("src.legal_summarizer.cli.get_llm_client")
    def test_summarize_ollama_not_running(self, mock_get_client):
        mock_get_client.return_value = (MagicMock(), MagicMock(), MagicMock(return_value=False))
        runner = CliRunner()
        result = runner.invoke(cli, ["summarize", "--file", "dummy.txt"])
        assert result.exit_code != 0

    @patch("src.legal_summarizer.cli.summarize_document", return_value=SAMPLE_SUMMARY)
    @patch("src.legal_summarizer.cli.get_llm_client")
    def test_summarize_successful_run(self, mock_get_client, mock_summarize, tmp_path):
        mock_get_client.return_value = (MagicMock(), MagicMock(), MagicMock(return_value=True))
        filepath = tmp_path / "contract.txt"
        filepath.write_text(SAMPLE_CONTRACT, encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(cli, ["summarize", "--file", str(filepath), "--format", "bullet"])
        assert result.exit_code == 0

    def test_clauses_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["clauses", "--help"])
        assert result.exit_code == 0

    def test_risks_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["risks", "--help"])
        assert result.exit_code == 0

    def test_compare_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["compare", "--help"])
        assert result.exit_code == 0
