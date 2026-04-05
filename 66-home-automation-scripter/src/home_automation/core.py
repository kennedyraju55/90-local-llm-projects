#!/usr/bin/env python3
"""Core business logic for Home Automation Scripter."""

from typing import Optional, List, Dict, Any, Tuple, Union
import sys
import os
import json
import logging
import re
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate

import yaml

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Platform templates
# ---------------------------------------------------------------------------

PLATFORM_TEMPLATES = {
    "homeassistant": {
        "name": "Home Assistant",
        "format": "YAML automation",
        "description": "Home Assistant automation YAML configuration",
    },
    "ifttt": {
        "name": "IFTTT",
        "format": "IFTTT applet rule",
        "description": "IFTTT-style If-This-Then-That rules",
    },
    "openhab": {
        "name": "openHAB",
        "format": "openHAB rule DSL",
        "description": "openHAB automation rules in DSL format",
    },
    "nodered": {
        "name": "Node-RED",
        "format": "Node-RED flow JSON",
        "description": "Node-RED flow configuration",
    },
    "smartthings": {
        "name": "SmartThings",
        "format": "SmartThings Groovy SmartApp / Rules API JSON",
        "description": "Samsung SmartThings automation rules",
    },
}

# ---------------------------------------------------------------------------
# Pre-built script templates
# ---------------------------------------------------------------------------

SCRIPT_TEMPLATES = {
    "motion_light": {
        "name": "Motion-Activated Light",
        "category": "lighting",
        "description": "Turn on a light when motion is detected and off after a delay.",
        "parameters": ["motion_sensor", "light_entity", "delay_minutes"],
        "template": {
            "homeassistant": (
                "automation:\n"
                "  - alias: 'Motion Light'\n"
                "    trigger:\n"
                "      platform: state\n"
                "      entity_id: {motion_sensor}\n"
                "      to: 'on'\n"
                "    action:\n"
                "      - service: light.turn_on\n"
                "        entity_id: {light_entity}\n"
                "      - delay:\n"
                "          minutes: {delay_minutes}\n"
                "      - service: light.turn_off\n"
                "        entity_id: {light_entity}\n"
            ),
        },
    },
    "thermostat_schedule": {
        "name": "Thermostat Schedule",
        "category": "climate",
        "description": "Set thermostat temperature based on time of day.",
        "parameters": ["thermostat_entity", "day_temp", "night_temp", "day_start", "night_start"],
        "template": {
            "homeassistant": (
                "automation:\n"
                "  - alias: 'Daytime Temperature'\n"
                "    trigger:\n"
                "      platform: time\n"
                "      at: '{day_start}'\n"
                "    action:\n"
                "      service: climate.set_temperature\n"
                "      data:\n"
                "        entity_id: {thermostat_entity}\n"
                "        temperature: {day_temp}\n"
                "  - alias: 'Nighttime Temperature'\n"
                "    trigger:\n"
                "      platform: time\n"
                "      at: '{night_start}'\n"
                "    action:\n"
                "      service: climate.set_temperature\n"
                "      data:\n"
                "        entity_id: {thermostat_entity}\n"
                "        temperature: {night_temp}\n"
            ),
        },
    },
    "security_alert": {
        "name": "Security Alert",
        "category": "security",
        "description": "Send a notification when a door or window opens while away.",
        "parameters": ["door_sensor", "notification_service"],
        "template": {
            "homeassistant": (
                "automation:\n"
                "  - alias: 'Security Alert'\n"
                "    trigger:\n"
                "      platform: state\n"
                "      entity_id: {door_sensor}\n"
                "      to: 'on'\n"
                "    condition:\n"
                "      condition: state\n"
                "      entity_id: group.family\n"
                "      state: 'not_home'\n"
                "    action:\n"
                "      service: {notification_service}\n"
                "      data:\n"
                "        message: 'ALERT: {{{{ states.{door_sensor}.name }}}} opened while away!'\n"
            ),
        },
    },
    "good_morning": {
        "name": "Good Morning Routine",
        "category": "routine",
        "description": "Run a morning routine: lights on, thermostat up, news briefing.",
        "parameters": ["wake_time", "light_entity", "thermostat_entity", "morning_temp"],
        "template": {
            "homeassistant": (
                "automation:\n"
                "  - alias: 'Good Morning'\n"
                "    trigger:\n"
                "      platform: time\n"
                "      at: '{wake_time}'\n"
                "    action:\n"
                "      - service: light.turn_on\n"
                "        entity_id: {light_entity}\n"
                "        data:\n"
                "          brightness_pct: 60\n"
                "          color_temp: 350\n"
                "      - service: climate.set_temperature\n"
                "        data:\n"
                "          entity_id: {thermostat_entity}\n"
                "          temperature: {morning_temp}\n"
            ),
        },
    },
    "energy_saver": {
        "name": "Energy Saver",
        "category": "energy",
        "description": "Turn off all non-essential devices when no one is home.",
        "parameters": ["presence_entity", "light_group", "media_player"],
        "template": {
            "homeassistant": (
                "automation:\n"
                "  - alias: 'Energy Saver - Away'\n"
                "    trigger:\n"
                "      platform: state\n"
                "      entity_id: {presence_entity}\n"
                "      to: 'not_home'\n"
                "      for:\n"
                "        minutes: 10\n"
                "    action:\n"
                "      - service: light.turn_off\n"
                "        entity_id: {light_group}\n"
                "      - service: media_player.turn_off\n"
                "        entity_id: {media_player}\n"
                "      - service: climate.set_preset_mode\n"
                "        data:\n"
                "          preset_mode: eco\n"
            ),
        },
    },
    "bedtime": {
        "name": "Bedtime Routine",
        "category": "routine",
        "description": "Gradually dim lights, lock doors, and lower thermostat at bedtime.",
        "parameters": ["bedtime", "light_group", "lock_entity", "night_temp", "thermostat_entity"],
        "template": {
            "homeassistant": (
                "automation:\n"
                "  - alias: 'Bedtime Routine'\n"
                "    trigger:\n"
                "      platform: time\n"
                "      at: '{bedtime}'\n"
                "    action:\n"
                "      - service: light.turn_on\n"
                "        entity_id: {light_group}\n"
                "        data:\n"
                "          brightness_pct: 10\n"
                "          transition: 300\n"
                "      - delay:\n"
                "          minutes: 5\n"
                "      - service: light.turn_off\n"
                "        entity_id: {light_group}\n"
                "      - service: lock.lock\n"
                "        entity_id: {lock_entity}\n"
                "      - service: climate.set_temperature\n"
                "        data:\n"
                "          entity_id: {thermostat_entity}\n"
                "          temperature: {night_temp}\n"
            ),
        },
    },
}

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = {
    "llm": {"model": "llama3.2", "temperature": 0.4, "max_tokens": 2000},
    "platforms": ["homeassistant", "ifttt", "smartthings", "openhab", "nodered"],
    "default_platform": "homeassistant",
    "rules_file": "automation_rules.json",
    "templates_dir": "templates",
    "logging": {"level": "INFO", "file": "home_automation.log"},
    "scheduling": {"enabled": False, "cron_format": True},
}


def load_config(config_path: str | None = None) -> dict:
    """Load configuration from a YAML file, falling back to defaults."""
    config = dict(DEFAULT_CONFIG)
    if config_path and os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = yaml.safe_load(f) or {}
            config.update(user_config)
            logger.info("Loaded config from %s", config_path)
        except Exception as exc:
            logger.warning("Failed to load config %s: %s", config_path, exc)
    return config


# ---------------------------------------------------------------------------
# Rules persistence
# ---------------------------------------------------------------------------


def _rules_path(config: dict | None = None) -> str:
    """Rules path."""
    if config and "rules_file" in config:
        return config["rules_file"]
    return DEFAULT_CONFIG["rules_file"]


def load_rules(config: dict | None = None) -> list[dict]:
    """Load saved automation rules from JSON."""
    path = _rules_path(config)
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                rules = json.load(f)
            logger.info("Loaded %d rules from %s", len(rules), path)
            return rules
        except (json.JSONDecodeError, IOError) as exc:
            logger.warning("Failed to read rules file %s: %s", path, exc)
            return []
    return []


def save_rule(rule: dict, config: dict | None = None) -> dict:
    """Persist a new automation rule and return it with id/timestamp."""
    rules = load_rules(config)
    rule["id"] = len(rules) + 1
    rule["created"] = datetime.now().isoformat()
    rules.append(rule)
    path = _rules_path(config)
    with open(path, "w") as f:
        json.dump(rules, f, indent=2)
    logger.info("Saved rule #%d to %s", rule["id"], path)
    return rule


def delete_rule(rule_id: int, config: dict | None = None) -> bool:
    """Delete a rule by its integer id. Returns True if found and deleted."""
    rules = load_rules(config)
    new_rules = [r for r in rules if r.get("id") != rule_id]
    if len(new_rules) == len(rules):
        logger.warning("Rule %d not found", rule_id)
        return False
    path = _rules_path(config)
    with open(path, "w") as f:
        json.dump(new_rules, f, indent=2)
    logger.info("Deleted rule #%d", rule_id)
    return True


# ---------------------------------------------------------------------------
# Script validation
# ---------------------------------------------------------------------------

_VALIDATORS = {
    "homeassistant": [
        (r"(automation|trigger|action|alias):", "Missing required HA keys"),
    ],
    "ifttt": [
        (r"(IF|THEN|if|then)", "Missing IF/THEN structure"),
    ],
    "openhab": [
        (r"(rule|when|then|end)", "Missing openHAB rule structure"),
    ],
    "nodered": [
        (r'"(id|type|wires)"', "Missing Node-RED flow keys"),
    ],
    "smartthings": [
        (r"(name|actions|if|SmartApp)", "Missing SmartThings structure"),
    ],
}


def validate_script(script: str, platform: str) -> dict:
    """Validate an automation script for a given platform.

    Returns a dict with keys ``valid`` (bool), ``errors`` (list[str]),
    and ``warnings`` (list[str]).
    """
    errors: list[str] = []
    warnings: list[str] = []

    if not script or not script.strip():
        return {"valid": False, "errors": ["Script is empty"], "warnings": []}

    checks = _VALIDATORS.get(platform, [])
    for pattern, msg in checks:
        if not re.search(pattern, script):
            errors.append(msg)

    if len(script.strip().splitlines()) < 2:
        warnings.append("Script seems very short – verify completeness")

    valid = len(errors) == 0
    level = "INFO" if valid else "WARNING"
    logger.log(logging.getLevelName(level), "Validation for %s: valid=%s errors=%s", platform, valid, errors)
    return {"valid": valid, "errors": errors, "warnings": warnings}


# ---------------------------------------------------------------------------
# Template library helpers
# ---------------------------------------------------------------------------


def list_templates(category: str | None = None) -> list[dict]:
    """Return template metadata, optionally filtered by category."""
    results = []
    for key, tpl in SCRIPT_TEMPLATES.items():
        if category and tpl["category"] != category:
            continue
        results.append({
            "id": key,
            "name": tpl["name"],
            "category": tpl["category"],
            "description": tpl["description"],
            "parameters": tpl["parameters"],
        })
    logger.debug("list_templates(category=%s) -> %d results", category, len(results))
    return results


def get_template(template_id: str) -> dict | None:
    """Get a single template by id."""
    tpl = SCRIPT_TEMPLATES.get(template_id)
    if tpl is None:
        logger.warning("Template '%s' not found", template_id)
        return None
    return {"id": template_id, **tpl}


def get_template_categories() -> list[str]:
    """Return sorted unique categories across all templates."""
    return sorted({t["category"] for t in SCRIPT_TEMPLATES.values()})


def generate_from_template(template_id: str, platform: str, params: dict) -> str | None:
    """Fill a template with user-provided parameters.

    Returns the rendered script string, or ``None`` if the template
    does not support the requested platform.
    """
    tpl = SCRIPT_TEMPLATES.get(template_id)
    if tpl is None:
        logger.error("Template '%s' not found", template_id)
        return None
    platform_tpl = tpl["template"].get(platform)
    if platform_tpl is None:
        logger.warning("Template '%s' has no variant for platform '%s'", template_id, platform)
        return None
    try:
        rendered = platform_tpl.format(**params)
        logger.info("Generated script from template '%s' for platform '%s'", template_id, platform)
        return rendered
    except KeyError as exc:
        logger.error("Missing parameter %s for template '%s'", exc, template_id)
        return None


# ---------------------------------------------------------------------------
# LLM-powered generation helpers
# ---------------------------------------------------------------------------


def detect_syntax(script: str) -> str:
    """Detect the syntax language for rich output."""
    if "automation:" in script or "trigger:" in script:
        return "yaml"
    if "{" in script and "}" in script:
        return "json"
    return "yaml"


def generate_automation(rule_description: str, platform: str, config: dict | None = None) -> str:
    """Generate a home automation script from a natural language description."""
    platform_info = PLATFORM_TEMPLATES.get(platform, PLATFORM_TEMPLATES["homeassistant"])
    temperature = (config or {}).get("llm", {}).get("temperature", 0.4)

    prompt = (
        f"Convert this natural language rule into a {platform_info['name']} automation script:\n\n"
        f'Rule: "{rule_description}"\n\n'
        f"Platform: {platform_info['name']}\n"
        f"Format: {platform_info['format']}\n\n"
        "Requirements:\n"
        f"1. Generate a complete, valid automation script\n"
        "2. Include appropriate triggers, conditions, and actions\n"
        "3. Add helpful comments explaining each section\n"
        f"4. Follow best practices for {platform_info['name']}\n"
        "5. Include error handling where applicable\n"
        "6. Make it production-ready\n\n"
        "Provide the complete script/configuration code."
    )

    logger.info("Generating %s automation for: %s", platform, rule_description[:60])
    return generate(
        prompt=prompt,
        system_prompt=(
            f"You are an expert {platform_info['name']} automation developer. "
            "Generate clean, production-ready automation scripts."
        ),
        temperature=temperature,
    )


def explain_automation(script: str, platform: str, config: dict | None = None) -> str:
    """Explain what an automation script does in plain language."""
    temperature = (config or {}).get("llm", {}).get("temperature", 0.5)

    prompt = (
        f"Explain this {platform} automation script in simple terms:\n\n"
        f"{script}\n\n"
        "Provide:\n"
        "1. **What it does**: Plain language description\n"
        "2. **Trigger**: What starts the automation\n"
        "3. **Conditions**: Any conditions that must be met\n"
        "4. **Actions**: What happens when triggered\n"
        "5. **Potential Issues**: Things to watch out for"
    )

    logger.info("Explaining %s script (%d chars)", platform, len(script))
    return generate(
        prompt=prompt,
        system_prompt="You are a home automation expert who explains technical scripts in simple terms.",
        temperature=temperature,
    )


def suggest_automations(devices: str, config: dict | None = None) -> str:
    """Suggest useful automations based on available devices."""
    temperature = (config or {}).get("llm", {}).get("temperature", 0.7)

    prompt = (
        f"Based on these smart home devices: {devices}\n\n"
        "Suggest 5 useful home automation rules:\n\n"
        "For each suggestion provide:\n"
        "1. **Name**: Short descriptive name\n"
        "2. **Description**: What it does in natural language\n"
        "3. **Trigger**: What starts it\n"
        "4. **Action**: What it does\n"
        "5. **Benefit**: Why it's useful (comfort, energy saving, security)\n\n"
        "Format as a numbered list in markdown."
    )

    logger.info("Suggesting automations for devices: %s", devices[:80])
    return generate(
        prompt=prompt,
        system_prompt="You are a smart home consultant who suggests practical and useful automations.",
        temperature=temperature,
    )
