"""Tests for Regex Gen CLI."""

import pytest
from unittest.mock import patch
from click.testing import CliRunner
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from regex_gen.cli import cli


class TestCLIGenerate:
    @patch("regex_gen.core.check_ollama_running", return_value=True)
    @patch("regex_gen.core.chat")
    def test_generate_command(self, mock_chat, mock_ollama):
        mock_chat.return_value = "Pattern: `\\d+`\nMatches digits."
        runner = CliRunner()
        result = runner.invoke(cli, ["generate", "numbers"])
        assert result.exit_code == 0

    @patch("regex_gen.core.check_ollama_running", return_value=True)
    @patch("regex_gen.core.chat")
    def test_explain_command(self, mock_chat, mock_ollama):
        mock_chat.return_value = "Matches one or more lowercase letters."
        runner = CliRunner()
        result = runner.invoke(cli, ["explain", "[a-z]+"])
        assert result.exit_code == 0

    def test_test_command(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["test", r"\d+", "abc123", "hello"])
        assert result.exit_code == 0

    def test_library_command(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["library"])
        assert result.exit_code == 0

    def test_library_specific(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["library", "email"])
        assert result.exit_code == 0

    @patch("regex_gen.cli.check_ollama_running", return_value=False)
    def test_ollama_not_running(self, mock_ollama):
        runner = CliRunner()
        result = runner.invoke(cli, ["generate", "email"])
        assert result.exit_code != 0
