"""Core business logic for Environment Config management."""

import logging
import os
import re
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

SYSTEM_PROMPT = """You are a DevOps and security engineer specializing in environment configuration.
You help teams manage .env files and environment variables securely. You:
1. Validate environment configurations for completeness
2. Identify security issues (exposed secrets, weak values, missing encryption)
3. Suggest missing variables based on project type
4. Recommend best practices for secret management
5. Generate environment templates for common project types
6. Compare environments and identify discrepancies

Follow 12-factor app methodology and security best practices.
Format your response using markdown."""

# ---------------------------------------------------------------------------
# Project Types
# ---------------------------------------------------------------------------

PROJECT_TYPES = [
    "flask", "django", "fastapi", "express", "nextjs", "rails",
    "spring-boot", "laravel", "dotnet", "generic",
]

# ---------------------------------------------------------------------------
# Secret Detection Patterns
# ---------------------------------------------------------------------------

SECRET_PATTERNS = {
    "api_key": re.compile(r"(API[_-]?KEY|APIKEY)", re.IGNORECASE),
    "password": re.compile(r"(PASSWORD|PASSWD|PASS)", re.IGNORECASE),
    "secret": re.compile(r"(SECRET|PRIVATE)", re.IGNORECASE),
    "token": re.compile(r"(TOKEN|JWT|BEARER)", re.IGNORECASE),
    "database_url": re.compile(r"(DATABASE[_-]?URL|DB[_-]?URI|CONNECTION[_-]?STRING)", re.IGNORECASE),
    "aws": re.compile(r"(AWS[_-]?(ACCESS|SECRET|KEY))", re.IGNORECASE),
    "ssh_key": re.compile(r"(SSH[_-]?KEY|RSA[_-]?KEY)", re.IGNORECASE),
    "encryption": re.compile(r"(ENCRYPT|CIPHER|HMAC)", re.IGNORECASE),
}

WEAK_VALUES = {"password", "secret", "changeme", "admin", "test", "123456", "default", "example", "todo", "fixme"}


def parse_env_file(filepath: str) -> dict:
    """Parse a .env file into key-value pairs.

    Args:
        filepath: Path to .env file.

    Returns:
        Dictionary of environment variable names to values.
    """
    env_vars = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                env_vars[key] = value
    return env_vars


def detect_secrets(env_vars: dict) -> list:
    """Detect potential secrets in environment variables.

    Args:
        env_vars: Dict of env var names to values.

    Returns:
        List of security finding dicts.
    """
    findings = []
    for key, value in env_vars.items():
        for pattern_name, pattern in SECRET_PATTERNS.items():
            if pattern.search(key):
                finding = {
                    "variable": key,
                    "type": pattern_name,
                    "severity": "info",
                    "message": f"`{key}` appears to be a secret ({pattern_name})",
                }
                if not value:
                    finding["severity"] = "warning"
                    finding["message"] = f"`{key}` is a secret but has an empty value"
                elif value.lower() in WEAK_VALUES:
                    finding["severity"] = "critical"
                    finding["message"] = f"`{key}` uses a weak/default value: '{value}'"
                elif len(value) < 8:
                    finding["severity"] = "warning"
                    finding["message"] = f"`{key}` secret value is too short ({len(value)} chars)"
                findings.append(finding)
                break
    return findings


def compare_envs(env1: dict, env2: dict) -> dict:
    """Compare two environment configurations.

    Args:
        env1: First env vars dict.
        env2: Second env vars dict.

    Returns:
        Comparison result with keys: only_in_first, only_in_second, different_values, same_values.
    """
    keys1 = set(env1.keys())
    keys2 = set(env2.keys())

    only_in_first = keys1 - keys2
    only_in_second = keys2 - keys1
    common = keys1 & keys2

    different = {k: {"env1": env1[k], "env2": env2[k]} for k in common if env1[k] != env2[k]}
    same = {k for k in common if env1[k] == env2[k]}

    return {
        "only_in_first": sorted(only_in_first),
        "only_in_second": sorted(only_in_second),
        "different_values": different,
        "same_values": sorted(same),
        "total_first": len(keys1),
        "total_second": len(keys2),
    }


def generate_migration_script(env_from: dict, env_to: dict, target_name: str = "target") -> str:
    """Generate a migration script between environments.

    Args:
        env_from: Source environment vars.
        env_to: Target environment vars.
        target_name: Name of target environment.

    Returns:
        Shell script for migration.
    """
    comparison = compare_envs(env_from, env_to)
    lines = [
        "#!/bin/bash",
        f"# Migration script to {target_name} environment",
        f"# Generated by Environment Config Manager",
        "",
        "# Variables to ADD (present in target, missing in source):",
    ]

    for key in comparison["only_in_second"]:
        value = env_to[key]
        is_secret = any(p.search(key) for p in SECRET_PATTERNS.values())
        display_val = "CHANGE_ME" if is_secret else value
        lines.append(f'export {key}="{display_val}"')

    lines.append("")
    lines.append("# Variables with DIFFERENT values:")
    for key, vals in comparison["different_values"].items():
        is_secret = any(p.search(key) for p in SECRET_PATTERNS.values())
        new_val = "CHANGE_ME" if is_secret else vals["env2"]
        lines.append(f'# Was: {vals["env1"] if not is_secret else "***"}')
        lines.append(f'export {key}="{new_val}"')

    if comparison["only_in_first"]:
        lines.append("")
        lines.append("# Variables to REMOVE (present in source, missing in target):")
        for key in comparison["only_in_first"]:
            lines.append(f"unset {key}")

    return "\n".join(lines)


def validate_env(filepath: str) -> str:
    """Validate a .env file for issues and security concerns.

    Args:
        filepath: Path to .env file.

    Returns:
        Validation results with recommendations.
    """
    logger.info("Validating env file: %s", filepath)
    env_vars = parse_env_file(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        raw_content = f.read()

    secret_findings = detect_secrets(env_vars)

    issues = []
    for key, value in env_vars.items():
        if not value:
            issues.append(f"- ⚠️ `{key}` has an empty value")

    for finding in secret_findings:
        icon = "❌" if finding["severity"] == "critical" else "⚠️"
        issues.append(f"- {icon} {finding['message']}")

    local_findings = "\n".join(issues) if issues else "No obvious issues found locally."

    prompt = f"""Validate this .env file for security and completeness issues.

ENV FILE CONTENT:
{raw_content}

LOCAL ANALYSIS FINDINGS:
{local_findings}

Check for:
1. Security issues (exposed secrets, weak values)
2. Missing common variables
3. Naming convention consistency
4. Environment-specific concerns
5. Recommendations for secret management"""

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )


def generate_env_template(project_type: str, env: str = "development") -> str:
    """Generate an .env template for a project type.

    Args:
        project_type: Type of project (flask, django, etc.).
        env: Target environment.

    Returns:
        Generated .env template content.
    """
    logger.info("Generating template: project=%s env=%s", project_type, env)
    prompt = f"""Generate a complete .env file template for a {project_type} project in {env} environment.
Include all common variables with:
- Sensible defaults for {env}
- Comments explaining each variable
- Placeholder values for secrets (marked with CHANGE_ME)
- Grouped by category (app, database, cache, auth, etc.)

Output only the .env file content."""

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )


def suggest_missing_vars(filepath: str, project_type: str) -> str:
    """Suggest missing environment variables based on project type.

    Args:
        filepath: Path to existing .env file.
        project_type: Type of project.

    Returns:
        Suggestions for missing variables.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    prompt = f"""Review this .env file for a {project_type} project and suggest missing variables.
For each suggestion provide: variable name, purpose, recommended value.

CURRENT .ENV:
{content}"""

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=1536,
    )


def generate_env_documentation(filepath: str) -> str:
    """Generate documentation for an .env file.

    Args:
        filepath: Path to .env file.

    Returns:
        Markdown documentation of all variables.
    """
    logger.info("Generating env documentation for: %s", filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    env_vars = parse_env_file(filepath)
    secret_findings = detect_secrets(env_vars)

    prompt = f"""Generate comprehensive markdown documentation for this .env file.
For each variable include:
- Name and type
- Purpose and description
- Default value (mask secrets)
- Required/optional
- Related variables

.ENV FILE:
{content}

DETECTED SECRETS: {[f['variable'] for f in secret_findings]}"""

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )
