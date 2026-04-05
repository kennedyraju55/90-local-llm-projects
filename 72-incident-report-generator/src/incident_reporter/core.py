"""Core business logic for Incident Report Generator."""

import re
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

from common.llm_client import chat

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants & Enums
# ---------------------------------------------------------------------------

class Priority(str, Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"


SYSTEM_PROMPT = (
    "You are a senior incident response analyst. Given raw security logs or "
    "incident data, generate a professional incident report with:\n"
    "1. Executive Summary\n"
    "2. Incident Timeline (chronological events)\n"
    "3. Impact Assessment (affected systems, data, users)\n"
    "4. Root Cause Analysis\n"
    "5. Remediation Steps Taken\n"
    "6. Recommendations for Prevention\n"
    "7. Appendix (relevant log entries)\n\n"
    "Use clear, professional language suitable for management and technical teams.\n"
    "Format the report using markdown."
)

INCIDENT_TYPES = {
    "security": "security breach or unauthorized access",
    "outage": "service outage or downtime",
    "data-breach": "data breach or data leak",
    "malware": "malware infection or ransomware",
    "phishing": "phishing attack or social engineering",
    "general": "general IT incident",
}

# Priority-based templates
PRIORITY_TEMPLATES = {
    Priority.P1: {
        "label": "Critical / SEV-1",
        "response_time": "15 minutes",
        "update_frequency": "Every 30 minutes",
        "escalation": "VP Engineering + CISO immediately",
        "sections": [
            "Executive Summary", "Impact Assessment (revenue/users/data)",
            "Incident Timeline", "Root Cause Analysis", "Remediation Steps",
            "Customer Communication Plan", "Post-Mortem Schedule",
        ],
    },
    Priority.P2: {
        "label": "High / SEV-2",
        "response_time": "30 minutes",
        "update_frequency": "Every 1 hour",
        "escalation": "Engineering Manager + Security Lead",
        "sections": [
            "Executive Summary", "Impact Assessment",
            "Incident Timeline", "Root Cause Analysis",
            "Remediation Steps", "Recommendations",
        ],
    },
    Priority.P3: {
        "label": "Medium / SEV-3",
        "response_time": "2 hours",
        "update_frequency": "Every 4 hours",
        "escalation": "Team Lead",
        "sections": [
            "Summary", "Impact Assessment", "Timeline",
            "Resolution Steps", "Recommendations",
        ],
    },
    Priority.P4: {
        "label": "Low / SEV-4",
        "response_time": "Next business day",
        "update_frequency": "Daily",
        "escalation": "Team ticket queue",
        "sections": ["Summary", "Resolution", "Recommendations"],
    },
}

# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class TimelineEntry:
    """A single event in an incident timeline."""
    timestamp: str
    event: str
    severity: str = "info"
    actor: str = ""
    system: str = ""


@dataclass
class ImpactAssessment:
    """Impact assessment for an incident."""
    affected_users: int = 0
    affected_systems: list = field(default_factory=list)
    data_compromised: bool = False
    revenue_impact: str = "Unknown"
    downtime_minutes: int = 0
    severity_score: float = 0.0

    @property
    def severity_label(self) -> str:
        """Severity label."""
        if self.severity_score >= 9.0:
            return "CATASTROPHIC"
        elif self.severity_score >= 7.0:
            return "MAJOR"
        elif self.severity_score >= 4.0:
            return "MODERATE"
        elif self.severity_score >= 1.0:
            return "MINOR"
        return "NEGLIGIBLE"


@dataclass
class LessonsLearned:
    """Lessons learned entry."""
    category: str
    observation: str
    recommendation: str
    owner: str = ""
    deadline: str = ""


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def generate_report(logs: str, incident_type: str, title: str = None,
                    priority: Priority = Priority.P2) -> str:
    """Generate an incident report from raw logs."""
    logger.info("Generating report (type=%s, priority=%s)", incident_type, priority.value)

    type_desc = INCIDENT_TYPES.get(incident_type, incident_type)
    template = PRIORITY_TEMPLATES[priority]
    title_str = f"Report Title: {title}" if title else ""
    sections = ", ".join(template["sections"])

    prompt = (
        f"Generate a comprehensive incident report from the following logs/data.\n"
        f"Incident Type: {type_desc}\n"
        f"Priority: {template['label']}\n"
        f"Response Time SLA: {template['response_time']}\n"
        f"{title_str}\n\n"
        f"Required sections: {sections}\n\n"
        f"RAW LOGS/DATA:\n{logs}\n\n"
        f"Create a professional incident report with all required sections."
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=3000,
    )


def generate_timeline(logs: str) -> str:
    """Extract a timeline from incident logs."""
    logger.info("Generating timeline")

    prompt = (
        f"Extract a chronological timeline from these incident logs.\n"
        f"Format each entry as: [TIMESTAMP] - EVENT DESCRIPTION - SEVERITY\n\n"
        f"LOGS:\n{logs}"
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=1536,
    )


def build_timeline(logs: str) -> list[TimelineEntry]:
    """Parse logs into structured timeline entries."""
    logger.info("Building structured timeline")
    entries: list[TimelineEntry] = []

    timestamp_pattern = re.compile(
        r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+"
        r"(CRITICAL|ERROR|WARN(?:ING)?|INFO|DEBUG|ALERT):\s*(.*)"
    )

    for line in logs.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        match = timestamp_pattern.match(line)
        if match:
            entries.append(TimelineEntry(
                timestamp=match.group(1),
                severity=match.group(2).lower(),
                event=match.group(3),
            ))
        elif entries:
            entries[-1].event += f" {line}"

    return entries


def calculate_impact(logs: str, affected_users: int = 0,
                     downtime_minutes: int = 0) -> ImpactAssessment:
    """Calculate impact assessment from incident data."""
    logger.info("Calculating impact assessment")

    text_lower = logs.lower()

    # Detect data compromise signals
    data_signals = ["data breach", "data leak", "exfiltrat", "unauthorized access to data",
                    "database dump", "credential", "pii", "ssn", "credit card"]
    data_compromised = any(s in text_lower for s in data_signals)

    # Extract affected systems
    system_patterns = re.findall(
        r"(?:server|system|service|database|host|node)[:\s]+([^\s,;]+)",
        logs, re.IGNORECASE
    )
    affected_systems = list(set(system_patterns))[:10]

    # Calculate severity score
    severity_score = 0.0
    if data_compromised:
        severity_score += 4.0
    if downtime_minutes > 240:
        severity_score += 3.0
    elif downtime_minutes > 60:
        severity_score += 2.0
    elif downtime_minutes > 15:
        severity_score += 1.0
    if affected_users > 10000:
        severity_score += 3.0
    elif affected_users > 1000:
        severity_score += 2.0
    elif affected_users > 100:
        severity_score += 1.0

    critical_keywords = ["critical", "ransomware", "root access", "data breach"]
    severity_score += sum(0.5 for kw in critical_keywords if kw in text_lower)
    severity_score = min(severity_score, 10.0)

    # Revenue impact estimation
    if severity_score >= 8:
        revenue_impact = "Significant — customer-facing impact"
    elif severity_score >= 5:
        revenue_impact = "Moderate — partial service disruption"
    elif severity_score >= 2:
        revenue_impact = "Low — internal impact only"
    else:
        revenue_impact = "Negligible"

    return ImpactAssessment(
        affected_users=affected_users,
        affected_systems=affected_systems,
        data_compromised=data_compromised,
        revenue_impact=revenue_impact,
        downtime_minutes=downtime_minutes,
        severity_score=round(severity_score, 1),
    )


def generate_lessons_learned(logs: str, incident_type: str) -> str:
    """Generate lessons learned from an incident."""
    logger.info("Generating lessons learned")

    prompt = (
        f"Based on this {incident_type} incident, generate a structured lessons learned report.\n"
        f"For each lesson include:\n"
        f"- Category (Detection / Response / Prevention / Communication)\n"
        f"- What happened vs what should have happened\n"
        f"- Specific action items with owners and deadlines\n\n"
        f"INCIDENT DATA:\n{logs}"
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )


def get_template(priority: Priority) -> dict:
    """Get the report template for a given priority level."""
    return PRIORITY_TEMPLATES.get(priority, PRIORITY_TEMPLATES[Priority.P2])
