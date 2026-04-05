"""Tests for Code Reviewer CLI."""

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from code_reviewer.cli import cli


class TestCLIReview:
    @patch("code_reviewer.core.check_ollama_running", return_value=True)
    @patch("code_reviewer.core.chat")
    def test_review_with_file(self, mock_chat, mock_ollama, tmp_path):
        mock_chat.return_value = "## Review\n- No issues found. Code looks clean."
        test_file = tmp_path / "sample.py"
        test_file.write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(cli, ["review", "--file", str(test_file)])
        assert result.exit_code == 0
        mock_chat.assert_called_once()

    @patch("code_reviewer.core.check_ollama_running", return_value=True)
    @patch("code_reviewer.core.chat")
    def test_review_with_focus(self, mock_chat, mock_ollama, tmp_path):
        mock_chat.return_value = "## Security Review\n- No vulnerabilities found."
        test_file = tmp_path / "sample.py"
        test_file.write_text("x = 1\n", encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(cli, ["review", "--file", str(test_file), "--focus", "security"])
        assert result.exit_code == 0

    @patch("code_reviewer.cli.check_ollama_running", return_value=False)
    def test_ollama_not_running(self, mock_ollama, tmp_path):
        test_file = tmp_path / "sample.py"
        test_file.write_text("x = 1\n", encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(cli, ["review", "--file", str(test_file)])
        assert result.exit_code != 0

    def test_missing_file_option(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["review"])
        assert result.exit_code != 0
