"""Core business logic for Password Strength Advisor."""

import math
import re
import string
import secrets
import hashlib
import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

from common.llm_client import chat

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants & Enums
# ---------------------------------------------------------------------------

class StrengthLevel(str, Enum):
    VERY_WEAK = "very_weak"
    WEAK = "weak"
    FAIR = "fair"
    STRONG = "strong"
    VERY_STRONG = "very_strong"


SYSTEM_PROMPT = (
    "You are a cybersecurity expert specializing in password security and "
    "authentication best practices. You provide:\n"
    "1. Password policy analysis with NIST SP 800-63B compliance checks\n"
    "2. Strength assessment and vulnerability identification\n"
    "3. Improvement recommendations following industry best practices\n"
    "4. Explanation of common attack vectors (brute force, dictionary, rainbow tables)\n\n"
    "Always reference current security standards (NIST, OWASP) in your recommendations.\n"
    "Format your response using markdown."
)

# Common password patterns to penalize
COMMON_PATTERNS = [
    r"^[a-z]+$", r"^[A-Z]+$", r"^[0-9]+$",
    r"^(.)\1+$",  # repeated char
    r"(012|123|234|345|456|567|678|789|890)",  # sequential digits
    r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop)",  # sequential letters
    r"(qwerty|asdf|zxcv|password|admin|login|welcome|letmein)",  # common words
]

# Well-known breached password prefixes (SHA-1 first 5 chars for k-anonymity concept)
KNOWN_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
    "dragon", "111111", "baseball", "iloveyou", "trustno1", "sunshine", "princess",
    "football", "shadow", "superman", "michael", "password1", "admin", "letmein",
}

# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class EntropyResult:
    """Password entropy calculation result."""
    entropy_bits: float
    charset_size: int
    effective_length: int
    time_to_crack: str
    strength: StrengthLevel
    details: dict = field(default_factory=dict)


@dataclass
class BreachCheckResult:
    """Breach database check result (conceptual)."""
    is_compromised: bool
    source: str = "local_dictionary"
    occurrences: int = 0
    recommendation: str = ""


@dataclass
class PolicyRule:
    """A single password policy rule."""
    name: str
    description: str
    enabled: bool = True
    value: str = ""


@dataclass
class BulkAnalysisResult:
    """Result of analyzing a single password in bulk mode."""
    index: int
    masked: str
    entropy: float
    strength: StrengthLevel
    issues: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def calculate_entropy(password: str) -> EntropyResult:
    """Calculate password entropy in bits."""
    logger.info("Calculating entropy for password of length %d", len(password))

    if not password:
        return EntropyResult(
            entropy_bits=0, charset_size=0, effective_length=0,
            time_to_crack="instant", strength=StrengthLevel.VERY_WEAK,
        )

    charset_size = 0
    details = {}

    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    has_space = " " in password

    if has_lower:
        charset_size += 26
        details["lowercase"] = True
    if has_upper:
        charset_size += 26
        details["uppercase"] = True
    if has_digit:
        charset_size += 10
        details["digits"] = True
    if has_special:
        charset_size += 32
        details["special"] = True
    if has_space:
        charset_size += 1
        details["spaces"] = True

    if charset_size == 0:
        charset_size = 1

    # Effective length with pattern penalty
    effective_length = len(password)
    pattern_penalty = 0
    for pattern in COMMON_PATTERNS:
        if re.search(pattern, password, re.IGNORECASE):
            pattern_penalty += 0.3

    effective_length = max(1, int(effective_length * (1.0 - min(pattern_penalty, 0.7))))

    # Shannon entropy
    entropy_bits = effective_length * math.log2(charset_size)
    details["char_types"] = sum([has_lower, has_upper, has_digit, has_special])
    details["pattern_penalty"] = round(pattern_penalty, 2)

    # Time to crack estimation (10B guesses/sec)
    guesses = 2 ** entropy_bits
    seconds = guesses / 10_000_000_000
    if seconds < 1:
        time_to_crack = "instant"
    elif seconds < 60:
        time_to_crack = f"{seconds:.0f} seconds"
    elif seconds < 3600:
        time_to_crack = f"{seconds / 60:.0f} minutes"
    elif seconds < 86400:
        time_to_crack = f"{seconds / 3600:.0f} hours"
    elif seconds < 86400 * 365:
        time_to_crack = f"{seconds / 86400:.0f} days"
    elif seconds < 86400 * 365 * 1000:
        time_to_crack = f"{seconds / (86400 * 365):.0f} years"
    else:
        time_to_crack = "centuries+"

    # Strength classification
    if entropy_bits >= 80:
        strength = StrengthLevel.VERY_STRONG
    elif entropy_bits >= 60:
        strength = StrengthLevel.STRONG
    elif entropy_bits >= 40:
        strength = StrengthLevel.FAIR
    elif entropy_bits >= 25:
        strength = StrengthLevel.WEAK
    else:
        strength = StrengthLevel.VERY_WEAK

    return EntropyResult(
        entropy_bits=round(entropy_bits, 2),
        charset_size=charset_size,
        effective_length=effective_length,
        time_to_crack=time_to_crack,
        strength=strength,
        details=details,
    )


def check_breach_database(password: str) -> BreachCheckResult:
    """Check if a password is in known breach databases (conceptual local check)."""
    logger.info("Checking password against breach database")

    if password.lower() in KNOWN_WEAK_PASSWORDS:
        return BreachCheckResult(
            is_compromised=True,
            source="local_dictionary",
            occurrences=1000000,
            recommendation="This password is extremely common and appears in breach databases. Choose a unique password.",
        )

    # Check common variations (l33t speak, etc.)
    simplified = password.lower().replace("@", "a").replace("3", "e").replace("1", "i").replace("0", "o").replace("$", "s")
    if simplified in KNOWN_WEAK_PASSWORDS:
        return BreachCheckResult(
            is_compromised=True,
            source="local_dictionary_leet",
            occurrences=50000,
            recommendation="This password is a common variation of a known breached password.",
        )

    return BreachCheckResult(
        is_compromised=False,
        recommendation="Password not found in local breach dictionary. Consider checking against HaveIBeenPwned API.",
    )


def generate_policy(requirements: dict = None) -> list[PolicyRule]:
    """Generate a password policy based on NIST SP 800-63B."""
    logger.info("Generating password policy")

    defaults = {
        "min_length": "12",
        "max_length": "128",
        "require_mfa": "true",
        "check_breaches": "true",
        "no_rotation": "true",
        "no_complexity_rules": "true",
    }

    if requirements:
        defaults.update(requirements)

    return [
        PolicyRule("Minimum Length", f"Passwords must be at least {defaults['min_length']} characters", True, defaults["min_length"]),
        PolicyRule("Maximum Length", f"Allow passwords up to {defaults['max_length']} characters", True, defaults["max_length"]),
        PolicyRule("No Mandatory Rotation", "Do NOT require periodic password changes (NIST 800-63B)", defaults["no_rotation"] == "true"),
        PolicyRule("No Complexity Rules", "Do NOT enforce arbitrary complexity (e.g., must have special char). Allow all Unicode.", defaults["no_complexity_rules"] == "true"),
        PolicyRule("Breach Database Check", "Check passwords against known breach databases before acceptance", defaults["check_breaches"] == "true"),
        PolicyRule("Multi-Factor Authentication", "Require MFA for all accounts", defaults["require_mfa"] == "true"),
        PolicyRule("Block Common Passwords", "Reject passwords from dictionary of commonly-used passwords", True),
        PolicyRule("Rate Limiting", "Implement rate limiting on authentication attempts", True),
        PolicyRule("Secure Storage", "Hash passwords with bcrypt/scrypt/Argon2 with proper salt", True),
        PolicyRule("Password Meter", "Show real-time password strength feedback during creation", True),
    ]


def analyze_password_llm(password: str) -> str:
    """Analyze a password using the LLM (masked characteristics only)."""
    logger.info("Analyzing password with LLM")

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    char_types = sum([has_upper, has_lower, has_digit, has_special])
    entropy = calculate_entropy(password)

    prompt = (
        f"Analyze a password with these characteristics (actual password NOT shown for security):\n"
        f"- Length: {length} characters\n"
        f"- Contains uppercase: {has_upper}\n"
        f"- Contains lowercase: {has_lower}\n"
        f"- Contains digits: {has_digit}\n"
        f"- Contains special characters: {has_special}\n"
        f"- Character types used: {char_types}/4\n"
        f"- Estimated entropy: {entropy.entropy_bits:.1f} bits\n"
        f"- Time to crack: {entropy.time_to_crack}\n\n"
        f"Provide detailed analysis, estimated entropy, time to crack, and recommendations."
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=1024,
    )


def analyze_policy_llm(policy_text: str) -> str:
    """Analyze a password policy using the LLM."""
    logger.info("Analyzing password policy with LLM")

    prompt = (
        f"Analyze this password policy against NIST SP 800-63B and OWASP guidelines.\n"
        f"Identify weaknesses, compliance gaps, and provide specific improvement recommendations.\n\n"
        f"PASSWORD POLICY:\n{policy_text}\n\n"
        f"Rate each aspect: STRONG ✅, ADEQUATE ⚠️, WEAK ❌\n"
        f"Include: minimum length, complexity requirements, rotation policy, MFA, breach checking."
    )

    return chat(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SYSTEM_PROMPT,
        temperature=0.3,
        max_tokens=2048,
    )


def generate_password(length: int = 16, requirements: str = "upper,lower,digits,special") -> str:
    """Generate a cryptographically secure password."""
    reqs = [r.strip().lower() for r in requirements.split(",")]
    charset = ""
    mandatory = []

    if "upper" in reqs:
        charset += string.ascii_uppercase
        mandatory.append(secrets.choice(string.ascii_uppercase))
    if "lower" in reqs:
        charset += string.ascii_lowercase
        mandatory.append(secrets.choice(string.ascii_lowercase))
    if "digits" in reqs:
        charset += string.digits
        mandatory.append(secrets.choice(string.digits))
    if "special" in reqs:
        charset += string.punctuation
        mandatory.append(secrets.choice(string.punctuation))

    if not charset:
        charset = string.ascii_letters + string.digits + string.punctuation
        mandatory = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation),
        ]

    remaining = max(0, length - len(mandatory))
    password_chars = mandatory + [secrets.choice(charset) for _ in range(remaining)]

    # Fisher-Yates shuffle
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def bulk_analyze(passwords: list[str]) -> list[BulkAnalysisResult]:
    """Analyze multiple passwords in bulk."""
    logger.info("Bulk analyzing %d passwords", len(passwords))
    results: list[BulkAnalysisResult] = []

    for idx, pwd in enumerate(passwords):
        entropy = calculate_entropy(pwd)
        breach = check_breach_database(pwd)
        issues = []

        if entropy.entropy_bits < 40:
            issues.append("Low entropy")
        if len(pwd) < 8:
            issues.append("Too short")
        if breach.is_compromised:
            issues.append("Found in breach database")

        masked = pwd[0] + "*" * (len(pwd) - 2) + pwd[-1] if len(pwd) > 2 else "***"

        results.append(BulkAnalysisResult(
            index=idx,
            masked=masked,
            entropy=entropy.entropy_bits,
            strength=entropy.strength,
            issues=issues,
        ))

    return results
