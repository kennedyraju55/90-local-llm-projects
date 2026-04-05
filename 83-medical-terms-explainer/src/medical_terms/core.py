"""
Medical Terms Explainer - Core logic, databases, and LLM integration.

⚠️  DISCLAIMER: This tool is for EDUCATIONAL PURPOSES ONLY and does NOT provide
medical advice. Always consult a qualified healthcare professional for medical
questions or concerns.
"""

import logging
import os
import sys
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

# ---------------------------------------------------------------------------
# Common LLM client import
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate, check_ollama_running  # noqa: E402

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
_CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')


def load_config() -> dict:
    """Load configuration from config.yaml."""
    try:
        with open(_CONFIG_PATH, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logger.warning("config.yaml not found, using defaults.")
        return {}


_config = load_config()

# ---------------------------------------------------------------------------
# Medical Disclaimer
# ---------------------------------------------------------------------------
DISCLAIMER = (
    "⚠️  DISCLAIMER: This tool is for EDUCATIONAL PURPOSES ONLY. "
    "It does NOT provide medical advice, diagnosis, or treatment recommendations. "
    "Always consult a qualified healthcare professional for any medical questions "
    "or concerns."
)

# ---------------------------------------------------------------------------
# System Prompt
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are a medical terminology educator. Your role is to explain medical terms
in clear, accessible language. For each term, provide:

1. **Definition**: A precise medical definition.
2. **Etymology**: The word origins (Greek, Latin, etc.) and how the parts combine.
3. **Layman Explanation**: A simple, everyday-language explanation anyone can understand.
4. **Usage in Context**: One or two example sentences showing how the term is used clinically.
5. **Related Terms**: 3-5 related medical terms with brief definitions.

IMPORTANT: You are an educational tool only. Always remind users that this information
is for learning purposes and is NOT a substitute for professional medical advice.

Adjust the depth of your explanation based on the requested detail level:
- brief: Short definition and layman explanation only.
- standard: All sections with moderate detail.
- comprehensive: All sections with extensive detail, additional examples, and historical context."""

# ---------------------------------------------------------------------------
# Visual Aids — references to anatomy / medical diagrams
# ---------------------------------------------------------------------------
VISUAL_AIDS: dict[str, str] = {
    "heart": "\U0001fac0 See: Heart anatomy diagram — 4 chambers, valves, major vessels",
    "lungs": "\U0001fac1 See: Respiratory system diagram — bronchi, alveoli, diaphragm",
    "brain": "\U0001f9e0 See: Brain regions diagram — cerebrum, cerebellum, brainstem",
    "liver": "See: Liver anatomy — lobes, hepatic portal system",
    "kidney": "See: Kidney cross-section — nephron, glomerulus, tubules",
    "skeleton": "\U0001f9b4 See: Skeletal system — 206 bones, major joints",
    "skin": "See: Skin layers diagram — epidermis, dermis, hypodermis",
    "eye": "\U0001f441\ufe0f See: Eye anatomy — cornea, lens, retina, optic nerve",
    "ear": "\U0001f442 See: Ear anatomy — outer, middle, inner ear, cochlea",
    "digestive": "See: Digestive system — esophagus, stomach, intestines",
}

# ---------------------------------------------------------------------------
# Pronunciation Guide
# ---------------------------------------------------------------------------
PRONUNCIATION_GUIDE: dict[str, str] = {
    "angina": "an-JY-nuh",
    "arrhythmia": "uh-RITH-mee-uh",
    "bronchitis": "bron-KY-tis",
    "cirrhosis": "sih-ROH-sis",
    "dyspnea": "DISP-nee-uh",
    "edema": "ih-DEE-muh",
    "fibromyalgia": "fy-broh-my-AL-juh",
    "gastritis": "gas-TRY-tis",
    "hepatitis": "hep-uh-TY-tis",
    "hypertension": "hy-per-TEN-shun",
    "ischemia": "is-KEE-mee-uh",
    "jaundice": "JAWN-dis",
    "myocardial": "my-oh-KAR-dee-ul",
    "neuropathy": "noo-ROP-uh-thee",
    "osteoporosis": "os-tee-oh-puh-ROH-sis",
    "pneumonia": "noo-MOH-nyuh",
    "tachycardia": "tak-ih-KAR-dee-uh",
    "thrombosis": "throm-BOH-sis",
    "urticaria": "ur-tih-KAIR-ee-uh",
    "vasculitis": "vas-kyoo-LY-tis",
}

# ---------------------------------------------------------------------------
# Related Conditions Mapping
# ---------------------------------------------------------------------------
RELATED_CONDITIONS: dict[str, list[str]] = {
    "hypertension": [
        "atherosclerosis", "heart failure", "stroke",
        "kidney disease", "retinopathy",
    ],
    "diabetes": [
        "neuropathy", "retinopathy", "nephropathy",
        "cardiovascular disease",
    ],
    "asthma": ["COPD", "bronchitis", "allergic rhinitis", "eczema"],
    "arthritis": ["osteoporosis", "gout", "fibromyalgia", "bursitis"],
    "pneumonia": ["bronchitis", "pleurisy", "ARDS", "lung abscess"],
    "anemia": [
        "iron deficiency", "thalassemia",
        "sickle cell disease", "B12 deficiency",
    ],
    "migraine": [
        "tension headache", "cluster headache", "aura", "vertigo",
    ],
    "depression": [
        "anxiety", "bipolar disorder", "dysthymia", "PTSD",
    ],
}

# ---------------------------------------------------------------------------
# Medical Abbreviation Decoder
# ---------------------------------------------------------------------------
MEDICAL_ABBREVIATIONS: dict[str, str] = {
    "BP": "Blood Pressure",
    "HR": "Heart Rate",
    "RR": "Respiratory Rate",
    "SpO2": "Peripheral Oxygen Saturation",
    "BMI": "Body Mass Index",
    "CBC": "Complete Blood Count",
    "BMP": "Basic Metabolic Panel",
    "CMP": "Comprehensive Metabolic Panel",
    "ECG/EKG": "Electrocardiogram",
    "MRI": "Magnetic Resonance Imaging",
    "CT": "Computed Tomography",
    "IV": "Intravenous",
    "IM": "Intramuscular",
    "PO": "Per Os (by mouth)",
    "PRN": "Pro Re Nata (as needed)",
    "BID": "Bis In Die (twice daily)",
    "TID": "Ter In Die (three times daily)",
    "QID": "Quater In Die (four times daily)",
    "STAT": "Statim (immediately)",
    "NPO": "Nil Per Os (nothing by mouth)",
    "DNR": "Do Not Resuscitate",
    "ICU": "Intensive Care Unit",
    "ER/ED": "Emergency Room / Emergency Department",
    "OR": "Operating Room",
    "OTC": "Over The Counter",
    "Rx": "Prescription",
    "Dx": "Diagnosis",
    "Tx": "Treatment",
    "Hx": "History",
    "Sx": "Symptoms",
    "HIPAA": "Health Insurance Portability and Accountability Act",
    "EHR/EMR": "Electronic Health Record / Electronic Medical Record",
    "PT": "Physical Therapy / Prothrombin Time",
    "INR": "International Normalized Ratio",
    "WBC": "White Blood Cell Count",
    "RBC": "Red Blood Cell Count",
    "HbA1c": "Hemoglobin A1c (glycated hemoglobin)",
    "LDL": "Low-Density Lipoprotein",
    "HDL": "High-Density Lipoprotein",
    "TSH": "Thyroid-Stimulating Hormone",
    "UTI": "Urinary Tract Infection",
    "COPD": "Chronic Obstructive Pulmonary Disease",
    "DVT": "Deep Vein Thrombosis",
    "PE": "Pulmonary Embolism",
    "MI": "Myocardial Infarction (Heart Attack)",
    "CVA": "Cerebrovascular Accident (Stroke)",
    "CHF": "Congestive Heart Failure",
    "GERD": "Gastroesophageal Reflux Disease",
}


# ===================================================================
# Public API
# ===================================================================

def _build_prompt(term: str, detail: str) -> str:
    """Build the LLM prompt for explaining a medical term.

    Args:
        term: The medical term to explain.
        detail: Level of detail — brief, standard, or comprehensive.

    Returns:
        The formatted prompt string.
    """
    return (
        f"Explain the medical term '{term}' at a '{detail}' detail level.\n\n"
        f"Detail level: {detail}\n\n"
        "Format your response in clear Markdown with headings for each section."
    )


def explain_term(term: str, detail: str = "standard") -> str:
    """Explain a single medical term using the LLM.

    Args:
        term: The medical term to explain.
        detail: Level of detail — brief, standard, or comprehensive.

    Returns:
        The LLM-generated explanation as a string.
    """
    ollama_cfg = _config.get("ollama", {})
    prompt = _build_prompt(term, detail)
    logger.info("Explaining term '%s' at '%s' detail level", term, detail)
    response = generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        temperature=ollama_cfg.get("temperature", 0.3),
        max_tokens=ollama_cfg.get("max_tokens", 2048),
    )
    return response


def get_pronunciation(term: str) -> Optional[str]:
    """Look up the phonetic pronunciation of a medical term.

    Args:
        term: The medical term (case-insensitive).

    Returns:
        Phonetic pronunciation string, or None if not found.
    """
    return PRONUNCIATION_GUIDE.get(term.lower())


def get_visual_aid(term: str) -> Optional[str]:
    """Look up a visual-aid reference for a medical topic.

    Args:
        term: An anatomy / organ keyword (case-insensitive).

    Returns:
        Visual-aid description string, or None if not found.
    """
    return VISUAL_AIDS.get(term.lower())


def get_related_conditions(term: str) -> list[str]:
    """Return a list of conditions related to the given term.

    Args:
        term: The medical condition (case-insensitive).

    Returns:
        List of related condition names, empty list if none found.
    """
    return RELATED_CONDITIONS.get(term.lower(), [])


def decode_abbreviation(abbrev: str) -> Optional[str]:
    """Decode a single medical abbreviation.

    Args:
        abbrev: The abbreviation to decode (case-insensitive match attempted).

    Returns:
        The full meaning, or None if not found.
    """
    # Try exact match first
    if abbrev in MEDICAL_ABBREVIATIONS:
        return MEDICAL_ABBREVIATIONS[abbrev]
    # Case-insensitive search
    upper = abbrev.upper()
    for key, value in MEDICAL_ABBREVIATIONS.items():
        if key.upper() == upper:
            return value
    return None


def search_abbreviations(query: str) -> dict[str, str]:
    """Search medical abbreviations by partial match on key or value.

    Args:
        query: Search string (case-insensitive).

    Returns:
        Dictionary of matching abbreviation → meaning pairs.
    """
    query_lower = query.lower()
    results: dict[str, str] = {}
    for key, value in MEDICAL_ABBREVIATIONS.items():
        if query_lower in key.lower() or query_lower in value.lower():
            results[key] = value
    return results
