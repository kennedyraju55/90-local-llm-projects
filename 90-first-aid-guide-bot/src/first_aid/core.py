"""
First Aid Guide Bot - Core logic and data.

🚨 EMERGENCY DISCLAIMER: This tool is NOT a substitute for emergency medical services.
If someone is seriously injured or in a life-threatening situation, CALL 911 IMMEDIATELY.
This is NOT medical advice. Always seek professional medical help for injuries and illness.
"""

from typing import Optional, List, Dict, Any, Tuple, Union
import logging
import os
import sys
from dataclasses import dataclass, field

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import chat, generate, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Emergency disclaimer
# ---------------------------------------------------------------------------
EMERGENCY_DISCLAIMER = (
    "[bold red]🚨 EMERGENCY DISCLAIMER[/bold red]\n\n"
    "[bold]This tool is NOT a substitute for emergency medical services.[/bold]\n"
    "[bold]This is NOT medical advice.[/bold]\n\n"
    "• For life-threatening emergencies, [bold red]CALL 911[/bold red] immediately.\n"
    "• For poison control, call [bold]1-800-222-1222[/bold].\n"
    "• Always seek professional medical evaluation for injuries.\n"
    "• This tool provides general first aid information only."
)

# ---------------------------------------------------------------------------
# System prompt for the LLM
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = (
    "You are a first aid information assistant. You provide general first aid "
    "guidance based on widely recognized first aid practices.\n\n"
    "CRITICAL RULES:\n"
    "1. ALWAYS start responses for serious or potentially serious situations with "
    "'⚠️ CALL 911/EMERGENCY SERVICES IMMEDIATELY IF...' followed by the specific "
    "warning signs that require emergency care.\n"
    "2. Provide clear, numbered step-by-step first aid instructions.\n"
    "3. Include a 'What NOT to Do' section listing common mistakes.\n"
    "4. End with 'When to Seek Professional Medical Help' guidance.\n"
    "5. NEVER diagnose conditions. Only provide general first aid information.\n"
    "6. ALWAYS remind the user that this is NOT medical advice and they should "
    "seek professional medical help.\n"
    "7. Use simple, clear language that anyone can follow in a stressful situation.\n"
    "8. If the situation sounds life-threatening, prioritize calling 911 above all else."
)

# ---------------------------------------------------------------------------
# Common first-aid scenarios
# ---------------------------------------------------------------------------
COMMON_SCENARIOS = [
    ("Minor Burns", "Small burns from cooking, hot surfaces, etc.", "🔥", "Moderate"),
    ("Cuts & Scrapes", "Minor wounds, lacerations, and abrasions", "🩹", "Low"),
    ("Choking (Adult)", "Airway obstruction in adults", "🫁", "High"),
    ("Choking (Infant)", "Airway obstruction in infants under 1 year", "👶", "High"),
    ("Sprains & Strains", "Twisted ankles, pulled muscles", "🦵", "Low-Moderate"),
    ("Allergic Reactions", "Mild to severe allergic reactions", "⚠️", "Moderate-High"),
    ("Nosebleed", "Bleeding from the nose", "👃", "Low"),
    ("Bee Stings", "Insect stings and bites", "🐝", "Low-Moderate"),
    ("Heat Exhaustion", "Overheating and heat-related illness", "🌡️", "Moderate-High"),
    ("Hypothermia", "Dangerously low body temperature", "🥶", "High"),
    ("Fractures", "Suspected broken bones", "🦴", "Moderate-High"),
    ("Seizures", "Epileptic or other seizures", "⚡", "High"),
    ("Fainting", "Loss of consciousness", "😵", "Moderate"),
    ("Eye Injuries", "Foreign objects, chemicals in eyes", "👁️", "Moderate-High"),
    ("Poisoning", "Ingestion of harmful substances", "☠️", "High"),
]

# ---------------------------------------------------------------------------
# Emergency decision tree for quick triage
# ---------------------------------------------------------------------------
EMERGENCY_DECISION_TREE = {
    "conscious": {
        "breathing": {
            "severe_bleeding": "Call 911, apply direct pressure",
            "no_bleeding": "Assess injuries, monitor",
        },
        "not_breathing": "Call 911, begin CPR",
    },
    "unconscious": {
        "breathing": "Recovery position, call 911",
        "not_breathing": "Call 911, begin CPR immediately",
    },
}

# ---------------------------------------------------------------------------
# First-aid supply checklist
# ---------------------------------------------------------------------------
FIRST_AID_SUPPLIES = [
    {"item": "Adhesive bandages (assorted)", "quantity": "25", "purpose": "Cover minor cuts and scrapes", "priority": "essential"},
    {"item": "Gauze pads (4x4 in)", "quantity": "10", "purpose": "Cover larger wounds, control bleeding", "priority": "essential"},
    {"item": "Medical tape", "quantity": "1 roll", "purpose": "Secure gauze and bandages", "priority": "essential"},
    {"item": "Scissors", "quantity": "1 pair", "purpose": "Cut tape, gauze, clothing", "priority": "essential"},
    {"item": "Tweezers", "quantity": "1 pair", "purpose": "Remove splinters and debris", "priority": "essential"},
    {"item": "Antiseptic wipes", "quantity": "10", "purpose": "Clean wounds to prevent infection", "priority": "essential"},
    {"item": "Disposable gloves (nitrile)", "quantity": "4 pairs", "purpose": "Protect against bloodborne pathogens", "priority": "essential"},
    {"item": "CPR pocket mask", "quantity": "1", "purpose": "Barrier device for rescue breathing", "priority": "essential"},
    {"item": "Elastic bandage (ACE wrap)", "quantity": "2", "purpose": "Wrap sprains, strains, secure splints", "priority": "essential"},
    {"item": "Instant cold pack", "quantity": "2", "purpose": "Reduce swelling from injuries", "priority": "recommended"},
    {"item": "Emergency blanket (mylar)", "quantity": "1", "purpose": "Retain body heat, treat shock", "priority": "recommended"},
    {"item": "First aid manual", "quantity": "1", "purpose": "Reference guide for procedures", "priority": "recommended"},
    {"item": "Triangular bandage", "quantity": "2", "purpose": "Arm sling, tourniquet, bandage", "priority": "recommended"},
    {"item": "Antibiotic ointment", "quantity": "1 tube", "purpose": "Prevent infection in minor wounds", "priority": "recommended"},
    {"item": "Pain relievers (ibuprofen/acetaminophen)", "quantity": "1 bottle", "purpose": "Pain and fever management", "priority": "recommended"},
    {"item": "Eye wash solution", "quantity": "1 bottle", "purpose": "Flush chemicals or debris from eyes", "priority": "optional"},
    {"item": "Burn gel packets", "quantity": "5", "purpose": "Cool and soothe minor burns", "priority": "optional"},
    {"item": "Splint (SAM splint)", "quantity": "1", "purpose": "Immobilize suspected fractures", "priority": "optional"},
    {"item": "Whistle", "quantity": "1", "purpose": "Signal for help in emergencies", "priority": "optional"},
    {"item": "Flashlight with batteries", "quantity": "1", "purpose": "Illumination during emergencies", "priority": "optional"},
]

# ---------------------------------------------------------------------------
# CPR steps
# ---------------------------------------------------------------------------
CPR_STEPS = [
    {"step_number": 1, "action": "Check scene safety", "details": "Ensure the scene is safe for you and the victim before approaching.", "duration_seconds": 5},
    {"step_number": 2, "action": "Check responsiveness", "details": "Tap the person's shoulder and shout 'Are you okay?' Look for movement or response.", "duration_seconds": 10},
    {"step_number": 3, "action": "Call 911", "details": "Call 911 or have someone call. Get an AED if available.", "duration_seconds": 15},
    {"step_number": 4, "action": "Open airway", "details": "Tilt the head back and lift the chin to open the airway (head-tilt, chin-lift).", "duration_seconds": 5},
    {"step_number": 5, "action": "Check breathing", "details": "Look, listen, and feel for breathing for no more than 10 seconds.", "duration_seconds": 10},
    {"step_number": 6, "action": "30 chest compressions", "details": "Place heel of hand on center of chest. Push hard and fast, at least 2 inches deep, at 100-120 compressions per minute.", "duration_seconds": 18},
    {"step_number": 7, "action": "2 rescue breaths", "details": "Pinch the nose, seal your mouth over theirs, and give 2 breaths (1 second each). Watch for chest rise.", "duration_seconds": 4},
    {"step_number": 8, "action": "Repeat cycles", "details": "Continue cycles of 30 compressions and 2 breaths until help arrives or the person starts breathing.", "duration_seconds": 0},
]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def show_disclaimer():
    """Display the emergency disclaimer prominently."""
    from rich.console import Console
    from rich.panel import Panel

    console = Console()
    console.print(Panel(EMERGENCY_DISCLAIMER, border_style="red", title="🚨 Disclaimer"))
    console.print()


def get_severity_style(severity: str) -> str:
    """Return a rich style string based on severity level."""
    severity_lower = severity.lower()
    if "high" in severity_lower:
        return "bold red"
    elif "moderate" in severity_lower:
        return "bold yellow"
    return "green"


def evaluate_emergency(conscious: bool, breathing: bool, severe_bleeding: bool = False) -> dict:
    """Evaluate an emergency situation using the decision tree.

    Returns a dict with action, severity, call_911, and instructions.
    """
    logger.info(
        "Evaluating emergency: conscious=%s, breathing=%s, severe_bleeding=%s",
        conscious, breathing, severe_bleeding,
    )

    if not conscious:
        if breathing:
            action = EMERGENCY_DECISION_TREE["unconscious"]["breathing"]
            severity = "high"
            call_911 = True
            instructions = [
                "Do not move the person unless in immediate danger.",
                "Place them in the recovery position (on their side).",
                "Call 911 immediately.",
                "Monitor breathing until help arrives.",
                "Do not give food or drink.",
            ]
        else:
            action = EMERGENCY_DECISION_TREE["unconscious"]["not_breathing"]
            severity = "critical"
            call_911 = True
            instructions = [
                "Call 911 immediately.",
                "Begin CPR: 30 chest compressions, then 2 rescue breaths.",
                "Push hard and fast in the center of the chest (100-120 per minute).",
                "Use an AED if available.",
                "Continue until help arrives or the person starts breathing.",
            ]
    else:
        if breathing:
            if severe_bleeding:
                action = EMERGENCY_DECISION_TREE["conscious"]["breathing"]["severe_bleeding"]
                severity = "high"
                call_911 = True
                instructions = [
                    "Call 911 immediately.",
                    "Apply direct pressure to the wound with a clean cloth.",
                    "Do not remove the cloth; add more layers if needed.",
                    "Elevate the injured area above heart level if possible.",
                    "Keep the person calm and still.",
                ]
            else:
                action = EMERGENCY_DECISION_TREE["conscious"]["breathing"]["no_bleeding"]
                severity = "low"
                call_911 = False
                instructions = [
                    "Keep the person calm and comfortable.",
                    "Assess for visible injuries.",
                    "Monitor for changes in condition.",
                    "Seek medical attention if symptoms worsen.",
                ]
        else:
            action = EMERGENCY_DECISION_TREE["conscious"]["not_breathing"]
            severity = "critical"
            call_911 = True
            instructions = [
                "Call 911 immediately.",
                "Check for airway obstruction (choking).",
                "If choking, perform abdominal thrusts (Heimlich maneuver).",
                "If not choking, begin CPR.",
                "Continue until help arrives.",
            ]

    return {
        "action": action,
        "severity": severity,
        "call_911": call_911,
        "instructions": instructions,
    }


def get_supply_checklist(priority: str = "all") -> list[dict]:
    """Return the first aid supply checklist, optionally filtered by priority.

    Args:
        priority: One of 'essential', 'recommended', 'optional', or 'all'.
    """
    if priority == "all":
        return list(FIRST_AID_SUPPLIES)
    return [s for s in FIRST_AID_SUPPLIES if s["priority"] == priority]


def get_cpr_steps() -> list[dict]:
    """Return the CPR steps with timing information."""
    return list(CPR_STEPS)


# ---------------------------------------------------------------------------
# Emergency contact management
# ---------------------------------------------------------------------------

@dataclass
class EmergencyContact:
    """A single emergency contact."""

    name: str
    number: str
    relationship: str
    is_default: bool = False


class EmergencyContactManager:
    """Manage a list of emergency contacts (in-memory storage)."""

    def __init__(self) -> None:
        """Init."""
        self._contacts: list[EmergencyContact] = []

    def add_contact(self, contact: EmergencyContact) -> None:
        """Add an emergency contact. If marked default, unset previous default."""
        if contact.is_default:
            for c in self._contacts:
                c.is_default = False
        self._contacts.append(contact)
        logger.info("Added emergency contact: %s", contact.name)

    def remove_contact(self, name: str) -> bool:
        """Remove a contact by name. Returns True if found and removed."""
        for i, c in enumerate(self._contacts):
            if c.name == name:
                self._contacts.pop(i)
                logger.info("Removed emergency contact: %s", name)
                return True
        return False

    def get_contacts(self) -> list[EmergencyContact]:
        """Return all contacts."""
        return list(self._contacts)

    def get_default(self) -> EmergencyContact | None:
        """Return the default contact, or None."""
        for c in self._contacts:
            if c.is_default:
                return c
        return None
