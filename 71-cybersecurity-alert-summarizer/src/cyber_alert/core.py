"""Core business logic for Cybersecurity Alert Summarizer."""

import re
import json
import logging
import hashlib
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

from common.llm_client import chat

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants & Enums
# ---------------------------------------------------------------------------

class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


SYSTEM_PROMPT = (
    "You are a senior cybersecurity analyst. Your job is to analyze security alerts "
    "and CVE reports, then provide:\n"
    "1. A concise summary of the threat\n"
    "2. Severity assessment (Critical/High/Medium/Low)\n"
    "3. Affected systems and attack vectors\n"
    "4. Recommended mitigations and immediate actions\n"
    "5. Priority ranking if multiple alerts are provided\n\n"
    "Format your response in clear sections with markdown headers."
)

# Common CVE pattern
CVE_PATTERN = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)

# IOC patterns
IOC_PATTERNS = {
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "ipv6": re.compile(r"\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b"),
    "domain": re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+(?:com|net|org|io|ru|cn|xyz|top|info|biz)\b"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
    "md5": re.compile(r"\b[a-fA-F0-9]{32}\b"),
    "sha1": re.compile(r"\b[a-fA-F0-9]{40}\b"),
    "sha256": re.compile(r"\b[a-fA-F0-9]{64}\b"),
    "url": re.compile(r"https?://[^\s<>\"']+"),
    "file_path": re.compile(r"(?:/[\w.-]+)+|(?:[A-Z]:\\[\w\\.-]+)"),
}

# Known CVE database (sample entries for offline lookup)
CVE_DATABASE = {
    "CVE-2024-3094": {
        "description": "XZ Utils backdoor - supply chain compromise",
        "cvss": 10.0,
        "severity": "critical",
        "affected": "xz-utils 5.6.0-5.6.1",
        "vector": "Supply Chain / Backdoor",
    },
    "CVE-2024-21762": {
        "description": "Fortinet FortiOS out-of-bound write vulnerability",
        "cvss": 9.8,
        "severity": "critical",
        "affected": "FortiOS 7.4.0-7.4.2, 7.2.0-7.2.6",
        "vector": "Remote Code Execution",
    },
    "CVE-2023-44228": {
        "description": "Log4Shell - Apache Log4j2 JNDI injection",
        "cvss": 10.0,
        "severity": "critical",
        "affected": "Apache Log4j2 < 2.17.0",
        "vector": "Remote Code Execution",
    },
    "CVE-2023-4966": {
        "description": "Citrix Bleed - information disclosure vulnerability",
        "cvss": 9.4,
        "severity": "critical",
        "affected": "Citrix NetScaler ADC/Gateway",
        "vector": "Information Disclosure",
    },
}

# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class IOCResult:
    """Indicator of Compromise extraction result."""
    ioc_type: str
    value: str
    context: str = ""


@dataclass
class CVEInfo:
    """CVE database lookup result."""
    cve_id: str
    description: str = "Unknown"
    cvss: float = 0.0
    severity: str = "unknown"
    affected: str = "Unknown"
    vector: str = "Unknown"
    found_in_db: bool = False


@dataclass
class ThreatScore:
    """Threat intelligence scoring result."""
    overall_score: float = 0.0
    severity: Severity = Severity.INFO
    confidence: float = 0.0
    factors: dict = field(default_factory=dict)

    @property
    def label(self) -> str:
        """Label."""
        if self.overall_score >= 9.0:
            return "CRITICAL"
        elif self.overall_score >= 7.0:
            return "HIGH"
        elif self.overall_score >= 4.0:
            return "MEDIUM"
        elif self.overall_score >= 1.0:
            return "LOW"
        return "INFO"


@dataclass
class AlertCorrelation:
    """Correlation result between alerts."""
    alert_ids: list = field(default_factory=list)
    correlation_type: str = ""
    confidence: float = 0.0
    description: str = ""


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def summarize_alert(alert_text: str, severity_filter: str = "all") -> str:
    """Summarize a security alert using the LLM."""
    logger.info("Summarizing alert (severity_filter=%s)", severity_filter)

    prompt = (
        f"Analyze the following security alert and provide a comprehensive summary.\n"
        f"Focus on severity level: {severity_filter}\n\n"
        f"ALERT DATA:\n{alert_text}\n\n"
        f"Provide: threat summary, severity assessment, affected systems, attack vectors, "
        f"recommended mitigations, and priority ranking."
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )


def prioritize_alerts(alert_text: str) -> str:
    """Prioritize multiple alerts by risk level."""
    logger.info("Prioritizing alerts")

    prompt = (
        f"Review these security alerts and prioritize them by risk level.\n"
        f"For each alert provide: priority rank, severity, immediate action required (yes/no), "
        f"and a one-line justification.\n\n"
        f"ALERTS:\n{alert_text}"
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=1536,
    )


def extract_iocs(text: str) -> list[IOCResult]:
    """Extract Indicators of Compromise from alert text."""
    logger.info("Extracting IOCs from text (%d chars)", len(text))
    results: list[IOCResult] = []
    seen = set()

    for ioc_type, pattern in IOC_PATTERNS.items():
        for match in pattern.finditer(text):
            value = match.group()
            key = f"{ioc_type}:{value}"
            if key not in seen:
                seen.add(key)
                start = max(0, match.start() - 40)
                end = min(len(text), match.end() + 40)
                context = text[start:end].strip()
                results.append(IOCResult(ioc_type=ioc_type, value=value, context=context))

    logger.info("Found %d IOCs", len(results))
    return results


def lookup_cve(cve_id: str) -> CVEInfo:
    """Look up CVE information from the local database."""
    cve_id = cve_id.upper()
    logger.info("Looking up CVE: %s", cve_id)

    if cve_id in CVE_DATABASE:
        entry = CVE_DATABASE[cve_id]
        return CVEInfo(
            cve_id=cve_id,
            description=entry["description"],
            cvss=entry["cvss"],
            severity=entry["severity"],
            affected=entry["affected"],
            vector=entry["vector"],
            found_in_db=True,
        )

    return CVEInfo(cve_id=cve_id, found_in_db=False)


def extract_cves(text: str) -> list[CVEInfo]:
    """Extract and look up all CVE identifiers from text."""
    cve_ids = CVE_PATTERN.findall(text)
    unique_cves = list(dict.fromkeys(cve_ids))
    logger.info("Found %d unique CVEs in text", len(unique_cves))
    return [lookup_cve(cve_id) for cve_id in unique_cves]


def calculate_threat_score(alert_text: str) -> ThreatScore:
    """Calculate a threat intelligence score for an alert."""
    logger.info("Calculating threat score")
    factors = {}

    # CVE severity factor
    cves = extract_cves(alert_text)
    max_cvss = max((c.cvss for c in cves if c.found_in_db), default=0.0)
    factors["cve_severity"] = min(max_cvss, 10.0)

    # IOC density factor
    iocs = extract_iocs(alert_text)
    ioc_count = len(iocs)
    factors["ioc_density"] = min(ioc_count / 5.0, 10.0)

    # Keyword-based severity signals
    critical_keywords = [
        "remote code execution", "rce", "zero-day", "0-day", "ransomware",
        "data breach", "exfiltration", "rootkit", "backdoor", "supply chain",
    ]
    high_keywords = [
        "privilege escalation", "sql injection", "xss", "authentication bypass",
        "unauthorized access", "brute force", "credential",
    ]

    text_lower = alert_text.lower()
    crit_hits = sum(1 for kw in critical_keywords if kw in text_lower)
    high_hits = sum(1 for kw in high_keywords if kw in text_lower)
    factors["keyword_severity"] = min((crit_hits * 3.0 + high_hits * 1.5), 10.0)

    # Overall score (weighted average)
    weights = {"cve_severity": 0.4, "ioc_density": 0.2, "keyword_severity": 0.4}
    overall = sum(factors[k] * weights[k] for k in weights)
    factors["weights"] = weights

    # Determine severity
    if overall >= 8.0:
        severity = Severity.CRITICAL
    elif overall >= 6.0:
        severity = Severity.HIGH
    elif overall >= 3.5:
        severity = Severity.MEDIUM
    elif overall >= 1.0:
        severity = Severity.LOW
    else:
        severity = Severity.INFO

    confidence = min(0.3 + (len(cves) * 0.15) + (ioc_count * 0.05), 1.0)

    return ThreatScore(
        overall_score=round(overall, 2),
        severity=severity,
        confidence=round(confidence, 2),
        factors=factors,
    )


def correlate_alerts(alerts: list[str]) -> list[AlertCorrelation]:
    """Find correlations between multiple alerts."""
    logger.info("Correlating %d alerts", len(alerts))
    correlations: list[AlertCorrelation] = []

    alert_iocs: list[list[IOCResult]] = [extract_iocs(a) for a in alerts]
    alert_cves: list[list[CVEInfo]] = [extract_cves(a) for a in alerts]

    for i in range(len(alerts)):
        for j in range(i + 1, len(alerts)):
            # Check for shared IOCs
            iocs_i = {ioc.value for ioc in alert_iocs[i]}
            iocs_j = {ioc.value for ioc in alert_iocs[j]}
            shared_iocs = iocs_i & iocs_j

            if shared_iocs:
                correlations.append(AlertCorrelation(
                    alert_ids=[i, j],
                    correlation_type="shared_iocs",
                    confidence=min(len(shared_iocs) * 0.25, 1.0),
                    description=f"Shared IOCs: {', '.join(list(shared_iocs)[:5])}",
                ))

            # Check for shared CVEs
            cves_i = {c.cve_id for c in alert_cves[i]}
            cves_j = {c.cve_id for c in alert_cves[j]}
            shared_cves = cves_i & cves_j

            if shared_cves:
                correlations.append(AlertCorrelation(
                    alert_ids=[i, j],
                    correlation_type="shared_cves",
                    confidence=min(len(shared_cves) * 0.35, 1.0),
                    description=f"Shared CVEs: {', '.join(shared_cves)}",
                ))

    return correlations
