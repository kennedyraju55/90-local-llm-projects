"""Core business logic for Infrastructure Documentation generation."""

import logging
import os
import sys
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import chat, check_ollama_running

logger = logging.getLogger(__name__)

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")


def load_config() -> dict:
    """Load application configuration from config.yaml."""
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logger.warning("config.yaml not found, using defaults")
        return {}


CONFIG = load_config()

SYSTEM_PROMPT = """You are a senior infrastructure engineer and technical writer.
Generate clear, comprehensive infrastructure documentation from configuration files.

Your documentation should include:
1. Architecture Overview - high-level description of the infrastructure
2. Component Details - each service/resource with purpose and configuration
3. Network Topology - how components communicate
4. Security Configuration - authentication, access controls, encryption
5. Scaling & Performance - resource limits, replicas, auto-scaling
6. Environment Variables - required configuration with descriptions
7. Dependencies - external services and inter-service dependencies
8. Operational Notes - maintenance, monitoring, backup procedures

Format using clean markdown with proper headings, tables, and code blocks."""

# ---------------------------------------------------------------------------
# Config Type Detection
# ---------------------------------------------------------------------------

CONFIG_TYPES = {
    ".yml": "Docker Compose / Kubernetes / Ansible",
    ".yaml": "Docker Compose / Kubernetes / Ansible",
    ".tf": "Terraform",
    ".hcl": "Terraform / HCL",
    ".json": "CloudFormation / Kubernetes / Config",
    ".toml": "Configuration file",
    ".ini": "Configuration file",
    ".conf": "Server configuration",
    ".dockerfile": "Docker",
}

INPUT_FORMATS = {
    "terraform": {
        "name": "Terraform",
        "extensions": [".tf", ".hcl"],
        "indicators": ["resource ", "provider ", "variable ", "module "],
    },
    "kubernetes": {
        "name": "Kubernetes",
        "extensions": [".yml", ".yaml"],
        "indicators": ["apiVersion:", "kind:", "metadata:"],
    },
    "docker-compose": {
        "name": "Docker Compose",
        "extensions": [".yml", ".yaml"],
        "indicators": ["services:", "image:", "build:"],
    },
    "dockerfile": {
        "name": "Dockerfile",
        "extensions": [".dockerfile", ""],
        "indicators": ["FROM ", "RUN ", "COPY ", "CMD "],
    },
    "ansible": {
        "name": "Ansible",
        "extensions": [".yml", ".yaml"],
        "indicators": ["hosts:", "tasks:", "roles:"],
    },
    "cloudformation": {
        "name": "CloudFormation",
        "extensions": [".json", ".yml", ".yaml"],
        "indicators": ["AWSTemplateFormatVersion", "Resources:"],
    },
}

DOC_FORMATS = ["markdown", "html", "text"]


def detect_config_type(filepath: str, content: str) -> str:
    """Detect the type of infrastructure config file.

    Args:
        filepath: Path to the config file.
        content: File content for analysis.

    Returns:
        Detected config type string.
    """
    basename = os.path.basename(filepath).lower()
    _, ext = os.path.splitext(basename)

    # Filename-based detection
    if "docker-compose" in basename or "compose" in basename:
        return "Docker Compose"
    if basename == "dockerfile" or basename.startswith("dockerfile"):
        return "Dockerfile"
    if ext in (".tf", ".hcl"):
        return "Terraform"
    if "k8s" in basename or "kubernetes" in basename:
        return "Kubernetes"
    if "ansible" in basename or "playbook" in basename:
        return "Ansible"

    # Content-based detection
    for fmt_key, fmt_info in INPUT_FORMATS.items():
        matches = sum(1 for ind in fmt_info["indicators"] if ind in content)
        if matches >= 2:
            return fmt_info["name"]

    if ext in CONFIG_TYPES:
        return CONFIG_TYPES[ext]

    return "Infrastructure configuration"


def extract_dependencies(content: str, config_type: str) -> list:
    """Extract service/resource dependencies from config content.

    Args:
        content: Configuration file content.
        config_type: Detected config type.

    Returns:
        List of dependency relationships as dicts.
    """
    dependencies = []

    if config_type == "Docker Compose":
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict) and "services" in data:
                for svc_name, svc_conf in data["services"].items():
                    if isinstance(svc_conf, dict):
                        for dep in svc_conf.get("depends_on", []):
                            dep_name = dep if isinstance(dep, str) else str(dep)
                            dependencies.append({"from": svc_name, "to": dep_name, "type": "depends_on"})
                        for link in svc_conf.get("links", []):
                            dependencies.append({"from": svc_name, "to": link, "type": "link"})
        except yaml.YAMLError:
            pass

    if config_type == "Kubernetes":
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict):
                kind = data.get("kind", "")
                name = data.get("metadata", {}).get("name", "unknown")
                dependencies.append({"from": name, "to": kind, "type": "resource"})
        except yaml.YAMLError:
            pass

    return dependencies


def generate_docs(
    content: str,
    config_type: str,
    output_format: str = "markdown",
    include_diagram: bool = False,
) -> str:
    """Generate documentation from an infrastructure config file.

    Args:
        content: Config file content.
        config_type: Type of configuration (Docker, Terraform, etc.).
        output_format: Output format (markdown, html, text).
        include_diagram: Whether to include architecture diagram.

    Returns:
        Generated documentation.
    """
    logger.info("Generating docs for config_type=%s format=%s", config_type, output_format)

    diagram_instruction = ""
    if include_diagram:
        diagram_instruction = "\nAlso include a text-based architecture diagram showing components and connections."

    prompt = f"""Generate comprehensive infrastructure documentation for this {config_type} configuration.
Output format: {output_format}
{diagram_instruction}

CONFIGURATION:
{content}

Include architecture overview, component details, networking, security, dependencies, and operational notes."""

    result = chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=3000,
    )
    logger.info("Documentation generation complete")
    return result


def generate_diagram(content: str, config_type: str) -> str:
    """Generate an architecture diagram description.

    Args:
        content: Config file content.
        config_type: Type of configuration.

    Returns:
        Text-based architecture diagram.
    """
    logger.info("Generating diagram for config_type=%s", config_type)
    prompt = f"""Create a text-based architecture diagram for this {config_type} configuration.
Use ASCII art or a structured representation showing:
- Components and their relationships
- Network connections and ports
- Data flow between services
- Dependency arrows

CONFIGURATION:
{content}"""

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )


def generate_dependency_map(content: str, config_type: str) -> str:
    """Generate a dependency map from configuration.

    Args:
        content: Config file content.
        config_type: Type of configuration.

    Returns:
        Dependency map in text format.
    """
    local_deps = extract_dependencies(content, config_type)
    local_deps_str = ""
    if local_deps:
        local_deps_str = "\n\nLocally detected dependencies:\n" + "\n".join(
            f"- {d['from']} → {d['to']} ({d['type']})" for d in local_deps
        )

    prompt = f"""Analyze this {config_type} configuration and create a comprehensive dependency map.
Show all dependencies between components including:
- Service dependencies
- Network dependencies
- Volume/storage dependencies
- External dependencies
{local_deps_str}

CONFIGURATION:
{content}"""

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )
