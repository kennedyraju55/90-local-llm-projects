"""
Clinical Note Generator - Core Module

AI-powered SOAP note generation from patient encounter descriptions.
Generates structured clinical notes (Subjective, Objective, Assessment, Plan).

⚠️ MEDICAL DISCLAIMER: This tool is for EDUCATIONAL and INFORMATIONAL purposes ONLY.
It is NOT a substitute for professional medical advice, diagnosis, or treatment.
ALWAYS consult a qualified healthcare provider for any health concerns.
"""

import os
import sys
import json
import logging
from typing import Optional, List, Dict, Any
from datetime import datetime

_common_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.insert(0, os.path.abspath(_common_path))

from common.llm_client import chat, check_ollama_running  # noqa: E402
from .config import load_config

logger = logging.getLogger("clinical_note_generator")


def _setup_logging(level: str = "INFO") -> None:
    """Configure logging."""
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


CONFIG = load_config()
_setup_logging(CONFIG.get("log_level", "INFO"))

DISCLAIMER = """
⚠️  MEDICAL DISCLAIMER  ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This tool is for EDUCATIONAL and INFORMATIONAL purposes ONLY.
It is NOT a substitute for professional medical advice, diagnosis, or treatment.

• Generated notes are AI-assisted drafts and MUST be reviewed by a physician.
• Do NOT use generated notes as final clinical documentation without review.
• ALWAYS verify clinical accuracy before incorporating into patient records.
• This tool does NOT replace clinical judgment or professional documentation.

By using this tool, you acknowledge that all output requires professional review.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

SYSTEM_PROMPT = """You are an expert medical documentation assistant specializing in generating SOAP notes.

IMPORTANT RULES:
1. Generate structured SOAP notes from patient encounter descriptions.
2. ALWAYS format output with clear S (Subjective), O (Objective), A (Assessment), P (Plan) sections.
3. Use proper medical terminology and abbreviations.
4. Be thorough but concise in each section.
5. Include relevant negatives in the objective section.
6. List differential diagnoses in the assessment when appropriate.
7. Include specific, actionable items in the plan.
8. ALWAYS include a disclaimer that notes must be reviewed by the treating physician.

SOAP Format:
**SUBJECTIVE (S):** Patient's chief complaint, history of present illness, review of systems, past medical/surgical/family/social history.
**OBJECTIVE (O):** Vital signs, physical examination findings, lab results, imaging.
**ASSESSMENT (A):** Diagnosis or differential diagnoses with clinical reasoning.
**PLAN (P):** Treatment plan, medications, follow-up, patient education, referrals."""

NOTE_TEMPLATES: Dict[str, str] = {
    "general": "Standard office visit SOAP note",
    "follow_up": "Follow-up visit for existing condition",
    "urgent": "Urgent/acute care visit",
    "pediatric": "Pediatric visit with age-appropriate documentation",
    "psychiatric": "Psychiatric evaluation with mental status exam",
    "surgical": "Pre-operative or post-operative note",
}

SPECIALTY_PROMPTS: Dict[str, str] = {
    "internal_medicine": "Focus on comprehensive medical history, systems review, and chronic disease management.",
    "emergency": "Prioritize chief complaint, acute findings, and disposition. Include time-critical elements.",
    "pediatrics": "Include developmental milestones, growth parameters, and age-specific considerations.",
    "psychiatry": "Include detailed mental status examination, risk assessment, and psychosocial factors.",
    "surgery": "Focus on surgical indications, operative findings, and post-operative planning.",
    "family_medicine": "Include preventive care, screening recommendations, and health maintenance.",
}


def display_disclaimer() -> None:
    """Display the medical disclaimer using rich formatting."""
    from rich.console import Console
    from rich.panel import Panel
    console = Console()
    console.print(Panel(DISCLAIMER, title="⚕️  Medical Disclaimer", border_style="red"))


def generate_soap_note(
    encounter_description: str,
    patient_demographics: Optional[Dict[str, Any]] = None,
    note_type: str = "general",
    specialty: str = "internal_medicine",
    conversation_history: Optional[List[Dict[str, str]]] = None,
) -> str:
    """Generate a SOAP note from an encounter description.

    Args:
        encounter_description: Free-text description of the patient encounter.
        patient_demographics: Optional dict with age, sex, etc.
        note_type: Type of note (general, follow_up, urgent, etc.).
        specialty: Medical specialty for tailored documentation.
        conversation_history: Optional prior messages for context.

    Returns:
        Formatted SOAP note as a string.
    """
    if conversation_history is None:
        conversation_history = []

    demo_context = ""
    if patient_demographics:
        parts = []
        if "age" in patient_demographics:
            parts.append(f"Age: {patient_demographics['age']}")
        if "sex" in patient_demographics:
            parts.append(f"Sex: {patient_demographics['sex']}")
        if "mrn" in patient_demographics:
            parts.append(f"MRN: {patient_demographics['mrn']}")
        demo_context = f"\nPatient Demographics: {', '.join(parts)}"

    specialty_guidance = SPECIALTY_PROMPTS.get(specialty, "")
    template_desc = NOTE_TEMPLATES.get(note_type, "Standard visit")

    prompt = f"""Generate a comprehensive SOAP note for the following encounter.
Note Type: {template_desc}
Specialty: {specialty}{demo_context}

Encounter Description:
{encounter_description}

{specialty_guidance}

Please generate a complete, well-structured SOAP note with all four sections (S, O, A, P).
Include appropriate medical terminology and ICD-10 codes where applicable.
End with: "⚠️ This note is AI-generated and must be reviewed by the treating physician."
"""

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(conversation_history)
    messages.append({"role": "user", "content": prompt})

    logger.info("Generating SOAP note (type=%s, specialty=%s)", note_type, specialty)
    try:
        response = chat(messages)
        logger.info("SOAP note generated (%d chars)", len(response))
        return response
    except Exception as exc:
        logger.error("SOAP note generation failed: %s", exc)
        raise


def generate_note_section(
    encounter_description: str,
    section: str = "S",
) -> str:
    """Generate a specific section of a SOAP note.

    Args:
        encounter_description: Description of the encounter.
        section: One of S, O, A, P.

    Returns:
        The requested section text.
    """
    section_names = {"S": "Subjective", "O": "Objective", "A": "Assessment", "P": "Plan"}
    section_name = section_names.get(section.upper(), "Subjective")

    prompt = f"""From the following encounter description, generate ONLY the {section_name} section of a SOAP note.
Be thorough and use proper medical terminology.

Encounter: {encounter_description}

Generate the {section_name} ({section.upper()}) section only:"""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    logger.info("Generating section: %s", section_name)
    try:
        return chat(messages)
    except Exception as exc:
        logger.error("Section generation failed: %s", exc)
        raise


def refine_note(
    original_note: str,
    feedback: str,
) -> str:
    """Refine a SOAP note based on physician feedback.

    Args:
        original_note: The original generated note.
        feedback: Physician's corrections or additions.

    Returns:
        Refined SOAP note.
    """
    prompt = f"""Please refine the following SOAP note based on the physician's feedback.

Original Note:
{original_note}

Physician Feedback:
{feedback}

Generate the refined SOAP note maintaining proper format:"""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    logger.info("Refining SOAP note with feedback")
    try:
        return chat(messages)
    except Exception as exc:
        logger.error("Note refinement failed: %s", exc)
        raise


def extract_diagnoses(note: str) -> List[str]:
    """Extract diagnoses from a SOAP note's Assessment section.

    Args:
        note: Complete SOAP note text.

    Returns:
        List of extracted diagnosis strings.
    """
    prompt = f"""Extract all diagnoses and differential diagnoses from the Assessment section of this SOAP note.
Return them as a simple numbered list, one per line.

SOAP Note:
{note}

Diagnoses:"""

    messages = [
        {"role": "system", "content": "You are a medical documentation analyst. Extract diagnoses precisely."},
        {"role": "user", "content": prompt},
    ]

    try:
        response = chat(messages)
        diagnoses = [line.strip().lstrip("0123456789.-) ") for line in response.strip().split("\n") if line.strip()]
        return [d for d in diagnoses if d]
    except Exception:
        return []


class NoteSession:
    """Track note generation sessions."""

    def __init__(self) -> None:
        self.notes: List[Dict[str, Any]] = []

    def add_note(self, encounter: str, note: str, note_type: str, specialty: str) -> None:
        """Add a generated note to the session."""
        self.notes.append({
            "timestamp": datetime.now().isoformat(),
            "encounter": encounter,
            "note": note,
            "note_type": note_type,
            "specialty": specialty,
        })

    def get_notes(self) -> List[Dict[str, Any]]:
        """Get all notes in this session."""
        return list(self.notes)

    def get_summary(self) -> Dict[str, Any]:
        """Get session summary."""
        if not self.notes:
            return {"total_notes": 0, "note_types": [], "specialties": []}
        types = list(set(n["note_type"] for n in self.notes))
        specs = list(set(n["specialty"] for n in self.notes))
        return {"total_notes": len(self.notes), "note_types": types, "specialties": specs}
