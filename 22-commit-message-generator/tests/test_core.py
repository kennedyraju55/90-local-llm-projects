"""Tests for Commit Gen core module."""

import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from commit_gen.core import generate_commit_messages, generate_batch_messages
from commit_gen.utils import (
    truncate_diff, add_emoji_to_message, get_git_branch,
    get_git_staged_files, read_diff_from_stdin,
)
from commit_gen.config import load_config, CommitConfig, COMMIT_EMOJIS

SAMPLE_DIFF = """diff --git a/app.py b/app.py
index 1234567..abcdefg 100644
--- a/app.py
+++ b/app.py
@@ -1,3 +1,5 @@
+import logging
+
 def main():
-    print("hello")
+    logging.info("hello")
     return 0
"""


class TestGenerateCommitMessages:
    @patch("commit_gen.core.chat")
    def test_generates_messages(self, mock_chat):
        mock_chat.return_value = "1. feat: add logging support\n2. refactor: replace print"
        result = generate_commit_messages(SAMPLE_DIFF)
        assert result is not None
        mock_chat.assert_called_once()

    @patch("commit_gen.core.chat")
    def test_with_type_hint(self, mock_chat):
        mock_chat.return_value = "1. refactor: replace print with logging"
        result = generate_commit_messages(SAMPLE_DIFF, msg_type="refactor")
        call_args = str(mock_chat.call_args)
        assert "refactor" in call_args

    @patch("commit_gen.core.chat")
    def test_truncates_large_diff(self, mock_chat):
        mock_chat.return_value = "1. feat: large change"
        large_diff = "+" * 10000
        generate_commit_messages(large_diff)
        call_args = str(mock_chat.call_args)
        assert len(call_args) < 15000


class TestUtils:
    def test_truncate_diff_short(self):
        result = truncate_diff("short diff", max_chars=1000)
        assert result == "short diff"

    def test_truncate_diff_long(self):
        result = truncate_diff("x" * 5000, max_chars=100)
        assert len(result) < 200
        assert "truncated" in result

    def test_add_emoji(self):
        result = add_emoji_to_message("feat: add feature", COMMIT_EMOJIS)
        assert "✨" in result

    def test_add_emoji_no_match(self):
        result = add_emoji_to_message("something else", COMMIT_EMOJIS)
        assert result == "something else"


class TestConfig:
    def test_default_config(self):
        config = CommitConfig()
        assert config.model == "gemma4"
        assert config.num_suggestions == 3

    def test_load_config_no_file(self):
        config = load_config("nonexistent.yaml")
        assert config.model == "gemma4"


class TestBatchMessages:
    @patch("commit_gen.core.chat")
    def test_batch_generation(self, mock_chat):
        mock_chat.return_value = "feat: change"
        diffs = [
            {"name": "file1", "diff": SAMPLE_DIFF},
            {"name": "file2", "diff": ""},
        ]
        results = generate_batch_messages(diffs)
        assert len(results) == 2
        assert results[1]["messages"] == "No changes found."
