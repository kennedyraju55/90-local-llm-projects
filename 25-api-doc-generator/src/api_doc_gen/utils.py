"""Utility helpers for API Doc Gen."""

import os
import ast
import json
import logging
import glob as glob_module
from typing import Optional

logger = logging.getLogger(__name__)


def find_python_files(source_path: str) -> list[str]:
    """Find all Python files in a directory or return a single file."""
    if os.path.isfile(source_path):
        return [source_path]
    if os.path.isdir(source_path):
        return sorted(glob_module.glob(os.path.join(source_path, "**", "*.py"), recursive=True))
    logger.error("Path not found: %s", source_path)
    return []


def extract_functions(filepath: str) -> list[dict]:
    """Extract function and class definitions from a Python file using AST."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            source = f.read()
    except Exception as e:
        logger.error("Could not read %s: %s", filepath, e)
        return []

    try:
        tree = ast.parse(source, filename=filepath)
    except SyntaxError as e:
        logger.warning("Syntax error in %s: %s", filepath, e)
        return []

    items = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_info = {
                "type": "function",
                "name": node.name,
                "lineno": node.lineno,
                "args": [],
                "returns": None,
                "docstring": ast.get_docstring(node) or "",
                "decorators": [],
                "is_async": isinstance(node, ast.AsyncFunctionDef),
            }
            for d in node.decorator_list:
                try:
                    func_info["decorators"].append(ast.unparse(d))
                except Exception:
                    pass
            for arg in node.args.args:
                arg_info = {"name": arg.arg, "annotation": ""}
                if arg.annotation:
                    try:
                        arg_info["annotation"] = ast.unparse(arg.annotation)
                    except Exception:
                        pass
                func_info["args"].append(arg_info)
            if node.returns:
                try:
                    func_info["returns"] = ast.unparse(node.returns)
                except Exception:
                    pass
            items.append(func_info)

        elif isinstance(node, ast.ClassDef):
            class_info = {
                "type": "class",
                "name": node.name,
                "lineno": node.lineno,
                "docstring": ast.get_docstring(node) or "",
                "bases": [],
                "methods": [],
            }
            for base in node.bases:
                try:
                    class_info["bases"].append(ast.unparse(base))
                except Exception:
                    pass
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    method_info = {
                        "name": item.name,
                        "args": [a.arg for a in item.args.args if a.arg != "self"],
                        "docstring": ast.get_docstring(item) or "",
                        "returns": None,
                    }
                    if item.returns:
                        try:
                            method_info["returns"] = ast.unparse(item.returns)
                        except Exception:
                            pass
                    class_info["methods"].append(method_info)
            items.append(class_info)

    return items


def format_extracted_info(filepath: str, items: list[dict]) -> str:
    """Format extracted items into a prompt-friendly string."""
    lines = [f"## File: {os.path.basename(filepath)}\n"]
    for item in items:
        if item["type"] == "function":
            async_prefix = "async " if item.get("is_async") else ""
            args_str = ", ".join(
                f"{a['name']}: {a['annotation']}" if a["annotation"] else a["name"]
                for a in item["args"]
            )
            returns = f" -> {item['returns']}" if item["returns"] else ""
            decorators = " ".join(f"@{d}" for d in item.get("decorators", []))
            if decorators:
                lines.append(decorators)
            lines.append(f"### {async_prefix}def {item['name']}({args_str}){returns}")
            if item["docstring"]:
                lines.append(f"Docstring: {item['docstring']}")
            lines.append(f"Line: {item['lineno']}\n")
        elif item["type"] == "class":
            bases = f"({', '.join(item['bases'])})" if item["bases"] else ""
            lines.append(f"### class {item['name']}{bases}")
            if item["docstring"]:
                lines.append(f"Docstring: {item['docstring']}")
            for method in item["methods"]:
                args = ", ".join(method["args"])
                returns = f" -> {method['returns']}" if method.get("returns") else ""
                lines.append(f"  - {method['name']}({args}){returns}")
                if method["docstring"]:
                    lines.append(f"    {method['docstring']}")
            lines.append("")
    return "\n".join(lines)


def generate_openapi_skeleton(items: list[dict], title: str = "API") -> dict:
    """Generate an OpenAPI 3.0 skeleton from extracted functions."""
    spec = {
        "openapi": "3.0.0",
        "info": {"title": title, "version": "1.0.0", "description": f"API documentation for {title}"},
        "paths": {},
    }
    for item in items:
        if item["type"] == "function" and not item["name"].startswith("_"):
            path = f"/{item['name']}"
            params = []
            for arg in item.get("args", []):
                if arg["name"] not in ("self", "cls"):
                    params.append({
                        "name": arg["name"],
                        "in": "query",
                        "required": True,
                        "schema": {"type": "string"},
                        "description": arg.get("annotation", ""),
                    })
            spec["paths"][path] = {
                "get": {
                    "summary": item.get("docstring", item["name"]),
                    "parameters": params,
                    "responses": {"200": {"description": "Success"}},
                }
            }
    return spec
