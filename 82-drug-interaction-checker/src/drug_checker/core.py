"""
Drug Interaction Checker - Core Logic

⚠️ DISCLAIMER: This tool is for EDUCATIONAL and INFORMATIONAL purposes only.
It is NOT a substitute for professional medical or pharmacological advice.
Always consult a qualified healthcare provider or pharmacist before making
any decisions about your medications.
"""

from typing import Optional, List, Dict, Any, Tuple, Union
import sys
import os
import logging

# ---------------------------------------------------------------------------
# Path setup for shared common module
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import chat, generate, check_ollama_running  # noqa: E402

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
logger = logging.getLogger("drug_checker")

DEFAULT_CONFIG = {
    "model": "gemma4",
    "temperature": 0.2,
    "max_tokens": 1500,
    "log_level": "INFO",
    "ollama_url": "http://localhost:11434",
    "interactions": {
        "include_food": True,
        "include_dosage": True,
        "show_alternatives": True,
        "severity_threshold": "minor",
    },
}


def load_config() -> dict:
    """Load configuration from config.yaml, falling back to defaults."""
    config = DEFAULT_CONFIG.copy()
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')
    try:
        import yaml
        with open(config_path, 'r') as f:
            file_config = yaml.safe_load(f)
        if file_config:
            config.update(file_config)
    except Exception:
        pass
    logging.basicConfig(level=getattr(logging, config.get("log_level", "INFO")))
    return config


CONFIG = load_config()

# ============================================================================
# ⚠️  MEDICAL DISCLAIMER  ⚠️
# ============================================================================
DISCLAIMER = (
    "⚠️  IMPORTANT MEDICAL DISCLAIMER ⚠️\n\n"
    "This drug interaction checker is for EDUCATIONAL and INFORMATIONAL purposes ONLY.\n"
    "It is NOT a substitute for professional medical or pharmacological advice.\n\n"
    "• Do NOT use this tool to make decisions about your medications.\n"
    "• ALWAYS consult a qualified healthcare provider or pharmacist.\n"
    "• Never start, stop, or change medications based on this tool's output.\n"
    "• This tool may miss interactions or provide incomplete information.\n\n"
    "By using this tool, you acknowledge that the information provided is NOT medical advice."
)

SYSTEM_PROMPT = (
    "You are a drug interaction information assistant for EDUCATIONAL purposes only. "
    "You MUST begin EVERY response with a clear disclaimer that you are NOT a pharmacist "
    "or doctor and this is NOT medical advice. "
    "When given a list of medications, analyse potential interactions based on general "
    "pharmacological literature. For each interaction found, provide: "
    "1. The pair of drugs involved. "
    "2. The type/severity of interaction (e.g., Major, Moderate, Minor). "
    "3. A brief description of the interaction mechanism. "
    "4. General recommendations (always including 'consult your healthcare provider'). "
    "If no known interactions are found, state that clearly but still recommend "
    "consulting a pharmacist. Present information in a structured, readable format. "
    "NEVER recommend specific dosage changes or treatment modifications."
)

# ============================================================================
# Severity Levels
# ============================================================================
SEVERITY_LEVELS = {
    "contraindicated": {
        "level": 5,
        "color": "red",
        "emoji": "🚫",
        "description": "These drugs should NOT be taken together. Life-threatening risk.",
    },
    "major": {
        "level": 4,
        "color": "red",
        "emoji": "🔴",
        "description": "Significant risk. Avoid combination or use with close monitoring.",
    },
    "moderate": {
        "level": 3,
        "color": "yellow",
        "emoji": "🟡",
        "description": "Could cause noticeable effects. Use with caution.",
    },
    "minor": {
        "level": 2,
        "color": "green",
        "emoji": "🟢",
        "description": "Minimal clinical significance. Monitor as needed.",
    },
    "none": {
        "level": 1,
        "color": "dim",
        "emoji": "✅",
        "description": "No known interaction.",
    },
}

# ============================================================================
# Common Food-Drug Interactions Database
# ============================================================================
FOOD_INTERACTIONS = {
    "warfarin": ["vitamin K rich foods (leafy greens)", "cranberry juice", "grapefruit"],
    "metformin": ["alcohol"],
    "statins": ["grapefruit", "grapefruit juice"],
    "ciprofloxacin": ["dairy products", "calcium-fortified foods"],
    "tetracycline": ["dairy products", "antacids", "iron supplements"],
    "maois": ["tyramine-rich foods (aged cheese, cured meats, soy sauce)"],
    "lisinopril": ["potassium-rich foods (bananas, oranges)", "salt substitutes"],
    "methotrexate": ["alcohol", "folate-rich foods (may affect efficacy)"],
    "theophylline": ["caffeine", "high-protein diet"],
    "levothyroxine": ["soy products", "high-fiber foods", "calcium supplements"],
}

# ============================================================================
# Common Dosage Notes
# ============================================================================
DOSAGE_NOTES = {
    "aspirin": "Typical adult dose: 325-650mg every 4-6h. Max 4g/day.",
    "ibuprofen": "Typical adult dose: 200-400mg every 4-6h. Max 1200mg/day (OTC).",
    "acetaminophen": "Typical adult dose: 325-1000mg every 4-6h. Max 3g/day.",
    "metformin": "Typical starting dose: 500mg twice daily. Max 2550mg/day.",
    "lisinopril": "Typical starting dose: 5-10mg once daily. Max 80mg/day.",
    "atorvastatin": "Typical starting dose: 10-20mg once daily. Max 80mg/day.",
    "omeprazole": "Typical dose: 20mg once daily. Short-term use recommended.",
    "amoxicillin": "Typical adult dose: 250-500mg every 8h or 875mg every 12h.",
    "warfarin": "Dose varies widely. Requires regular INR monitoring.",
    "metoprolol": "Typical starting dose: 25-50mg twice daily.",
}

# ============================================================================
# Common Alternatives
# ============================================================================
COMMON_ALTERNATIVES = {
    "ibuprofen": ["acetaminophen", "naproxen", "aspirin"],
    "aspirin": ["acetaminophen", "ibuprofen"],
    "omeprazole": ["famotidine", "ranitidine", "esomeprazole"],
    "atorvastatin": ["rosuvastatin", "simvastatin", "pravastatin"],
    "lisinopril": ["losartan", "enalapril", "ramipril"],
    "metformin": ["glipizide", "sitagliptin", "empagliflozin"],
    "amoxicillin": ["azithromycin", "doxycycline", "cephalexin"],
    "metoprolol": ["atenolol", "propranolol", "carvedilol"],
    "warfarin": ["apixaban", "rivaroxaban", "dabigatran"],
    "sertraline": ["escitalopram", "fluoxetine", "venlafaxine"],
}


# ============================================================================
# Core Functions
# ============================================================================

def parse_medications(medications_str: str) -> list[str]:
    """
    Parse a comma-separated medication string into a cleaned list.

    Args:
        medications_str: Comma-separated medication names.

    Returns:
        List of trimmed, non-empty medication names.
    """
    return [med.strip() for med in medications_str.split(",") if med.strip()]


def check_interactions(medications: list[str]) -> str:
    """
    Send medication list to the LLM for interaction analysis.

    Args:
        medications: List of medication names.

    Returns:
        LLM response describing potential interactions.
    """
    prompt = (
        f"Please check for potential drug interactions among the following medications:\n"
        f"{', '.join(medications)}\n\n"
        f"List each interaction found with severity and a brief explanation. "
        f"If no interactions are known, state that clearly."
    )

    logger.info("Checking interactions for: %s", ", ".join(medications))

    return generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=CONFIG.get("temperature", 0.2),
        max_tokens=CONFIG.get("max_tokens", 1500),
    )


def get_food_interactions(medication: str) -> list[str]:
    """
    Look up known food interactions for a medication.

    Args:
        medication: Medication name (case-insensitive).

    Returns:
        List of food interaction strings, or empty list if none found.
    """
    key = medication.strip().lower()
    return FOOD_INTERACTIONS.get(key, [])


def get_dosage_notes(medication: str) -> str | None:
    """
    Look up typical dosage notes for a medication.

    Args:
        medication: Medication name (case-insensitive).

    Returns:
        Dosage note string or None if not found.
    """
    key = medication.strip().lower()
    return DOSAGE_NOTES.get(key, None)


def get_alternatives(medication: str) -> list[str]:
    """
    Look up common alternatives for a medication.

    Args:
        medication: Medication name (case-insensitive).

    Returns:
        List of alternative medication names, or empty list if none found.
    """
    key = medication.strip().lower()
    return COMMON_ALTERNATIVES.get(key, [])


def classify_severity(interaction_text: str) -> str:
    """
    Classify the severity of an interaction based on keyword matching.

    Scans the LLM output text for severity keywords and returns the highest
    severity level found.

    Args:
        interaction_text: Text from LLM describing the interaction.

    Returns:
        Severity level string (e.g. "major", "moderate", "minor", "none").
    """
    text_lower = interaction_text.lower()

    # Check from highest severity to lowest
    if "contraindicated" in text_lower or "do not take together" in text_lower:
        return "contraindicated"
    if "major" in text_lower or "severe" in text_lower or "serious" in text_lower:
        return "major"
    if "moderate" in text_lower or "caution" in text_lower:
        return "moderate"
    if "minor" in text_lower or "mild" in text_lower or "low risk" in text_lower:
        return "minor"
    return "none"


def display_results(medications: list[str], response: str) -> None:
    """Display the interaction check results with rich formatting and severity."""
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.table import Table

    console = Console()

    # Medication table
    med_table = Table(
        title="Medications Checked",
        show_header=True,
        header_style="bold cyan",
    )
    med_table.add_column("#", style="dim", width=4)
    med_table.add_column("Medication", style="bold")
    med_table.add_column("Dosage Info", style="dim")
    for i, med in enumerate(medications, 1):
        dosage = get_dosage_notes(med) or "—"
        med_table.add_row(str(i), med, dosage)
    console.print(med_table)

    # Severity classification
    severity = classify_severity(response)
    sev_info = SEVERITY_LEVELS[severity]
    console.print()
    console.print(
        f"  {sev_info['emoji']}  Overall Severity: "
        f"[bold {sev_info['color']}]{severity.upper()}[/bold {sev_info['color']}] "
        f"— {sev_info['description']}"
    )

    # Interaction analysis
    console.print()
    console.print(Panel(
        Markdown(response),
        title="[bold green]Interaction Analysis[/bold green]",
        border_style="green",
        padding=(1, 2),
    ))

    # Food interactions
    food_found = False
    food_table = Table(
        title="🍎 Food Interactions",
        show_header=True,
        header_style="bold yellow",
    )
    food_table.add_column("Medication", style="bold")
    food_table.add_column("Food/Substance to Watch", style="yellow")
    for med in medications:
        foods = get_food_interactions(med)
        if foods:
            food_found = True
            food_table.add_row(med, ", ".join(foods))

    if food_found:
        console.print()
        console.print(food_table)

    # Alternatives
    alt_found = False
    alt_table = Table(
        title="💡 Possible Alternatives",
        show_header=True,
        header_style="bold blue",
    )
    alt_table.add_column("Medication", style="bold")
    alt_table.add_column("Alternatives", style="blue")
    for med in medications:
        alts = get_alternatives(med)
        if alts:
            alt_found = True
            alt_table.add_row(med, ", ".join(alts))

    if alt_found:
        console.print()
        console.print(alt_table)

    # Reminder
    console.print()
    console.print(
        "[dim]⚠️  Remember: ALWAYS consult a qualified healthcare provider "
        "or pharmacist about drug interactions.[/dim]"
    )
