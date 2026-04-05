"""Tests for Stack Explainer CLI."""

import pytest
from unittest.mock import patch
from click.testing import CliRunner
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from stack_explainer.cli import cli

PYTHON_TRACE = """Traceback (most recent call last):
  File "app.py", line 42, in main
    result = process(data)
KeyError: 'key'
"""


class TestCLIExplain:
    @patch("stack_explainer.core.check_ollama_running", return_value=True)
    @patch("stack_explainer.core.chat")
    def test_with_trace_file(self, mock_chat, mock_ollama, tmp_path):
        mock_chat.return_value = "## Error\nKeyError means the key was not found."
        trace_file = tmp_path / "error.txt"
        trace_file.write_text(PYTHON_TRACE, encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(cli, ["explain", "--trace", str(trace_file)])
        assert result.exit_code == 0

    @patch("stack_explainer.core.check_ollama_running", return_value=True)
    @patch("stack_explainer.core.chat")
    def test_with_text_argument(self, mock_chat, mock_ollama):
        mock_chat.return_value = "Error explanation here."
        runner = CliRunner()
        result = runner.invoke(cli, ["explain", "--text", PYTHON_TRACE])
        assert result.exit_code == 0

    @patch("stack_explainer.cli.check_ollama_running", return_value=False)
    def test_ollama_not_running(self, mock_ollama):
        runner = CliRunner()
        result = runner.invoke(cli, ["explain", "--text", "error"])
        assert result.exit_code != 0

    def test_no_input(self):
        runner = CliRunner()
        with patch("stack_explainer.cli.check_ollama_running", return_value=True):
            result = runner.invoke(cli, ["explain"])
            assert result.exit_code != 0
