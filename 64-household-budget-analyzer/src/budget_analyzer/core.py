#!/usr/bin/env python3
"""Core budget analysis engine with AI-powered insights."""

import sys
import os
import csv
import json
import logging
import math
from datetime import datetime, timedelta
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

# LLM client integration
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from common.llm_client import generate, check_ollama_running

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'config.yaml')


def load_config(config_path: Optional[str] = None) -> dict:
    """Load application configuration from YAML file."""
    path = config_path or DEFAULT_CONFIG_PATH
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            cfg = yaml.safe_load(f)
            logger.info("Configuration loaded from %s", path)
            return cfg or {}
    logger.warning("Config file not found at %s – using defaults", path)
    return {}


_CONFIG: dict = {}


def get_config(config_path: Optional[str] = None) -> dict:
    """Return cached configuration, loading on first call."""
    global _CONFIG
    if not _CONFIG:
        _CONFIG = load_config(config_path)
    return _CONFIG


def setup_logging(level: Optional[str] = None) -> None:
    """Configure logging for the application."""
    cfg = get_config()
    log_level = level or cfg.get('app', {}).get('log_level', 'INFO')
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _parse_amount(raw: str) -> float:
    """Parse a currency string into a float."""
    try:
        return float(str(raw).replace("$", "").replace(",", ""))
    except (ValueError, TypeError):
        return 0.0


def _parse_date(date_str: str) -> Optional[datetime]:
    """Try multiple date formats and return a datetime or None."""
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def _get_field(row: dict, *keys: str, default: str = "") -> str:
    """Get first matching field from a row (case-insensitive fallback)."""
    for k in keys:
        if k in row:
            return row[k]
    return default

# ---------------------------------------------------------------------------
# Original functions (preserved)
# ---------------------------------------------------------------------------


def load_expenses(file_path: str) -> list[dict]:
    """Load expenses from a CSV file."""
    if not os.path.exists(file_path):
        logger.error("File '%s' not found.", file_path)
        raise FileNotFoundError(f"File '{file_path}' not found.")
    try:
        expenses: list[dict] = []
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append(row)
        if not expenses:
            logger.warning("No expenses found in file '%s'.", file_path)
        logger.info("Loaded %d expenses from '%s'.", len(expenses), file_path)
        return expenses
    except Exception as e:
        logger.error("Error reading CSV: %s", e)
        raise


def filter_by_month(expenses: list[dict], month_str: str) -> list[dict]:
    """Filter expenses by month string like 'March 2024'."""
    if not month_str:
        return expenses
    try:
        target = datetime.strptime(month_str, "%B %Y")
    except ValueError:
        logger.warning("Could not parse month '%s'. Returning all.", month_str)
        return expenses

    filtered: list[dict] = []
    for exp in expenses:
        date_str = _get_field(exp, "date", "Date")
        dt = _parse_date(date_str)
        if dt and dt.year == target.year and dt.month == target.month:
            filtered.append(exp)
    logger.info("Filtered to %d expenses for '%s'.", len(filtered), month_str)
    return filtered


def compute_category_breakdown(expenses: list[dict]) -> dict:
    """Compute spending by category."""
    categories: dict[str, float] = defaultdict(float)
    for exp in expenses:
        category = _get_field(exp, "category", "Category") or "Uncategorized"
        amount = _parse_amount(_get_field(exp, "amount", "Amount", default="0"))
        categories[category] += amount
    return dict(sorted(categories.items(), key=lambda x: x[1], reverse=True))


def compute_total(expenses: list[dict]) -> float:
    """Compute total spending."""
    total = 0.0
    for exp in expenses:
        total += _parse_amount(_get_field(exp, "amount", "Amount", default="0"))
    return total


def display_breakdown(categories: dict, total: float) -> None:
    """Display category breakdown in a table (requires rich)."""
    from rich.console import Console
    from rich.table import Table

    console = Console()
    table = Table(title="💰 Expense Breakdown", show_lines=True)
    table.add_column("Category", style="cyan", min_width=18)
    table.add_column("Amount", style="green", justify="right", min_width=12)
    table.add_column("Percentage", style="yellow", justify="right", min_width=10)

    for category, amount in categories.items():
        pct = (amount / total * 100) if total > 0 else 0
        bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
        table.add_row(category, f"${amount:,.2f}", f"{pct:.1f}% {bar}")

    table.add_row("[bold]TOTAL[/bold]", f"[bold]${total:,.2f}[/bold]", "100%", style="bold")
    console.print(table)


def analyze_budget(expenses: list[dict], categories: dict, total: float, month: str) -> str:
    """Use AI to analyze budget and provide savings suggestions."""
    expense_summary = json.dumps({
        "total": total,
        "categories": categories,
        "num_transactions": len(expenses),
        "period": month or "all time",
    }, indent=2)

    prompt = f"""Analyze this household budget:

{expense_summary}

Please provide:
1. **Spending Analysis**: Overall assessment of spending patterns
2. **Top Expense Areas**: Where most money is going and if amounts seem reasonable
3. **Savings Opportunities**: Specific, actionable suggestions to reduce spending
4. **Budget Recommendations**: Suggested budget percentages per category
5. **Trend Insights**: Observations about spending habits
6. **Monthly Savings Goal**: Realistic savings target based on the data

Be specific with dollar amounts and percentages."""

    cfg = get_config()
    llm_cfg = cfg.get('llm', {})
    return generate(
        prompt=prompt,
        system_prompt=llm_cfg.get('system_prompt', "You are an expert financial advisor specializing in household budgets."),
        temperature=llm_cfg.get('temperature', 0.5),
    )


def compare_months(expenses: list[dict]) -> str:
    """Compare spending across months using AI."""
    monthly: dict[str, float] = defaultdict(float)
    for exp in expenses:
        date_str = _get_field(exp, "date", "Date")
        dt = _parse_date(date_str)
        if dt:
            key = dt.strftime("%B %Y")
            monthly[key] += _parse_amount(_get_field(exp, "amount", "Amount", default="0"))

    if not monthly:
        return "No monthly data available for comparison."

    prompt = f"""Compare monthly spending trends:

{json.dumps(dict(monthly), indent=2)}

Provide:
1. **Month-over-Month Change**: How spending changed
2. **Highest/Lowest Months**: Peak and trough spending
3. **Trend Direction**: Is spending increasing or decreasing?
4. **Recommendations**: How to maintain budget discipline"""

    cfg = get_config()
    llm_cfg = cfg.get('llm', {})
    return generate(
        prompt=prompt,
        system_prompt="You are a household budget trend analyst.",
        temperature=llm_cfg.get('temperature', 0.5),
    )

# ---------------------------------------------------------------------------
# NEW: Category Rules Engine
# ---------------------------------------------------------------------------


def categorize_expense(description: str, config: Optional[dict] = None) -> str:
    """Auto-categorize an expense based on keyword rules from config.

    Returns the matched category name or 'Other'.
    """
    cfg = config or get_config()
    rules: dict = cfg.get('budget', {}).get('category_rules', {})
    desc_lower = description.lower()
    for category, keywords in rules.items():
        for keyword in keywords:
            if keyword.lower() in desc_lower:
                logger.debug("Categorized '%s' as '%s' (keyword: %s)", description, category, keyword)
                return category
    return "Other"

# ---------------------------------------------------------------------------
# NEW: Budget vs Actual Comparison
# ---------------------------------------------------------------------------


def compare_budget_vs_actual(categories: dict, config: Optional[dict] = None) -> list[dict]:
    """Compare actual spending against budget limits.

    Returns a list of dicts with keys: category, budget, actual, difference, status.
    """
    cfg = config or get_config()
    budget_limits: dict = cfg.get('budget', {}).get('categories', {})
    results: list[dict] = []

    all_categories = set(list(budget_limits.keys()) + list(categories.keys()))
    for cat in sorted(all_categories):
        budget = budget_limits.get(cat, 0)
        actual = categories.get(cat, 0.0)
        diff = budget - actual
        status = "under" if diff >= 0 else "over"
        results.append({
            "category": cat,
            "budget": budget,
            "actual": round(actual, 2),
            "difference": round(diff, 2),
            "status": status,
        })
    return results

# ---------------------------------------------------------------------------
# NEW: Savings Goals Tracking
# ---------------------------------------------------------------------------


@dataclass
class SavingsGoal:
    """Track progress toward a savings goal."""

    name: str
    target_amount: float
    current_amount: float = 0.0
    monthly_contribution: float = 0.0
    start_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))

    def track_progress(self) -> dict:
        """Return progress information."""
        pct = (self.current_amount / self.target_amount * 100) if self.target_amount > 0 else 0
        return {
            "name": self.name,
            "target": self.target_amount,
            "current": self.current_amount,
            "remaining": round(self.target_amount - self.current_amount, 2),
            "percent_complete": round(min(pct, 100.0), 1),
        }

    def estimate_completion(self) -> Optional[str]:
        """Estimate completion date based on monthly contribution.

        Returns ISO-format date string or None if cannot be estimated.
        """
        remaining = self.target_amount - self.current_amount
        if remaining <= 0:
            return datetime.now().strftime("%Y-%m-%d")
        if self.monthly_contribution <= 0:
            return None
        months_needed = math.ceil(remaining / self.monthly_contribution)
        est = datetime.now() + timedelta(days=months_needed * 30)
        return est.strftime("%Y-%m-%d")

# ---------------------------------------------------------------------------
# NEW: Recurring Expense Detection
# ---------------------------------------------------------------------------


def detect_recurring(expenses: list[dict], tolerance: float = 0.1) -> list[dict]:
    """Detect expenses that recur monthly (same description ± tolerance on amount).

    Returns a list of dicts with keys: description, avg_amount, occurrences, months.
    """
    by_desc: dict[str, list[dict]] = defaultdict(list)
    for exp in expenses:
        desc = _get_field(exp, "description", "Description").strip()
        if desc:
            by_desc[desc].append(exp)

    recurring: list[dict] = []
    for desc, items in by_desc.items():
        if len(items) < 2:
            continue

        amounts = [_parse_amount(_get_field(it, "amount", "Amount", default="0")) for it in items]
        avg = sum(amounts) / len(amounts) if amounts else 0
        # Check if amounts are within tolerance of average
        if avg > 0 and all(abs(a - avg) / avg <= tolerance for a in amounts):
            months_seen: set[str] = set()
            for it in items:
                dt = _parse_date(_get_field(it, "date", "Date"))
                if dt:
                    months_seen.add(dt.strftime("%Y-%m"))
            if len(months_seen) >= 2:
                recurring.append({
                    "description": desc,
                    "avg_amount": round(avg, 2),
                    "occurrences": len(items),
                    "months": sorted(months_seen),
                })

    recurring.sort(key=lambda x: x['avg_amount'], reverse=True)
    logger.info("Detected %d recurring expenses.", len(recurring))
    return recurring

# ---------------------------------------------------------------------------
# NEW: Monthly Trends
# ---------------------------------------------------------------------------


def compute_monthly_trends(expenses: list[dict]) -> dict[str, float]:
    """Compute total spending per month, sorted chronologically.

    Returns {\"2024-01\": 500.0, \"2024-02\": 620.0, ...}
    """
    monthly: dict[str, float] = defaultdict(float)
    for exp in expenses:
        dt = _parse_date(_get_field(exp, "date", "Date"))
        if dt:
            key = dt.strftime("%Y-%m")
            monthly[key] += _parse_amount(_get_field(exp, "amount", "Amount", default="0"))

    return {k: round(v, 2) for k, v in sorted(monthly.items())}

# ---------------------------------------------------------------------------
# NEW: Top Expenses
# ---------------------------------------------------------------------------


def get_top_expenses(expenses: list[dict], n: int = 10) -> list[dict]:
    """Return the top N highest individual transactions.

    Each entry has keys: date, description, category, amount.
    """
    parsed: list[dict] = []
    for exp in expenses:
        amount = _parse_amount(_get_field(exp, "amount", "Amount", default="0"))
        parsed.append({
            "date": _get_field(exp, "date", "Date"),
            "description": _get_field(exp, "description", "Description"),
            "category": _get_field(exp, "category", "Category") or "Uncategorized",
            "amount": round(amount, 2),
        })
    parsed.sort(key=lambda x: x['amount'], reverse=True)
    return parsed[:n]
