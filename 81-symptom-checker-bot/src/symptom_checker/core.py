"""
Symptom Checker Bot - Core Module

AI-powered symptom analysis with urgency scoring, body region mapping,
and medical history tracking.

⚠️ MEDICAL DISCLAIMER: This tool is for EDUCATIONAL and INFORMATIONAL purposes ONLY.
It is NOT a substitute for professional medical advice, diagnosis, or treatment.
ALWAYS consult a qualified healthcare provider for any health concerns.
"""

from typing import Optional, List, Dict, Any, Tuple, Union
import os
import sys
import json
import logging
from datetime import datetime

# ---------------------------------------------------------------------------
# Path setup for shared common module
# ---------------------------------------------------------------------------
_common_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.insert(0, os.path.abspath(_common_path))

from common.llm_client import chat, check_ollama_running  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logger = logging.getLogger("symptom_checker")


def _setup_logging(level: str = "INFO") -> None:
    """Configure logging for the symptom checker."""
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

def load_config() -> dict:
    """Load configuration from config.yaml or use defaults."""
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')
    defaults: dict = {
        "model": "gemma4",
        "temperature": 0.3,
        "max_tokens": 1024,
        "log_level": "INFO",
        "ollama_url": "http://localhost:11434",
    }
    try:
        import yaml
        with open(config_path, 'r') as f:
            user_config = yaml.safe_load(f) or {}
        defaults.update(user_config)
    except (ImportError, FileNotFoundError):
        pass
    return defaults


CONFIG = load_config()
_setup_logging(CONFIG.get("log_level", "INFO"))

# ---------------------------------------------------------------------------
# Medical disclaimer
# ---------------------------------------------------------------------------

DISCLAIMER = """
⚠️  MEDICAL DISCLAIMER  ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This tool is for EDUCATIONAL and INFORMATIONAL purposes ONLY.
It is NOT a substitute for professional medical advice, diagnosis, or treatment.

• Do NOT use this tool to make medical decisions.
• Do NOT delay seeking professional medical care based on this tool's output.
• ALWAYS consult a qualified healthcare professional for health concerns.
• Call emergency services (911) for medical emergencies.

By using this tool, you acknowledge that all information provided is for
educational purposes only and should not be relied upon for medical decisions.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a medical information assistant designed for EDUCATIONAL purposes only.

IMPORTANT RULES:
1. You are NOT a doctor and CANNOT provide medical diagnoses or treatment plans.
2. ALWAYS remind users to consult a healthcare professional.
3. Provide general educational information about symptoms.
4. If symptoms sound serious or life-threatening, strongly urge immediate medical attention.
5. Never prescribe medications or specific treatments.
6. Be empathetic but clear about your limitations.

When analyzing symptoms:
- List possible conditions that commonly present with those symptoms (for educational awareness).
- Suggest general self-care measures (rest, hydration, etc.) where appropriate.
- Clearly state when professional medical evaluation is recommended.
- Note any red-flag symptoms that require urgent attention.

Always end your response with a reminder that this is educational information only."""

# ---------------------------------------------------------------------------
# Symptom database by body region
# ---------------------------------------------------------------------------

SYMPTOM_DATABASE: dict[str, dict] = {
    "head": {
        "symptoms": [
            "headache", "migraine", "dizziness", "blurred vision", "ear pain",
            "sore throat", "runny nose", "sinus pressure", "jaw pain", "neck stiffness",
        ],
        "description": "Head, face, and neck region",
    },
    "chest": {
        "symptoms": [
            "chest pain", "shortness of breath", "cough", "wheezing", "palpitations",
            "heartburn", "chest tightness", "rapid heartbeat",
        ],
        "description": "Chest and respiratory system",
    },
    "abdomen": {
        "symptoms": [
            "stomach pain", "nausea", "vomiting", "diarrhea", "constipation",
            "bloating", "loss of appetite", "acid reflux", "abdominal cramps",
        ],
        "description": "Abdominal and digestive system",
    },
    "limbs": {
        "symptoms": [
            "joint pain", "muscle ache", "swelling", "numbness", "tingling",
            "weakness", "back pain", "knee pain", "shoulder pain",
        ],
        "description": "Arms, legs, back, and joints",
    },
    "general": {
        "symptoms": [
            "fever", "fatigue", "weight loss", "weight gain", "chills",
            "night sweats", "loss of appetite", "dehydration", "malaise",
        ],
        "description": "General/systemic symptoms",
    },
    "skin": {
        "symptoms": [
            "rash", "itching", "hives", "bruising", "dry skin",
            "skin discoloration", "swelling", "wound", "burns",
        ],
        "description": "Skin and external",
    },
    "mental": {
        "symptoms": [
            "anxiety", "depression", "insomnia", "confusion", "memory loss",
            "mood swings", "panic attacks", "stress", "irritability",
        ],
        "description": "Mental health and neurological",
    },
}

# ---------------------------------------------------------------------------
# Urgency scoring
# ---------------------------------------------------------------------------

URGENCY_KEYWORDS: dict[int, list[str]] = {
    5: [
        "chest pain", "difficulty breathing", "severe bleeding", "unconscious",
        "seizure", "stroke symptoms", "anaphylaxis", "suicidal thoughts",
        "severe allergic reaction", "sudden severe headache", "loss of consciousness",
    ],
    4: [
        "high fever", "severe pain", "persistent vomiting", "signs of infection",
        "rapid heartbeat", "severe dehydration", "blood in stool", "blood in urine",
        "sudden vision loss", "severe abdominal pain",
    ],
    3: [
        "moderate pain", "persistent cough", "mild fever", "recurring headache",
        "joint swelling", "skin rash spreading", "persistent fatigue", "dizziness",
    ],
    2: [
        "mild headache", "minor cold", "mild sore throat", "minor muscle ache",
        "mild nausea", "minor skin irritation", "mild fatigue",
    ],
    1: [
        "minor scratch", "mild discomfort", "occasional sneeze", "minor bruise",
    ],
}

URGENCY_LABELS: dict[int, tuple[str, str]] = {
    1: ("🟢 Low", "Self-care likely sufficient. Monitor symptoms."),
    2: ("🟡 Mild", "Consider scheduling a routine appointment if symptoms persist."),
    3: ("🟠 Moderate", "Schedule an appointment with your healthcare provider soon."),
    4: ("🔴 High", "Seek medical attention promptly. Visit urgent care or your doctor today."),
    5: ("🚨 Emergency", "SEEK IMMEDIATE MEDICAL ATTENTION. Call emergency services if needed."),
}


def assess_urgency(symptoms_text: str) -> tuple[int, str, str]:
    """Assess urgency level based on symptom keywords.

    Returns:
        (level, label, advice) where level is 1-5.
    """
    text_lower = symptoms_text.lower()
    highest_level = 1

    for level in sorted(URGENCY_KEYWORDS.keys(), reverse=True):
        for keyword in URGENCY_KEYWORDS[level]:
            if keyword in text_lower:
                if level > highest_level:
                    highest_level = level
                    logger.debug("Matched urgency keyword '%s' at level %d", keyword, level)
                break  # one match per level is enough

    label, advice = URGENCY_LABELS[highest_level]
    logger.info("Urgency assessment: level=%d label=%s", highest_level, label)
    return highest_level, label, advice


def get_body_regions(symptoms_text: str) -> list[str]:
    """Identify which body regions are affected by the described symptoms."""
    text_lower = symptoms_text.lower()
    affected: list[str] = []

    for region, data in SYMPTOM_DATABASE.items():
        for symptom in data["symptoms"]:
            if symptom in text_lower:
                if region not in affected:
                    affected.append(region)
                break

    if not affected:
        affected.append("general")

    logger.debug("Detected body regions: %s", affected)
    return affected


# ---------------------------------------------------------------------------
# Medical history tracker
# ---------------------------------------------------------------------------

class MedicalHistoryTracker:
    """Track symptom history across a session."""

    def __init__(self) -> None:
        """Init."""
        self.entries: list[dict] = []

    def add_entry(
        self,
        symptoms: str,
        urgency: int,
        regions: list[str],
        response: str,
    ) -> None:
        """Add a symptom check entry to history."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "symptoms": symptoms,
            "urgency": urgency,
            "regions": regions,
            "response": response,
        }
        self.entries.append(entry)
        logger.info("Added history entry (total: %d)", len(self.entries))

    def get_history(self) -> list[dict]:
        """Get all history entries."""
        return list(self.entries)

    def get_summary(self) -> dict:
        """Get a summary of symptom history."""
        if not self.entries:
            return {
                "total_checks": 0,
                "max_urgency": 0,
                "regions_affected": [],
                "all_symptoms": [],
            }

        all_regions: list[str] = []
        all_symptoms: list[str] = []
        max_urgency = 0

        for entry in self.entries:
            for r in entry.get("regions", []):
                if r not in all_regions:
                    all_regions.append(r)
            all_symptoms.append(entry["symptoms"])
            if entry["urgency"] > max_urgency:
                max_urgency = entry["urgency"]

        return {
            "total_checks": len(self.entries),
            "max_urgency": max_urgency,
            "regions_affected": all_regions,
            "all_symptoms": all_symptoms,
        }


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def display_disclaimer() -> None:
    """Display the medical disclaimer using rich formatting."""
    from rich.console import Console
    from rich.panel import Panel

    console = Console()
    console.print(Panel(DISCLAIMER, title="⚕️  Medical Disclaimer", border_style="red"))


# ---------------------------------------------------------------------------
# Symptom checking via LLM
# ---------------------------------------------------------------------------

def check_symptoms(
    symptoms: str,
    conversation_history: list[dict] | None = None,
) -> str:
    """Analyse symptoms using the LLM and return the response text.

    Args:
        symptoms: free-text description of symptoms.
        conversation_history: optional prior messages for multi-turn chat.

    Returns:
        LLM response text (educational information only).
    """
    if conversation_history is None:
        conversation_history = []

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(conversation_history)
    messages.append({"role": "user", "content": symptoms})

    logger.info("Sending symptom query to LLM (%d prior messages)", len(conversation_history))

    try:
        response = chat(messages)
        logger.info("Received LLM response (%d chars)", len(response))
        return response
    except Exception as exc:
        logger.error("LLM call failed: %s", exc)
        raise
