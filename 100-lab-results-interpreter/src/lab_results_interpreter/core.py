"""
Lab Results Interpreter - Core Module
AI-powered laboratory result analysis using Gemma 4 via Ollama.

Provides interpretation of lab results, abnormality detection,
follow-up test suggestions, and reference range lookups.
All processing is local — no patient data leaves the machine.
"""

import logging
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Add project root to path for common imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from common.llm_client import chat, check_ollama_running
from src.lab_results_interpreter.config import load_config

logger = logging.getLogger(__name__)

# ─── Medical Disclaimer ─────────────────────────────────────────────

DISCLAIMER = (
    "⚠️  DISCLAIMER: This tool provides AI-generated interpretations of "
    "laboratory results for educational and informational purposes ONLY. "
    "It is NOT a substitute for professional medical advice, diagnosis, "
    "or treatment. Always consult a qualified healthcare provider for "
    "interpretation of your lab results. Never disregard professional "
    "medical advice or delay seeking it because of information from this tool. "
    "The developers assume no liability for any actions taken based on "
    "this tool's output."
)

# ─── System Prompt ───────────────────────────────────────────────────

SYSTEM_PROMPT = """You are an expert clinical laboratory scientist and pathologist assistant.
Your role is to help interpret laboratory test results in a clear, educational manner.

Guidelines:
1. Always explain what each test measures and why it matters.
2. Clearly identify values that are outside normal reference ranges.
3. Explain potential clinical significance of abnormal values.
4. Suggest possible causes for abnormalities (both benign and serious).
5. Recommend appropriate follow-up tests when relevant.
6. Use plain language that patients can understand, but also include medical terminology.
7. Always emphasize that results should be reviewed by a qualified healthcare provider.
8. Consider the patient's context (age, sex, medications, conditions) when provided.
9. Never diagnose — only educate and suggest areas for physician discussion.
10. Group related findings and explain how they may be connected.

Format your responses with clear headings, bullet points, and organized sections.
Always end with a reminder to discuss results with a healthcare provider."""

# ─── Reference Ranges ───────────────────────────────────────────────

REFERENCE_RANGES = {
    "CBC": {
        "WBC": {"range": "4.5-11.0", "unit": "x10^3/µL", "description": "White Blood Cell Count"},
        "RBC": {"range": "4.5-5.5", "unit": "x10^6/µL", "description": "Red Blood Cell Count"},
        "Hemoglobin": {"range": "13.5-17.5", "unit": "g/dL", "description": "Hemoglobin"},
        "Hematocrit": {"range": "38.3-48.6", "unit": "%", "description": "Hematocrit"},
        "Platelets": {"range": "150-400", "unit": "x10^3/µL", "description": "Platelet Count"},
        "MCV": {"range": "80-100", "unit": "fL", "description": "Mean Corpuscular Volume"},
    },
    "BMP": {
        "Glucose": {"range": "70-100", "unit": "mg/dL", "description": "Fasting Glucose"},
        "BUN": {"range": "7-20", "unit": "mg/dL", "description": "Blood Urea Nitrogen"},
        "Creatinine": {"range": "0.7-1.3", "unit": "mg/dL", "description": "Creatinine"},
        "Sodium": {"range": "136-145", "unit": "mEq/L", "description": "Sodium"},
        "Potassium": {"range": "3.5-5.0", "unit": "mEq/L", "description": "Potassium"},
        "Calcium": {"range": "8.5-10.5", "unit": "mg/dL", "description": "Calcium"},
        "CO2": {"range": "23-29", "unit": "mEq/L", "description": "Carbon Dioxide"},
    },
    "Lipid Panel": {
        "Total Cholesterol": {"range": "<200", "unit": "mg/dL", "description": "Total Cholesterol"},
        "LDL": {"range": "<100", "unit": "mg/dL", "description": "LDL Cholesterol"},
        "HDL": {"range": ">40", "unit": "mg/dL", "description": "HDL Cholesterol"},
        "Triglycerides": {"range": "<150", "unit": "mg/dL", "description": "Triglycerides"},
    },
    "Liver Panel": {
        "ALT": {"range": "7-56", "unit": "U/L", "description": "Alanine Aminotransferase"},
        "AST": {"range": "10-40", "unit": "U/L", "description": "Aspartate Aminotransferase"},
        "ALP": {"range": "44-147", "unit": "U/L", "description": "Alkaline Phosphatase"},
        "Bilirubin": {"range": "0.1-1.2", "unit": "mg/dL", "description": "Total Bilirubin"},
        "Albumin": {"range": "3.5-5.0", "unit": "g/dL", "description": "Albumin"},
    },
    "Thyroid": {
        "TSH": {"range": "0.4-4.0", "unit": "mIU/L", "description": "Thyroid Stimulating Hormone"},
        "Free T4": {"range": "0.8-1.8", "unit": "ng/dL", "description": "Free Thyroxine"},
        "Free T3": {"range": "2.3-4.2", "unit": "pg/mL", "description": "Free Triiodothyronine"},
    },
    "Urinalysis": {
        "pH": {"range": "4.5-8.0", "unit": "", "description": "Urine pH"},
        "Specific Gravity": {"range": "1.005-1.030", "unit": "", "description": "Specific Gravity"},
        "Protein": {"range": "Negative", "unit": "", "description": "Protein"},
        "Glucose": {"range": "Negative", "unit": "", "description": "Glucose"},
    },
}

# ─── Lab Panel List ──────────────────────────────────────────────────

LAB_PANELS = [
    "CBC",
    "BMP",
    "CMP",
    "Lipid Panel",
    "Liver Panel",
    "Thyroid",
    "Urinalysis",
    "Coagulation",
    "Iron Studies",
    "HbA1c",
]

# ─── Configuration ───────────────────────────────────────────────────

_config = load_config()


# ─── Core Functions ──────────────────────────────────────────────────


def interpret_results(
    lab_results_text: str,
    patient_context: str = "",
    panel_type: str = "",
    conversation_history: Optional[List[Dict[str, str]]] = None,
) -> str:
    """
    Interpret laboratory results using the LLM.

    Args:
        lab_results_text: Raw lab results text (e.g., from a report).
        patient_context: Optional patient context (age, sex, medications).
        panel_type: Optional lab panel type (e.g., "CBC", "BMP").
        conversation_history: Optional prior conversation messages.

    Returns:
        AI-generated interpretation of the lab results.
    """
    logger.info("Interpreting lab results (panel: %s)", panel_type or "auto-detect")

    prompt_parts = ["Please interpret the following laboratory results:\n"]
    if panel_type:
        prompt_parts.append(f"Panel Type: {panel_type}\n")
    if patient_context:
        prompt_parts.append(f"Patient Context: {patient_context}\n")

    # Include reference ranges if panel is known
    if panel_type and panel_type in REFERENCE_RANGES:
        prompt_parts.append(f"\nReference Ranges for {panel_type}:")
        for test, info in REFERENCE_RANGES[panel_type].items():
            prompt_parts.append(
                f"  - {test} ({info['description']}): {info['range']} {info['unit']}"
            )
        prompt_parts.append("")

    prompt_parts.append(f"Lab Results:\n{lab_results_text}")
    prompt_parts.append(
        "\nPlease provide:\n"
        "1. Summary of results\n"
        "2. Abnormal values and their significance\n"
        "3. Possible clinical implications\n"
        "4. Recommended follow-up actions\n"
        "5. Important context or caveats"
    )

    prompt = "\n".join(prompt_parts)
    messages = list(conversation_history or [])
    messages.append({"role": "user", "content": prompt})

    response = chat(
        messages=messages,
        model=_config.get("model", "gemma4"),
        system_prompt=SYSTEM_PROMPT,
        temperature=_config.get("temperature", 0.3),
        max_tokens=_config.get("max_tokens", 2048),
    )
    logger.info("Interpretation complete")
    return response


def identify_abnormalities(
    lab_results_text: str,
    panel_type: str = "",
) -> str:
    """
    Identify abnormal values in lab results.

    Args:
        lab_results_text: Raw lab results text.
        panel_type: Optional lab panel type for reference range context.

    Returns:
        AI-generated list of abnormalities with explanations.
    """
    logger.info("Identifying abnormalities (panel: %s)", panel_type or "auto-detect")

    prompt_parts = [
        "Analyze the following lab results and identify ALL abnormal values.\n"
    ]
    if panel_type:
        prompt_parts.append(f"Panel Type: {panel_type}\n")

    if panel_type and panel_type in REFERENCE_RANGES:
        prompt_parts.append(f"Reference Ranges for {panel_type}:")
        for test, info in REFERENCE_RANGES[panel_type].items():
            prompt_parts.append(
                f"  - {test}: {info['range']} {info['unit']}"
            )
        prompt_parts.append("")

    prompt_parts.append(f"Lab Results:\n{lab_results_text}")
    prompt_parts.append(
        "\nFor each abnormal value, provide:\n"
        "1. The test name and value\n"
        "2. Whether it is HIGH or LOW\n"
        "3. The normal reference range\n"
        "4. Possible causes\n"
        "5. Clinical significance"
    )

    prompt = "\n".join(prompt_parts)
    messages = [{"role": "user", "content": prompt}]

    return chat(
        messages=messages,
        model=_config.get("model", "gemma4"),
        system_prompt=SYSTEM_PROMPT,
        temperature=_config.get("temperature", 0.3),
        max_tokens=_config.get("max_tokens", 2048),
    )


def suggest_followup_tests(
    lab_results_text: str,
    clinical_context: str = "",
) -> str:
    """
    Suggest follow-up tests based on current lab results.

    Args:
        lab_results_text: Raw lab results text.
        clinical_context: Optional clinical context (symptoms, history).

    Returns:
        AI-generated follow-up test recommendations.
    """
    logger.info("Suggesting follow-up tests")

    prompt_parts = [
        "Based on the following lab results, suggest appropriate follow-up tests.\n"
    ]
    if clinical_context:
        prompt_parts.append(f"Clinical Context: {clinical_context}\n")

    prompt_parts.append(f"Lab Results:\n{lab_results_text}")
    prompt_parts.append(
        "\nFor each recommended follow-up test, provide:\n"
        "1. Test name\n"
        "2. Why it is recommended based on the current results\n"
        "3. What it would help rule in or rule out\n"
        "4. Priority level (urgent, routine, optional)"
    )

    prompt = "\n".join(prompt_parts)
    messages = [{"role": "user", "content": prompt}]

    return chat(
        messages=messages,
        model=_config.get("model", "gemma4"),
        system_prompt=SYSTEM_PROMPT,
        temperature=_config.get("temperature", 0.3),
        max_tokens=_config.get("max_tokens", 2048),
    )


def explain_lab_value(
    test_name: str,
    value: str,
    unit: str = "",
) -> str:
    """
    Explain a specific lab value in detail.

    Args:
        test_name: Name of the lab test (e.g., "Hemoglobin").
        value: The test result value.
        unit: Unit of measurement.

    Returns:
        AI-generated explanation of the lab value.
    """
    logger.info("Explaining lab value: %s = %s %s", test_name, value, unit)

    value_str = f"{value} {unit}".strip()
    prompt = (
        f"Please explain the following lab test result in detail:\n\n"
        f"Test: {test_name}\n"
        f"Value: {value_str}\n\n"
        f"Please cover:\n"
        f"1. What this test measures and why it's important\n"
        f"2. Whether this value is normal, high, or low\n"
        f"3. Possible causes if abnormal\n"
        f"4. What this might mean clinically\n"
        f"5. When to be concerned"
    )

    messages = [{"role": "user", "content": prompt}]

    return chat(
        messages=messages,
        model=_config.get("model", "gemma4"),
        system_prompt=SYSTEM_PROMPT,
        temperature=_config.get("temperature", 0.3),
        max_tokens=_config.get("max_tokens", 2048),
    )


def get_reference_range(panel: str, test_name: str) -> Dict:
    """
    Get reference range information for a specific test.

    Args:
        panel: Lab panel name (e.g., "CBC", "BMP").
        test_name: Name of the specific test.

    Returns:
        Dictionary with range, unit, and description, or empty dict.
    """
    panel_data = REFERENCE_RANGES.get(panel, {})
    return panel_data.get(test_name, {})


# ─── Lab Session Tracker ─────────────────────────────────────────────


class LabSession:
    """Track lab result interpretations across a session."""

    def __init__(self):
        """Initialize a new lab session."""
        self.interpretations: List[Dict] = []
        self.conversation_history: List[Dict[str, str]] = []
        self.created_at: str = datetime.now().isoformat()

    def add_interpretation(
        self,
        lab_results: str,
        interpretation: str,
        panel_type: str = "",
        patient_context: str = "",
    ) -> None:
        """
        Add an interpretation to the session history.

        Args:
            lab_results: The original lab results text.
            interpretation: The AI-generated interpretation.
            panel_type: Lab panel type.
            patient_context: Patient context provided.
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "lab_results": lab_results,
            "interpretation": interpretation,
            "panel_type": panel_type,
            "patient_context": patient_context,
        }
        self.interpretations.append(entry)
        self.conversation_history.append(
            {"role": "user", "content": lab_results}
        )
        self.conversation_history.append(
            {"role": "assistant", "content": interpretation}
        )
        logger.info(
            "Added interpretation to session (total: %d)",
            len(self.interpretations),
        )

    def get_history(self) -> List[Dict]:
        """
        Get the full interpretation history.

        Returns:
            List of interpretation entries.
        """
        return self.interpretations

    def get_summary(self) -> str:
        """
        Get a summary of the session.

        Returns:
            Human-readable session summary string.
        """
        total = len(self.interpretations)
        panels = [
            e["panel_type"] for e in self.interpretations if e["panel_type"]
        ]
        panel_summary = ", ".join(set(panels)) if panels else "Various"
        return (
            f"Lab Session Summary\n"
            f"  Created: {self.created_at}\n"
            f"  Total Interpretations: {total}\n"
            f"  Panels Analyzed: {panel_summary}"
        )


def display_disclaimer() -> str:
    """
    Display the medical disclaimer.

    Returns:
        The disclaimer text.
    """
    return DISCLAIMER
