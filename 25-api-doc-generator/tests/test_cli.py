"""Tests for API Doc Gen CLI."""

import pytest
from unittest.mock import patch
from click.testing import CliRunner
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from api_doc_gen.cli import cli

SAMPLE_CODE = '''def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
'''


class TestCLIGenerate:
    @patch("api_doc_gen.core.check_ollama_running", return_value=True)
    @patch("api_doc_gen.core.chat")
    def test_generate_docs(self, mock_chat, mock_ollama, tmp_path):
        mock_chat.return_value = "# API Docs\n## add(a, b)\nAdds two numbers."
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(cli, ["generate", "--source", str(f)])
        assert result.exit_code == 0

    @patch("api_doc_gen.core.check_ollama_running", return_value=True)
    @patch("api_doc_gen.core.chat")
    def test_output_to_file(self, mock_chat, mock_ollama, tmp_path):
        mock_chat.return_value = "# API Documentation"
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")
        out = tmp_path / "docs.md"

        runner = CliRunner()
        result = runner.invoke(cli, ["generate", "--source", str(f), "--output", str(out)])
        assert result.exit_code == 0
        assert out.exists()

    @patch("api_doc_gen.cli.check_ollama_running", return_value=False)
    def test_ollama_not_running(self, mock_ollama, tmp_path):
        f = tmp_path / "sample.py"
        f.write_text("x=1", encoding="utf-8")
        runner = CliRunner()
        result = runner.invoke(cli, ["generate", "--source", str(f)])
        assert result.exit_code != 0

    def test_inspect_command(self, tmp_path):
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")
        runner = CliRunner()
        result = runner.invoke(cli, ["inspect", "--source", str(f)])
        assert result.exit_code == 0
