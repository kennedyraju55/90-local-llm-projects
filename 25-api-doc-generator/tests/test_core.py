"""Tests for API Doc Gen core module."""

import pytest
from unittest.mock import patch
import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from api_doc_gen.core import generate_docs, generate_openapi, export_docs
from api_doc_gen.utils import (
    extract_functions, find_python_files, format_extracted_info,
    generate_openapi_skeleton,
)
from api_doc_gen.config import load_config, DocGenConfig

SAMPLE_CODE = '''"""Sample module."""

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

class Calculator:
    """A simple calculator."""

    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers."""
        return x * y

    def divide(self, x: float, y: float) -> float:
        """Divide x by y."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

async def fetch_data(url: str) -> dict:
    """Fetch data from a URL."""
    pass
'''


class TestExtractFunctions:
    def test_extracts_functions(self, tmp_path):
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")
        items = extract_functions(str(f))
        names = [i["name"] for i in items]
        assert "add" in names
        assert "Calculator" in names
        assert "fetch_data" in names

    def test_function_args(self, tmp_path):
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")
        items = extract_functions(str(f))
        add_func = [i for i in items if i["name"] == "add"][0]
        assert len(add_func["args"]) == 2
        assert add_func["args"][0]["name"] == "a"
        assert add_func["returns"] == "int"

    def test_class_methods(self, tmp_path):
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")
        items = extract_functions(str(f))
        calc = [i for i in items if i["name"] == "Calculator"][0]
        method_names = [m["name"] for m in calc["methods"]]
        assert "multiply" in method_names
        assert "divide" in method_names

    def test_async_function(self, tmp_path):
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")
        items = extract_functions(str(f))
        fetch = [i for i in items if i["name"] == "fetch_data"][0]
        assert fetch["is_async"] is True

    def test_syntax_error(self, tmp_path):
        f = tmp_path / "bad.py"
        f.write_text("def broken(:\n  pass", encoding="utf-8")
        items = extract_functions(str(f))
        assert items == []


class TestFindPythonFiles:
    def test_find_single_file(self, tmp_path):
        f = tmp_path / "test.py"
        f.write_text("x = 1", encoding="utf-8")
        files = find_python_files(str(f))
        assert len(files) == 1

    def test_find_in_directory(self, tmp_path):
        (tmp_path / "a.py").write_text("x=1", encoding="utf-8")
        (tmp_path / "b.py").write_text("y=2", encoding="utf-8")
        (tmp_path / "c.txt").write_text("z=3", encoding="utf-8")
        files = find_python_files(str(tmp_path))
        assert len(files) == 2

    def test_nonexistent_path(self):
        files = find_python_files("nonexistent_path_xyz")
        assert files == []


class TestFormatExtractedInfo:
    def test_formats_function(self):
        items = [{"type": "function", "name": "add", "lineno": 1,
                  "args": [{"name": "a", "annotation": "int"}],
                  "returns": "int", "docstring": "Add numbers.", "is_async": False,
                  "decorators": []}]
        result = format_extracted_info("test.py", items)
        assert "add" in result
        assert "int" in result


class TestGenerateOpenAPISkeleton:
    def test_generates_spec(self, tmp_path):
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")
        items = extract_functions(str(f))
        spec = generate_openapi_skeleton(items, "TestAPI")
        assert "openapi" in spec
        assert spec["info"]["title"] == "TestAPI"


class TestGenerateDocs:
    @patch("api_doc_gen.core.chat")
    def test_generate_docs(self, mock_chat, tmp_path):
        mock_chat.return_value = "# API Docs\n## add(a, b)\nAdds two numbers."
        f = tmp_path / "sample.py"
        f.write_text(SAMPLE_CODE, encoding="utf-8")
        result = generate_docs(str(f))
        assert "docs" in result
        assert result["items_count"] > 0

    def test_no_files(self):
        result = generate_docs("nonexistent_xyz")
        assert "No Python files" in result["docs"]


class TestExportDocs:
    def test_export_markdown(self, tmp_path):
        out = str(tmp_path / "docs.md")
        export_docs("# Docs", out)
        assert os.path.exists(out)


class TestConfig:
    def test_default(self):
        config = DocGenConfig()
        assert config.model == "gemma4"

    def test_load_no_file(self):
        config = load_config("nonexistent.yaml")
        assert config.model == "gemma4"
