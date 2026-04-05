"""Core business logic for CI/CD Pipeline generation."""

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

SYSTEM_PROMPT = """You are a DevOps engineer expert in CI/CD pipelines. Generate production-ready
pipeline configurations following best practices:
1. Use caching for dependencies
2. Run jobs in parallel where possible
3. Add proper environment variables and secrets handling
4. Include artifact uploading
5. Add conditional deployments per environment
6. Use matrix builds for multiple versions when appropriate
7. Add proper timeouts and retry mechanisms
8. Follow the platform's best practices and latest syntax

Output ONLY valid configuration unless asked for explanation."""

# ---------------------------------------------------------------------------
# Platform Registry
# ---------------------------------------------------------------------------

PLATFORMS = {
    "github-actions": {
        "name": "GitHub Actions",
        "ext": "yml",
        "lang": "yaml",
        "config_path": ".github/workflows/ci.yml",
        "docs_url": "https://docs.github.com/en/actions",
    },
    "gitlab-ci": {
        "name": "GitLab CI",
        "ext": "yml",
        "lang": "yaml",
        "config_path": ".gitlab-ci.yml",
        "docs_url": "https://docs.gitlab.com/ee/ci/",
    },
    "jenkins": {
        "name": "Jenkins",
        "ext": "groovy",
        "lang": "groovy",
        "config_path": "Jenkinsfile",
        "docs_url": "https://www.jenkins.io/doc/book/pipeline/",
    },
    "azure-pipelines": {
        "name": "Azure Pipelines",
        "ext": "yml",
        "lang": "yaml",
        "config_path": "azure-pipelines.yml",
        "docs_url": "https://learn.microsoft.com/en-us/azure/devops/pipelines/",
    },
    "circleci": {
        "name": "CircleCI",
        "ext": "yml",
        "lang": "yaml",
        "config_path": ".circleci/config.yml",
        "docs_url": "https://circleci.com/docs/",
    },
}

LANGUAGES = [
    "python", "javascript", "typescript", "java", "go", "rust", "ruby",
    "csharp", "php", "kotlin", "swift",
]

# ---------------------------------------------------------------------------
# Pipeline Stages
# ---------------------------------------------------------------------------

STAGE_CATALOG = {
    "lint": {"description": "Code linting & static analysis", "order": 1},
    "test": {"description": "Unit & integration tests", "order": 2},
    "security": {"description": "Security scanning (SAST/DAST)", "order": 3},
    "build": {"description": "Build artifacts / Docker images", "order": 4},
    "publish": {"description": "Publish packages / push images", "order": 5},
    "deploy-staging": {"description": "Deploy to staging environment", "order": 6},
    "integration-test": {"description": "Run integration tests on staging", "order": 7},
    "deploy-production": {"description": "Deploy to production", "order": 8},
    "notify": {"description": "Send notifications (Slack, email)", "order": 9},
}

# ---------------------------------------------------------------------------
# Secret Templates
# ---------------------------------------------------------------------------

SECRET_TEMPLATES = {
    "github-actions": {
        "docker": ["DOCKER_USERNAME", "DOCKER_PASSWORD"],
        "aws": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_REGION"],
        "npm": ["NPM_TOKEN"],
        "pypi": ["PYPI_TOKEN"],
        "slack": ["SLACK_WEBHOOK_URL"],
    },
    "gitlab-ci": {
        "docker": ["CI_REGISTRY_USER", "CI_REGISTRY_PASSWORD"],
        "aws": ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"],
    },
}

# ---------------------------------------------------------------------------
# Matrix Build Presets
# ---------------------------------------------------------------------------

MATRIX_PRESETS = {
    "python": {"versions": ["3.10", "3.11", "3.12"], "os": ["ubuntu-latest"]},
    "javascript": {"versions": ["18", "20", "22"], "os": ["ubuntu-latest"]},
    "java": {"versions": ["17", "21"], "os": ["ubuntu-latest"]},
    "go": {"versions": ["1.21", "1.22"], "os": ["ubuntu-latest"]},
    "rust": {"versions": ["stable", "nightly"], "os": ["ubuntu-latest"]},
}


def get_platforms() -> dict:
    """Return all supported CI/CD platforms."""
    return PLATFORMS


def get_stage_catalog() -> dict:
    """Return available pipeline stages."""
    return STAGE_CATALOG


def get_secret_template(platform: str) -> dict:
    """Return secret templates for a platform."""
    return SECRET_TEMPLATES.get(platform, {})


def get_matrix_preset(language: str) -> dict:
    """Return matrix build preset for a language."""
    return MATRIX_PRESETS.get(language, {"versions": ["latest"], "os": ["ubuntu-latest"]})


def generate_pipeline(
    platform: str,
    language: str,
    steps: str,
    project_name: Optional[str] = None,
    matrix: bool = False,
    secrets: Optional[list] = None,
) -> str:
    """Generate a CI/CD pipeline configuration.

    Args:
        platform: Target CI/CD platform key.
        language: Project programming language.
        steps: Comma-separated pipeline steps.
        project_name: Optional project name for labeling.
        matrix: Enable matrix builds.
        secrets: List of secret categories to include.

    Returns:
        Generated pipeline configuration.
    """
    logger.info("Generating pipeline: platform=%s lang=%s steps=%s", platform, language, steps)

    platform_info = PLATFORMS.get(platform, PLATFORMS["github-actions"])
    project_str = f"\nProject name: {project_name}" if project_name else ""

    matrix_str = ""
    if matrix:
        preset = get_matrix_preset(language)
        matrix_str = f"\nMatrix build: test across versions {preset['versions']} on {preset['os']}"

    secret_str = ""
    if secrets:
        secret_vars = []
        templates = get_secret_template(platform)
        for cat in secrets:
            secret_vars.extend(templates.get(cat, []))
        if secret_vars:
            secret_str = f"\nRequired secrets: {', '.join(secret_vars)}"

    prompt = f"""Generate a complete {platform_info['name']} CI/CD pipeline configuration.
Language: {language}
Pipeline steps: {steps}{project_str}{matrix_str}{secret_str}

Include proper caching, artifact handling, and environment setup.
Output only the configuration file content."""

    result = chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=3000,
    )
    logger.info("Pipeline generation complete")
    return result


def explain_pipeline(config_content: str, platform: Optional[str] = None) -> str:
    """Explain an existing pipeline configuration.

    Args:
        config_content: Pipeline configuration content.
        platform: Optional platform hint.

    Returns:
        Human-readable explanation.
    """
    logger.info("Explaining pipeline (%d chars)", len(config_content))
    platform_hint = f" (Platform: {platform})" if platform else ""

    prompt = f"""Explain this CI/CD pipeline configuration{platform_hint} in plain English.
Describe each stage, job, step, and how they work together.

{config_content}"""

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.4,
        max_tokens=2048,
    )


def extract_config(text: str) -> str:
    """Extract configuration content from LLM response.

    Args:
        text: Raw LLM response.

    Returns:
        Clean configuration content.
    """
    for fence in ["```yaml", "```yml", "```groovy", "```"]:
        if fence in text:
            start = text.index(fence) + len(fence)
            remaining = text[start:]
            end = remaining.index("```") if "```" in remaining else len(remaining)
            return remaining[:end].strip()
    return text.strip()


def validate_pipeline_config(config_text: str, platform: str) -> dict:
    """Basic validation of pipeline config.

    Args:
        config_text: Pipeline configuration text.
        platform: Target platform.

    Returns:
        Dict with 'valid' bool and 'warnings' list.
    """
    warnings = []
    platform_info = PLATFORMS.get(platform, {})

    if platform_info.get("lang") == "yaml":
        try:
            data = yaml.safe_load(config_text)
            if not isinstance(data, dict):
                warnings.append("Root element is not a mapping")
        except yaml.YAMLError as exc:
            warnings.append(f"YAML parse error: {exc}")

    if not config_text.strip():
        warnings.append("Configuration is empty")

    return {"valid": len(warnings) == 0, "warnings": warnings}
