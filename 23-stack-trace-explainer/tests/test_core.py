"""Tests for Stack Explainer core module."""

import pytest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from stack_explainer.core import explain_trace, generate_fix_code, find_similar_errors
from stack_explainer.utils import (
    detect_language, read_trace_from_file, truncate_trace,
    extract_error_type, get_error_hint,
)
from stack_explainer.config import load_config, ExplainerConfig

PYTHON_TRACE = """Traceback (most recent call last):
  File "app.py", line 42, in main
    result = process(data)
  File "app.py", line 28, in process
    return data["key"]
KeyError: 'key'
"""

JAVA_TRACE = """Exception in thread "main" java.lang.NullPointerException
    at com.example.App.process(App.java:42)
    at com.example.App.main(App.java:15)
"""

JS_TRACE = """TypeError: Cannot read property 'map' of undefined
    at Object.<anonymous> (/app/src/index.js:15:20)
    at Module._compile (node:internal/modules/cjs/loader:1105:14)
"""


class TestDetectLanguage:
    def test_detect_python(self):
        assert detect_language(PYTHON_TRACE) == "python"

    def test_detect_java(self):
        assert detect_language(JAVA_TRACE) == "java"

    def test_detect_javascript(self):
        assert detect_language(JS_TRACE) == "javascript"

    def test_detect_unknown(self):
        assert detect_language("some random text") == "unknown"


class TestExtractErrorType:
    def test_python_key_error(self):
        result = extract_error_type(PYTHON_TRACE)
        assert result is not None
        assert "KeyError" in result

    def test_java_npe(self):
        result = extract_error_type(JAVA_TRACE)
        assert result is not None
        assert "NullPointerException" in result

    def test_no_error(self):
        result = extract_error_type("just some text")
        assert result is None


class TestGetErrorHint:
    def test_python_key_error(self):
        hint = get_error_hint("python", "KeyError: 'key'")
        assert hint is not None
        assert "dictionary" in hint.lower()

    def test_unknown_error(self):
        hint = get_error_hint("python", "SomeCustomError")
        assert hint is None


class TestReadTraceFromFile:
    def test_read_existing_file(self, tmp_path):
        trace_file = tmp_path / "error.txt"
        trace_file.write_text(PYTHON_TRACE, encoding="utf-8")
        content = read_trace_from_file(str(trace_file))
        assert "KeyError" in content

    def test_read_nonexistent_file(self):
        result = read_trace_from_file("nonexistent_error.txt")
        assert result is None


class TestTruncateTrace:
    def test_short_trace(self):
        result = truncate_trace("short", max_chars=1000)
        assert result == "short"

    def test_long_trace(self):
        result = truncate_trace("x" * 10000, max_chars=100)
        assert "truncated" in result


class TestExplainTrace:
    @patch("stack_explainer.core.chat")
    def test_explain_python_trace(self, mock_chat):
        mock_chat.return_value = "This is a KeyError."
        result = explain_trace(PYTHON_TRACE, "python")
        assert "explanation" in result
        assert result["language"] == "python"
        mock_chat.assert_called_once()

    @patch("stack_explainer.core.chat")
    def test_explain_with_language_hint(self, mock_chat):
        mock_chat.return_value = "NullPointerException explanation"
        result = explain_trace(JAVA_TRACE, "java")
        assert result["language"] == "java"


class TestConfig:
    def test_default_config(self):
        config = ExplainerConfig()
        assert config.model == "gemma4"

    def test_load_config_no_file(self):
        config = load_config("nonexistent.yaml")
        assert config.model == "gemma4"
