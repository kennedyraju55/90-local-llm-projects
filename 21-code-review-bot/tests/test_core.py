"""Tests for Code Reviewer core module."""

import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from code_reviewer.core import review_single_file, review_multiple_files, generate_autofix, export_report
from code_reviewer.utils import detect_language, number_lines, calculate_severity_score, read_file_safe
from code_reviewer.config import load_config, ReviewConfig


class TestDetectLanguage:
    def test_python_file(self):
        assert detect_language("script.py") == "python"

    def test_javascript_file(self):
        assert detect_language("app.js") == "javascript"

    def test_unknown_extension(self):
        assert detect_language("file.xyz") == "text"

    def test_no_extension(self):
        assert detect_language("Makefile") == "text"

    def test_java_file(self):
        assert detect_language("Main.java") == "java"

    def test_typescript_file(self):
        assert detect_language("index.ts") == "typescript"


class TestNumberLines:
    def test_basic(self):
        result = number_lines("hello\nworld")
        assert "1: hello" in result
        assert "2: world" in result

    def test_empty(self):
        result = number_lines("")
        assert result == ""


class TestCalculateSeverityScore:
    def test_clean_code(self):
        result = calculate_severity_score([])
        assert result["score"] == 100
        assert result["grade"] == "A"

    def test_high_severity_issues(self):
        issues = [{"severity": "HIGH"}, {"severity": "HIGH"}]
        result = calculate_severity_score(issues)
        assert result["score"] < 100
        assert result["counts"]["HIGH"] == 2

    def test_mixed_issues(self):
        issues = [{"severity": "HIGH"}, {"severity": "MEDIUM"}, {"severity": "LOW"}]
        result = calculate_severity_score(issues)
        assert result["total_issues"] == 3


class TestReadFileSafe:
    def test_read_existing_file(self, tmp_path):
        test_file = tmp_path / "test.py"
        test_file.write_text("print('hello')", encoding="utf-8")
        content = read_file_safe(str(test_file))
        assert content == "print('hello')"

    def test_nonexistent_file(self):
        result = read_file_safe("nonexistent_file_xyz.py")
        assert result is None

    def test_file_too_large(self, tmp_path):
        test_file = tmp_path / "big.py"
        test_file.write_text("x" * (600 * 1024), encoding="utf-8")
        result = read_file_safe(str(test_file), max_size_kb=500)
        assert result is None


class TestReviewSingleFile:
    @patch("code_reviewer.core.chat")
    @patch("code_reviewer.core.check_ollama_running", return_value=True)
    def test_review_valid_file(self, mock_ollama, mock_chat, tmp_path):
        mock_chat.return_value = "## Review\n- No issues found."
        test_file = tmp_path / "sample.py"
        test_file.write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")

        result = review_single_file(str(test_file))
        assert "review" in result
        assert result["filename"] == "sample.py"
        mock_chat.assert_called_once()

    def test_review_nonexistent_file(self):
        result = review_single_file("nonexistent.py")
        assert result.get("error") is not None

    def test_review_empty_file(self, tmp_path):
        test_file = tmp_path / "empty.py"
        test_file.write_text("", encoding="utf-8")
        result = review_single_file(str(test_file))
        assert result.get("error") is not None


class TestExportReport:
    def test_export_markdown(self, tmp_path):
        results = [{"filename": "test.py", "language": "python", "lines": 10, "review": "Looks good."}]
        out = str(tmp_path / "report.md")
        export_report(results, out, "markdown")
        assert os.path.exists(out)

    def test_export_json(self, tmp_path):
        results = [{"filename": "test.py", "review": "OK"}]
        out = str(tmp_path / "report.json")
        export_report(results, out, "json")
        assert os.path.exists(out)


class TestConfig:
    def test_default_config(self):
        config = ReviewConfig()
        assert config.model == "gemma4"
        assert config.temperature == 0.3

    def test_load_config_no_file(self):
        config = load_config("nonexistent.yaml")
        assert config.model == "gemma4"
