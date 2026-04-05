"""Tests for Regex Gen core module."""

import pytest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from regex_gen.core import generate_regex, explain_regex, get_pattern_from_library, list_library_patterns
from regex_gen.utils import run_regex_test, validate_regex, extract_regex_from_text, highlight_matches
from regex_gen.config import load_config, RegexConfig


class TestRunRegexTest:
    def test_matching_pattern(self):
        results = run_regex_test(r"\d+", ["abc123", "hello", "42"])
        assert results[0]["matches"] is True
        assert results[1]["matches"] is False
        assert results[2]["matches"] is True

    def test_email_pattern(self):
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        results = run_regex_test(pattern, ["user@example.com", "invalid", "a@b.co"])
        assert results[0]["matches"] is True
        assert results[1]["matches"] is False
        assert results[2]["matches"] is True

    def test_invalid_pattern(self):
        results = run_regex_test(r"[invalid", ["test"])
        assert results[0].get("error") is not None

    def test_match_text_extraction(self):
        results = run_regex_test(r"\d+", ["abc123def"])
        assert results[0]["match_text"] == "123"

    def test_all_matches(self):
        results = run_regex_test(r"\d+", ["abc123def456"])
        assert len(results[0]["all_matches"]) == 2


class TestValidateRegex:
    def test_valid_pattern(self):
        result = validate_regex(r"\d+")
        assert result["valid"] is True

    def test_invalid_pattern(self):
        result = validate_regex(r"[invalid")
        assert result["valid"] is False


class TestExtractRegexFromText:
    def test_extract_from_markdown(self):
        text = "Use the pattern `\\d+` for digits and `[a-z]+` for letters."
        patterns = extract_regex_from_text(text)
        assert len(patterns) >= 1

    def test_no_patterns(self):
        text = "Just some plain text."
        patterns = extract_regex_from_text(text)
        assert len(patterns) == 0


class TestHighlightMatches:
    def test_highlight(self):
        result = highlight_matches("abc123def", r"\d+")
        assert ">>>123<<<" in result


class TestGenerateRegex:
    @patch("regex_gen.core.chat")
    def test_generates_regex(self, mock_chat):
        mock_chat.return_value = "Pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}`"
        result = generate_regex("email addresses")
        assert result is not None
        assert "explanation" in result
        mock_chat.assert_called_once()


class TestExplainRegex:
    @patch("regex_gen.core.chat")
    def test_explains_pattern(self, mock_chat):
        mock_chat.return_value = "This pattern matches one or more digits."
        result = explain_regex(r"\d+")
        assert "explanation" in result
        mock_chat.assert_called_once()


class TestPatternLibrary:
    def test_get_email(self):
        pattern = get_pattern_from_library("email")
        assert pattern is not None
        assert "@" in pattern

    def test_get_nonexistent(self):
        pattern = get_pattern_from_library("nonexistent_xyz")
        assert pattern is None

    def test_list_all(self):
        patterns = list_library_patterns()
        assert len(patterns) > 5


class TestConfig:
    def test_default(self):
        config = RegexConfig()
        assert config.model == "gemma4"

    def test_load_no_file(self):
        config = load_config("nonexistent.yaml")
        assert config.model == "gemma4"
