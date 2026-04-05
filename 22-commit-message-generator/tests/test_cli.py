"""Tests for Commit Gen CLI."""

import pytest
from unittest.mock import patch
from click.testing import CliRunner
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from commit_gen.cli import cli

SAMPLE_DIFF = """diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1,3 +1,3 @@
-print("hello")
+logging.info("hello")
"""


class TestCLIGenerate:
    @patch("commit_gen.cli.check_ollama_running", return_value=True)
    @patch("commit_gen.core.chat")
    @patch("commit_gen.cli.get_git_diff", return_value=SAMPLE_DIFF)
    @patch("commit_gen.cli.get_git_stat", return_value="1 file changed")
    @patch("commit_gen.cli.read_diff_from_stdin", return_value="")
    def test_basic_generate(self, mock_stdin, mock_stat, mock_diff, mock_chat, mock_ollama):
        mock_chat.return_value = "feat: add logging"
        runner = CliRunner()
        result = runner.invoke(cli, ["generate"])
        assert result.exit_code == 0

    @patch("commit_gen.core.check_ollama_running", return_value=True)
    @patch("commit_gen.core.chat")
    def test_diff_from_file(self, mock_chat, mock_ollama, tmp_path):
        mock_chat.return_value = "feat: add feature"
        diff_file = tmp_path / "changes.diff"
        diff_file.write_text(SAMPLE_DIFF, encoding="utf-8")

        runner = CliRunner()
        result = runner.invoke(cli, ["generate", "--diff-file", str(diff_file)])
        assert result.exit_code == 0

    @patch("commit_gen.cli.check_ollama_running", return_value=False)
    def test_ollama_not_running(self, mock_ollama):
        runner = CliRunner()
        result = runner.invoke(cli, ["generate"])
        assert result.exit_code != 0
