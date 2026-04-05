"""Core business logic for Log File Analyzer."""

import re
import logging
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

from common.llm_client import chat

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants & Enums
# ---------------------------------------------------------------------------

class LogLevel(str, Enum):
    CRITICAL = "critical"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"


SYSTEM_PROMPT = (
    "You are a senior systems engineer and log analysis expert. Analyze log files to:\n"
    "1. Identify error patterns and anomalies\n"
    "2. Cluster related errors together\n"
    "3. Determine root causes\n"
    "4. Suggest remediation steps\n"
    "5. Highlight critical issues requiring immediate attention\n\n"
    "Provide structured analysis with severity levels and actionable recommendations.\n"
    "Format your response using markdown with clear sections."
)

FOCUS_AREAS = {
    "errors": "error messages, exceptions, and failures",
    "warnings": "warning messages and potential issues",
    "security": "security-related events, unauthorized access, authentication failures",
    "performance": "performance issues, slow queries, timeouts, resource exhaustion",
    "all": "all notable events and patterns",
}

# Pattern library for common log patterns
PATTERN_LIBRARY = {
    "database_error": {
        "pattern": re.compile(r"(?:database|db|sql|mysql|postgres|mongo)\s+(?:error|timeout|connection|fail)", re.IGNORECASE),
        "severity": LogLevel.ERROR,
        "category": "Database",
        "description": "Database connectivity or query error",
    },
    "auth_failure": {
        "pattern": re.compile(r"(?:auth|authentication|login|password)\s+(?:fail|error|denied|invalid|unauthorized)", re.IGNORECASE),
        "severity": LogLevel.WARNING,
        "category": "Security",
        "description": "Authentication or authorization failure",
    },
    "http_error": {
        "pattern": re.compile(r"HTTP\s+[45]\d{2}|status[:\s]+[45]\d{2}", re.IGNORECASE),
        "severity": LogLevel.ERROR,
        "category": "HTTP",
        "description": "HTTP client/server error",
    },
    "timeout": {
        "pattern": re.compile(r"timeout|timed?\s*out|deadline\s+exceeded", re.IGNORECASE),
        "severity": LogLevel.ERROR,
        "category": "Performance",
        "description": "Operation timeout",
    },
    "memory_issue": {
        "pattern": re.compile(r"out\s+of\s+memory|oom|memory\s+(?:leak|exceeded|high|usage\s*:?\s*\d{2,3}%)", re.IGNORECASE),
        "severity": LogLevel.CRITICAL,
        "category": "Resources",
        "description": "Memory exhaustion or leak",
    },
    "disk_issue": {
        "pattern": re.compile(r"disk\s+(?:full|space|quota)|no\s+space\s+left|storage\s+(?:full|exceeded)", re.IGNORECASE),
        "severity": LogLevel.CRITICAL,
        "category": "Resources",
        "description": "Disk space issue",
    },
    "connection_error": {
        "pattern": re.compile(r"connection\s+(?:refused|reset|closed|lost|error)|ECONNREFUSED|ECONNRESET", re.IGNORECASE),
        "severity": LogLevel.ERROR,
        "category": "Network",
        "description": "Network connection error",
    },
    "ssl_tls_error": {
        "pattern": re.compile(r"ssl|tls|certificate\s+(?:error|expired|invalid|verify)", re.IGNORECASE),
        "severity": LogLevel.ERROR,
        "category": "Security",
        "description": "SSL/TLS certificate or handshake error",
    },
    "crash": {
        "pattern": re.compile(r"(?:segfault|segmentation\s+fault|core\s+dump|fatal|panic|unhandled\s+exception)", re.IGNORECASE),
        "severity": LogLevel.CRITICAL,
        "category": "Application",
        "description": "Application crash or fatal error",
    },
    "rate_limit": {
        "pattern": re.compile(r"rate\s+limit|throttl|too\s+many\s+requests|429", re.IGNORECASE),
        "severity": LogLevel.WARNING,
        "category": "Performance",
        "description": "Rate limiting triggered",
    },
}

# Alert rules
DEFAULT_ALERT_RULES = {
    "critical_threshold": 1,     # Alert on first critical
    "error_rate_threshold": 10,  # Alert if > 10 errors
    "auth_fail_threshold": 5,    # Alert if > 5 auth failures
    "timeout_threshold": 3,      # Alert if > 3 timeouts
}

# Timestamp patterns
TIMESTAMP_PATTERN = re.compile(
    r"(\d{4}-\d{2}-\d{2}[\sT]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:?\d{2})?)"
)

LOG_LEVEL_PATTERN = re.compile(
    r"\b(CRITICAL|FATAL|ERROR|ERR|WARN(?:ING)?|INFO|DEBUG|TRACE|ALERT|EMERG)\b", re.IGNORECASE
)

# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class PatternMatch:
    """A matched log pattern."""
    pattern_name: str
    category: str
    severity: LogLevel
    description: str
    line_number: int
    line_text: str
    timestamp: str = ""


@dataclass
class ErrorCluster:
    """A cluster of similar errors."""
    cluster_id: int
    pattern: str
    count: int
    severity: LogLevel
    first_seen: str = ""
    last_seen: str = ""
    example_lines: list = field(default_factory=list)


@dataclass
class TimelineEvent:
    """A timeline event extracted from logs."""
    timestamp: str
    level: str
    message: str
    line_number: int


@dataclass
class AnomalyResult:
    """An anomaly detection result."""
    anomaly_type: str
    description: str
    severity: LogLevel
    evidence: list = field(default_factory=list)
    score: float = 0.0


@dataclass
class AlertRule:
    """An alert rule definition."""
    name: str
    condition: str
    threshold: int
    current_value: int = 0
    triggered: bool = False


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def read_log_file(filepath: str, last_n: int = None) -> str:
    """Read a log file, optionally only the last N lines."""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        if last_n:
            lines = f.readlines()
            return "".join(lines[-last_n:])
        return f.read()


def analyze_logs(log_content: str, focus: str, context: str = None) -> str:
    """Analyze log content using the LLM."""
    logger.info("Analyzing logs (focus=%s)", focus)
    focus_desc = FOCUS_AREAS.get(focus, focus)
    context_str = f"\nSystem context: {context}" if context else ""

    prompt = (
        f"Analyze these log entries with focus on: {focus_desc}{context_str}\n\n"
        f"LOG ENTRIES:\n{log_content}\n\n"
        f"Provide:\n1. Summary of findings\n2. Error patterns detected\n"
        f"3. Root cause analysis\n4. Severity-ranked issues\n5. Recommended actions"
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=3000,
    )


def cluster_errors(log_content: str) -> str:
    """Cluster similar errors using LLM."""
    logger.info("Clustering errors with LLM")

    prompt = (
        f"Group and cluster similar errors in these logs.\n"
        f"For each cluster provide: error type, count estimate, example entry, likely cause.\n\n"
        f"LOGS:\n{log_content}"
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.2,
        max_tokens=2048,
    )


def match_patterns(log_content: str) -> list[PatternMatch]:
    """Match known patterns in log content."""
    logger.info("Matching patterns in log content")
    matches: list[PatternMatch] = []

    for line_num, line in enumerate(log_content.splitlines(), 1):
        for name, pattern_info in PATTERN_LIBRARY.items():
            if pattern_info["pattern"].search(line):
                # Extract timestamp if present
                ts_match = TIMESTAMP_PATTERN.search(line)
                timestamp = ts_match.group(1) if ts_match else ""

                matches.append(PatternMatch(
                    pattern_name=name,
                    category=pattern_info["category"],
                    severity=pattern_info["severity"],
                    description=pattern_info["description"],
                    line_number=line_num,
                    line_text=line.strip()[:200],
                    timestamp=timestamp,
                ))

    logger.info("Found %d pattern matches", len(matches))
    return matches


def detect_anomalies(log_content: str) -> list[AnomalyResult]:
    """Detect anomalies in log content."""
    logger.info("Detecting anomalies")
    anomalies: list[AnomalyResult] = []
    lines = log_content.splitlines()

    # Error burst detection
    error_lines = []
    for i, line in enumerate(lines):
        level_match = LOG_LEVEL_PATTERN.search(line)
        if level_match and level_match.group(1).upper() in ("ERROR", "ERR", "CRITICAL", "FATAL"):
            error_lines.append(i)

    # Check for error bursts (>5 errors in 10 consecutive lines)
    for i in range(len(error_lines) - 4):
        if error_lines[i + 4] - error_lines[i] <= 10:
            anomalies.append(AnomalyResult(
                anomaly_type="error_burst",
                description=f"Error burst detected: 5+ errors in {error_lines[i+4]-error_lines[i]+1} lines",
                severity=LogLevel.CRITICAL,
                evidence=[lines[error_lines[j]].strip()[:100] for j in range(i, i + 5)],
                score=0.9,
            ))
            break

    # Repeated message detection
    line_counter = Counter(line.strip() for line in lines if line.strip())
    for line_text, count in line_counter.most_common(5):
        if count >= 10:
            anomalies.append(AnomalyResult(
                anomaly_type="repeated_message",
                description=f"Message repeated {count} times",
                severity=LogLevel.WARNING,
                evidence=[line_text[:100]],
                score=min(count / 50.0, 1.0),
            ))

    # Timestamp gap detection
    timestamps = []
    for line in lines:
        ts_match = TIMESTAMP_PATTERN.search(line)
        if ts_match:
            try:
                ts_str = ts_match.group(1).replace("T", " ").replace("Z", "")
                ts = datetime.fromisoformat(ts_str[:19])
                timestamps.append(ts)
            except (ValueError, TypeError):
                pass

    if len(timestamps) >= 2:
        for i in range(1, len(timestamps)):
            gap = (timestamps[i] - timestamps[i-1]).total_seconds()
            if gap > 3600:  # >1 hour gap
                anomalies.append(AnomalyResult(
                    anomaly_type="timestamp_gap",
                    description=f"Large time gap: {gap/3600:.1f} hours between log entries",
                    severity=LogLevel.WARNING,
                    evidence=[f"From {timestamps[i-1]} to {timestamps[i]}"],
                    score=min(gap / 86400, 1.0),
                ))
                break

    return anomalies


def cluster_errors_local(log_content: str) -> list[ErrorCluster]:
    """Cluster similar errors locally (no LLM)."""
    logger.info("Clustering errors locally")
    clusters: dict[str, list[str]] = defaultdict(list)

    for line in log_content.splitlines():
        level_match = LOG_LEVEL_PATTERN.search(line)
        if level_match and level_match.group(1).upper() in ("ERROR", "ERR", "CRITICAL", "FATAL"):
            # Normalize the error message for clustering
            normalized = re.sub(r"\d+", "N", line.strip())
            normalized = re.sub(r"0x[0-9a-fA-F]+", "ADDR", normalized)
            normalized = re.sub(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP", normalized)
            clusters[normalized[:80]].append(line.strip())

    result: list[ErrorCluster] = []
    for idx, (pattern, lines) in enumerate(sorted(clusters.items(), key=lambda x: -len(x[1]))):
        if not lines:
            continue
        # Extract severity
        level = LogLevel.ERROR
        if any("CRITICAL" in l.upper() or "FATAL" in l.upper() for l in lines):
            level = LogLevel.CRITICAL

        # Extract timestamps
        timestamps = []
        for l in lines:
            ts_match = TIMESTAMP_PATTERN.search(l)
            if ts_match:
                timestamps.append(ts_match.group(1))

        result.append(ErrorCluster(
            cluster_id=idx,
            pattern=pattern[:80],
            count=len(lines),
            severity=level,
            first_seen=timestamps[0] if timestamps else "",
            last_seen=timestamps[-1] if timestamps else "",
            example_lines=lines[:3],
        ))

    return result[:20]  # Top 20 clusters


def build_timeline(log_content: str) -> list[TimelineEvent]:
    """Build a timeline of events from log content."""
    logger.info("Building timeline")
    events: list[TimelineEvent] = []

    for line_num, line in enumerate(log_content.splitlines(), 1):
        ts_match = TIMESTAMP_PATTERN.search(line)
        level_match = LOG_LEVEL_PATTERN.search(line)

        if ts_match:
            timestamp = ts_match.group(1)
            level = level_match.group(1).upper() if level_match else "INFO"
            # Extract message (everything after timestamp and level)
            msg = line.strip()
            events.append(TimelineEvent(
                timestamp=timestamp,
                level=level,
                message=msg[:200],
                line_number=line_num,
            ))

    return events


def evaluate_alert_rules(log_content: str,
                         rules: dict = None) -> list[AlertRule]:
    """Evaluate alert rules against log content."""
    logger.info("Evaluating alert rules")
    if rules is None:
        rules = DEFAULT_ALERT_RULES

    matches = match_patterns(log_content)
    lines = log_content.splitlines()

    # Count by category
    level_counts = Counter()
    for line in lines:
        lm = LOG_LEVEL_PATTERN.search(line)
        if lm:
            level_counts[lm.group(1).upper()] += 1

    pattern_counts = Counter(m.pattern_name for m in matches)

    results = [
        AlertRule(
            name="Critical Events",
            condition=f"Critical count > {rules['critical_threshold']}",
            threshold=rules["critical_threshold"],
            current_value=level_counts.get("CRITICAL", 0) + level_counts.get("FATAL", 0),
        ),
        AlertRule(
            name="Error Rate",
            condition=f"Error count > {rules['error_rate_threshold']}",
            threshold=rules["error_rate_threshold"],
            current_value=level_counts.get("ERROR", 0) + level_counts.get("ERR", 0),
        ),
        AlertRule(
            name="Auth Failures",
            condition=f"Auth failures > {rules['auth_fail_threshold']}",
            threshold=rules["auth_fail_threshold"],
            current_value=pattern_counts.get("auth_failure", 0),
        ),
        AlertRule(
            name="Timeouts",
            condition=f"Timeouts > {rules['timeout_threshold']}",
            threshold=rules["timeout_threshold"],
            current_value=pattern_counts.get("timeout", 0),
        ),
    ]

    for rule in results:
        rule.triggered = rule.current_value > rule.threshold

    return results
