"""Core business logic for GDPR Compliance Checker."""

import re
import json
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

class ComplianceStatus(str, Enum):
    COMPLIANT = "compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_ADDRESSED = "not_addressed"


SYSTEM_PROMPT = (
    "You are a GDPR compliance expert and data protection officer. Analyze documents, "
    "privacy policies, or code for GDPR compliance issues. Check for:\n"
    "1. Data collection and processing legality (Article 6)\n"
    "2. Consent mechanisms (Article 7)\n"
    "3. Data subject rights (Articles 15-22)\n"
    "4. Data retention policies (Article 5)\n"
    "5. Data protection by design (Article 25)\n"
    "6. Data breach notification procedures (Articles 33-34)\n"
    "7. Cross-border data transfer compliance (Articles 44-49)\n"
    "8. Data Processing Agreements (Article 28)\n\n"
    "Rate each area as: COMPLIANT ✅, PARTIALLY COMPLIANT ⚠️, NON-COMPLIANT ❌, or NOT ADDRESSED ❓\n"
    "Provide specific recommendations for each finding."
)

CHECK_TYPES = {
    "all": "all GDPR compliance areas",
    "consent": "consent mechanisms and data subject rights",
    "retention": "data retention and deletion policies",
    "transfer": "cross-border data transfer compliance",
    "security": "data security and breach notification",
    "rights": "data subject rights implementation",
}

# Article-by-article checklist
GDPR_ARTICLES = {
    "Art. 5": {"title": "Principles", "description": "Lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity, accountability"},
    "Art. 6": {"title": "Lawfulness of Processing", "description": "Legal basis for data processing (consent, contract, legal obligation, vital interests, public task, legitimate interests)"},
    "Art. 7": {"title": "Conditions for Consent", "description": "Demonstrable consent, clear distinguishable request, right to withdraw"},
    "Art. 12": {"title": "Transparent Information", "description": "Clear, plain language communication about data processing"},
    "Art. 13-14": {"title": "Information Provision", "description": "Information provided at collection (direct or indirect)"},
    "Art. 15": {"title": "Right of Access", "description": "Data subject's right to access their personal data"},
    "Art. 16": {"title": "Right to Rectification", "description": "Right to correct inaccurate personal data"},
    "Art. 17": {"title": "Right to Erasure", "description": "Right to be forgotten under specific conditions"},
    "Art. 18": {"title": "Right to Restriction", "description": "Right to restrict processing of personal data"},
    "Art. 20": {"title": "Data Portability", "description": "Right to receive data in structured, machine-readable format"},
    "Art. 21": {"title": "Right to Object", "description": "Right to object to processing based on legitimate interests or direct marketing"},
    "Art. 22": {"title": "Automated Decision-Making", "description": "Rights related to automated profiling and decision-making"},
    "Art. 25": {"title": "Data Protection by Design", "description": "Privacy by design and by default principles"},
    "Art. 28": {"title": "Data Processors", "description": "Binding contracts with data processors, sub-processor controls"},
    "Art. 30": {"title": "Records of Processing", "description": "Maintaining records of processing activities"},
    "Art. 32": {"title": "Security of Processing", "description": "Appropriate technical and organizational measures"},
    "Art. 33": {"title": "Breach Notification (Authority)", "description": "72-hour notification to supervisory authority"},
    "Art. 34": {"title": "Breach Notification (Subject)", "description": "Communication of breach to data subjects"},
    "Art. 35": {"title": "Data Protection Impact Assessment", "description": "DPIA for high-risk processing"},
    "Art. 37-39": {"title": "Data Protection Officer", "description": "Designation, position, and tasks of DPO"},
    "Art. 44-49": {"title": "International Transfers", "description": "Safeguards for cross-border data transfers"},
}


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class ChecklistItem:
    """A single GDPR compliance checklist item."""
    article: str
    title: str
    description: str
    status: ComplianceStatus = ComplianceStatus.NOT_ADDRESSED
    findings: str = ""
    recommendation: str = ""


@dataclass
class DataFlowEntry:
    """A data flow mapping entry."""
    data_type: str
    source: str
    destination: str
    purpose: str
    legal_basis: str = ""
    retention: str = ""
    cross_border: bool = False


@dataclass
class AuditLogEntry:
    """An audit trail entry."""
    timestamp: str
    action: str
    article: str
    status: str
    details: str = ""
    auditor: str = "system"


@dataclass
class DPORecommendation:
    """DPO recommendation for compliance improvement."""
    priority: str  # high, medium, low
    article: str
    finding: str
    recommendation: str
    deadline: str = ""


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def check_compliance(content: str, check_type: str) -> str:
    """Check content for GDPR compliance using LLM."""
    logger.info("Checking compliance (type=%s)", check_type)
    check_desc = CHECK_TYPES.get(check_type, check_type)

    prompt = (
        f"Analyze the following document/code for GDPR compliance.\n"
        f"Focus area: {check_desc}\n\n"
        f"DOCUMENT CONTENT:\n{content}\n\n"
        f"Provide a structured compliance report with findings, ratings, and recommendations."
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=3000,
    )


def generate_checklist(content: str) -> str:
    """Generate a GDPR compliance checklist using LLM."""
    logger.info("Generating compliance checklist")

    prompt = (
        f"Based on this document, generate a GDPR compliance checklist.\n"
        f"Each item should have: [Status] Item Description - Action Required\n\n"
        f"DOCUMENT:\n{content}"
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=2048,
    )


def build_article_checklist(content: str) -> list[ChecklistItem]:
    """Build an article-by-article compliance checklist from content analysis."""
    logger.info("Building article-by-article checklist")
    items: list[ChecklistItem] = []
    content_lower = content.lower()

    compliance_signals = {
        "Art. 5": ["lawful", "fair", "transparent", "purpose limitation", "data minimization", "accuracy"],
        "Art. 6": ["legal basis", "consent", "contract", "legitimate interest", "legal obligation"],
        "Art. 7": ["consent", "withdraw consent", "opt-in", "opt-out", "explicit consent"],
        "Art. 12": ["privacy policy", "plain language", "clear", "transparent"],
        "Art. 13-14": ["data controller", "purpose of processing", "recipients", "retention period"],
        "Art. 15": ["right of access", "access request", "subject access"],
        "Art. 16": ["rectification", "correct", "update personal data"],
        "Art. 17": ["erasure", "right to be forgotten", "delete", "deletion"],
        "Art. 18": ["restriction", "restrict processing"],
        "Art. 20": ["portability", "export data", "machine-readable", "download data"],
        "Art. 21": ["right to object", "opt out", "unsubscribe"],
        "Art. 22": ["automated decision", "profiling", "algorithm"],
        "Art. 25": ["privacy by design", "data protection by design", "by default"],
        "Art. 28": ["data processor", "sub-processor", "processing agreement"],
        "Art. 30": ["record of processing", "processing activities", "data register"],
        "Art. 32": ["encryption", "security measures", "access control", "pseudonymization"],
        "Art. 33": ["breach notification", "72 hours", "supervisory authority"],
        "Art. 34": ["notify data subjects", "breach communication"],
        "Art. 35": ["impact assessment", "dpia", "risk assessment"],
        "Art. 37-39": ["data protection officer", "dpo"],
        "Art. 44-49": ["international transfer", "cross-border", "adequacy decision", "standard contractual"],
    }

    for article, info in GDPR_ARTICLES.items():
        signals = compliance_signals.get(article, [])
        matches = [s for s in signals if s in content_lower]

        if len(matches) >= 2:
            status = ComplianceStatus.COMPLIANT
            findings = f"Document addresses: {', '.join(matches)}"
        elif len(matches) == 1:
            status = ComplianceStatus.PARTIALLY_COMPLIANT
            findings = f"Partially addressed: {matches[0]}"
        else:
            status = ComplianceStatus.NOT_ADDRESSED
            findings = "No relevant content found"

        items.append(ChecklistItem(
            article=article,
            title=info["title"],
            description=info["description"],
            status=status,
            findings=findings,
            recommendation=f"Review {article} requirements" if status != ComplianceStatus.COMPLIANT else "",
        ))

    return items


def map_data_flows(content: str) -> list[DataFlowEntry]:
    """Extract data flow mappings from document content."""
    logger.info("Mapping data flows")
    flows: list[DataFlowEntry] = []
    content_lower = content.lower()

    # Detect common data types
    data_types = {
        "email": ["email", "e-mail", "email address"],
        "name": ["name", "full name", "first name", "last name"],
        "phone": ["phone", "telephone", "mobile number"],
        "address": ["address", "postal", "zip code"],
        "payment": ["credit card", "payment", "billing", "bank account"],
        "health": ["health", "medical", "diagnosis"],
        "location": ["location", "gps", "geolocation", "ip address"],
        "browsing": ["cookies", "browsing history", "tracking", "analytics"],
    }

    purposes = {
        "marketing": ["marketing", "advertising", "promotional", "newsletter"],
        "analytics": ["analytics", "statistics", "tracking", "usage data"],
        "service": ["service provision", "account", "registration", "login"],
        "legal": ["legal obligation", "compliance", "regulatory"],
    }

    for dtype, keywords in data_types.items():
        if any(kw in content_lower for kw in keywords):
            detected_purposes = [
                p for p, pkws in purposes.items()
                if any(pk in content_lower for pk in pkws)
            ]
            for purpose in (detected_purposes or ["unspecified"]):
                flows.append(DataFlowEntry(
                    data_type=dtype,
                    source="user/data subject",
                    destination="data controller",
                    purpose=purpose,
                    cross_border="transfer" in content_lower or "third country" in content_lower,
                ))

    return flows


def generate_dpo_recommendations(checklist: list[ChecklistItem]) -> list[DPORecommendation]:
    """Generate DPO recommendations based on checklist results."""
    logger.info("Generating DPO recommendations")
    recs: list[DPORecommendation] = []

    priority_map = {
        ComplianceStatus.NON_COMPLIANT: "high",
        ComplianceStatus.NOT_ADDRESSED: "high",
        ComplianceStatus.PARTIALLY_COMPLIANT: "medium",
    }

    for item in checklist:
        if item.status in priority_map:
            recs.append(DPORecommendation(
                priority=priority_map[item.status],
                article=item.article,
                finding=item.findings,
                recommendation=f"Address {item.article} ({item.title}): {item.description}",
            ))

    # Sort by priority
    priority_order = {"high": 0, "medium": 1, "low": 2}
    recs.sort(key=lambda r: priority_order.get(r.priority, 3))
    return recs


def create_audit_entry(action: str, article: str, status: str,
                       details: str = "") -> AuditLogEntry:
    """Create an audit trail entry."""
    return AuditLogEntry(
        timestamp=datetime.now().isoformat(),
        action=action,
        article=article,
        status=status,
        details=details,
    )
