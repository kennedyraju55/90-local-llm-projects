"""
KPI Dashboard Reporter - Core business logic.

Provides KPI data loading, trend computation, goal tracking,
anomaly detection, and LLM-powered report generation.
"""

import csv
import json
import logging
import math
import os
import sys
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

from common.llm_client import chat, check_ollama_running

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {
    "model": {"name": "gemma3", "temperature": 0.3, "max_tokens": 3500},
    "targets": {},
    "anomaly_detection": {"enabled": True, "threshold": 2.0},
    "moving_average": {"window": 3},
    "alert_threshold_pct": 10,
    "periods": ["monthly", "quarterly", "yearly"],
    "logging": {"level": "INFO", "file": "kpi_reporter.log"},
}


def load_config(path: str = "config.yaml") -> dict:
    """Load configuration from a YAML file, falling back to defaults."""
    config = DEFAULT_CONFIG.copy()
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                user_config = yaml.safe_load(f) or {}
            _deep_merge(config, user_config)
            logger.info("Loaded configuration from %s", path)
        except Exception as e:
            logger.warning("Failed to load config from %s: %s. Using defaults.", path, e)
    else:
        logger.info("Config file %s not found, using defaults.", path)
    return config


def _deep_merge(base: dict, override: dict) -> None:
    """Recursively merge override into base dict."""
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value


def load_kpi_data(file_path: str) -> list[dict]:
    """Load KPI data from a CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        List of row dictionaries.

    Raises:
        FileNotFoundError: If file does not exist.
        ValueError: If file is empty or unreadable.
    """
    if not os.path.exists(file_path):
        logger.error("File not found: %s", file_path)
        raise FileNotFoundError(f"File '{file_path}' not found.")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            logger.error("CSV file is empty: %s", file_path)
            raise ValueError(f"CSV file '{file_path}' is empty.")
        logger.info("Loaded %d rows from %s", len(rows), file_path)
        return rows
    except (ValueError, FileNotFoundError):
        raise
    except Exception as e:
        logger.error("Error reading CSV %s: %s", file_path, e)
        raise ValueError(f"Error reading CSV '{file_path}': {e}") from e


def safe_float(val: Any) -> float:
    """Safely convert a value to float, stripping $, %, and commas."""
    try:
        return float(str(val).replace(",", "").replace("$", "").replace("%", ""))
    except (ValueError, TypeError):
        return 0.0


def _detect_period_column(data: list[dict]) -> str:
    """Auto-detect the period/date column from data."""
    candidates = ["period", "month", "date", "week", "quarter", "year"]
    for candidate in candidates:
        for col in data[0].keys():
            if candidate in col.lower():
                return col
    return list(data[0].keys())[0]


def compute_kpi_trends(data: list[dict]) -> dict:
    """Compute trends and changes for each KPI column.

    Returns a dict mapping KPI name to trend info including:
    latest, previous, change, change_pct, average, min, max, trend arrow,
    periods list, and raw values.
    """
    if len(data) < 2:
        logger.warning("Insufficient data for trend computation (need >= 2 rows).")
        return {}

    period_col = _detect_period_column(data)
    trends: dict[str, dict] = {}

    for col in data[0].keys():
        if col == period_col:
            continue
        values = [safe_float(row.get(col, 0)) for row in data]
        if not any(v != 0 for v in values):
            continue

        latest = values[-1]
        previous = values[-2] if len(values) >= 2 else latest
        change = latest - previous
        change_pct = (change / previous * 100) if previous != 0 else 0
        avg = sum(values) / len(values)
        trend = "↑" if change > 0 else ("↓" if change < 0 else "→")

        trends[col] = {
            "latest": latest,
            "previous": previous,
            "change": change,
            "change_pct": change_pct,
            "average": avg,
            "min": min(values),
            "max": max(values),
            "trend": trend,
            "periods": [row.get(period_col, "") for row in data],
            "values": values,
        }

    logger.info("Computed trends for %d KPIs.", len(trends))
    return trends


def track_goals(trends: dict, targets: dict) -> dict:
    """Compare KPI actuals vs target values.

    Args:
        trends: Output of compute_kpi_trends().
        targets: Dict mapping KPI name -> target value.

    Returns:
        Dict mapping KPI name -> {actual, target, pct_of_goal, status}.
    """
    goals: dict[str, dict] = {}
    for kpi, target_val in targets.items():
        if kpi not in trends:
            logger.debug("KPI '%s' has a target but no trend data.", kpi)
            continue
        target_val = safe_float(target_val)
        if target_val == 0:
            continue
        actual = trends[kpi]["latest"]
        pct_of_goal = (actual / target_val) * 100

        if pct_of_goal >= 100:
            status = "achieved"
        elif pct_of_goal >= 80:
            status = "on_track"
        elif pct_of_goal >= 50:
            status = "at_risk"
        else:
            status = "behind"

        goals[kpi] = {
            "actual": actual,
            "target": target_val,
            "pct_of_goal": pct_of_goal,
            "status": status,
        }
        logger.debug("Goal %s: %.1f%% of target (status=%s)", kpi, pct_of_goal, status)

    logger.info("Tracked goals for %d KPIs.", len(goals))
    return goals


def detect_anomalies(trends: dict, threshold: float = 2.0) -> list[dict]:
    """Detect anomalous KPI values using standard deviation.

    A value is anomalous if it is more than `threshold` standard deviations
    from the mean.

    Returns:
        List of anomaly dicts with kpi, value, mean, std_dev, deviation info.
    """
    anomalies: list[dict] = []
    for kpi, info in trends.items():
        values = info["values"]
        if len(values) < 3:
            continue
        mean = sum(values) / len(values)
        variance = sum((v - mean) ** 2 for v in values) / len(values)
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            continue

        for i, val in enumerate(values):
            deviation = abs(val - mean) / std_dev
            if deviation > threshold:
                period = info["periods"][i] if i < len(info["periods"]) else f"Period {i}"
                anomalies.append({
                    "kpi": kpi,
                    "period": period,
                    "value": val,
                    "mean": mean,
                    "std_dev": std_dev,
                    "deviation": deviation,
                })
                logger.info(
                    "Anomaly detected: %s=%s in %s (%.1f σ from mean)",
                    kpi, val, period, deviation,
                )

    return anomalies


def compute_moving_average(values: list[float], window: int = 3) -> list[float]:
    """Compute a simple moving average over a list of values.

    Args:
        values: List of numeric values.
        window: Window size for the moving average.

    Returns:
        List of moving average values (same length as input; early values
        use available data).
    """
    if not values or window < 1:
        return []
    result: list[float] = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        window_vals = values[start : i + 1]
        result.append(sum(window_vals) / len(window_vals))
    return result


def generate_kpi_report(data: list[dict], trends: dict, period: str) -> str:
    """Generate a narrative KPI report using the LLM."""
    data_text = "\n".join(str(row) for row in data)
    trends_summary = {}
    for kpi, info in trends.items():
        trends_summary[kpi] = {
            "latest": info["latest"],
            "previous": info["previous"],
            "change_pct": f"{info['change_pct']:.1f}%",
            "trend": info["trend"],
            "average": info["average"],
        }
    trends_text = json.dumps(trends_summary, indent=2)

    system_prompt = (
        "You are a business intelligence analyst. Write a professional KPI narrative "
        "report. Highlight wins, flag concerns, and provide actionable insights. "
        "Use specific numbers. Format with markdown headings and bullet points."
    )

    messages = [{"role": "user", "content": (
        f"Generate a KPI narrative report for {period} reporting period.\n\n"
        f"Raw Data:\n{data_text}\n\n"
        f"KPI Trends:\n{trends_text}\n\n"
        "Include:\n"
        "1. Performance Highlights\n"
        "2. Areas of Concern\n"
        "3. Period-over-Period Analysis\n"
        "4. Key Takeaways & Recommendations"
    )}]

    logger.info("Generating KPI narrative report for period: %s", period)
    return chat(messages, system_prompt=system_prompt, temperature=0.3, max_tokens=3500)


def generate_executive_summary(
    trends: dict, goals: dict, anomalies: list[dict]
) -> str:
    """Generate an executive summary using the LLM.

    Combines trends, goal status, and anomaly info into a concise summary.
    """
    summary_data = {
        "kpi_count": len(trends),
        "goals_achieved": sum(1 for g in goals.values() if g["status"] == "achieved"),
        "goals_at_risk": sum(1 for g in goals.values() if g["status"] in ("at_risk", "behind")),
        "anomaly_count": len(anomalies),
        "top_performers": [],
        "concerns": [],
    }
    for kpi, info in trends.items():
        entry = {"kpi": kpi, "change_pct": f"{info['change_pct']:.1f}%", "trend": info["trend"]}
        if info["change_pct"] > 5:
            summary_data["top_performers"].append(entry)
        elif info["change_pct"] < -5:
            summary_data["concerns"].append(entry)

    system_prompt = (
        "You are a C-suite executive advisor. Write a concise executive summary "
        "(3-5 bullet points) highlighting key business performance, risks, and "
        "recommended actions. Be data-driven and specific."
    )

    messages = [{"role": "user", "content": (
        "Generate an executive summary from this KPI analysis:\n\n"
        f"{json.dumps(summary_data, indent=2)}\n\n"
        "Anomalies detected:\n"
        f"{json.dumps(anomalies, indent=2) if anomalies else 'None'}\n\n"
        "Goal tracking:\n"
        f"{json.dumps(goals, indent=2) if goals else 'No targets configured'}"
    )}]

    logger.info("Generating executive summary.")
    return chat(messages, system_prompt=system_prompt, temperature=0.3, max_tokens=2000)


def generate_alert_summary(trends: dict, threshold_pct: float = 10.0) -> str:
    """Generate alerts for KPIs with significant changes.

    Args:
        trends: Output of compute_kpi_trends().
        threshold_pct: Percentage change threshold for alerting.
    """
    alerts: list[str] = []
    for kpi, data in trends.items():
        if abs(data["change_pct"]) > threshold_pct:
            direction = "increased" if data["change_pct"] > 0 else "decreased"
            alerts.append(
                f"⚠️ **{kpi}** {direction} by {abs(data['change_pct']):.1f}% "
                f"({data['previous']:,.2f} → {data['latest']:,.2f})"
            )

    if alerts:
        return "## 🔔 Alerts\n\n" + "\n".join(alerts)
    return "## ✅ No Significant Alerts\n\nAll KPIs within normal range."


def compute_analytics(trends: dict, goals: dict) -> dict:
    """Compute aggregate analytics across all KPIs.

    Returns summary statistics useful for dashboards and reporting.
    """
    analytics: dict[str, Any] = {
        "total_kpis": len(trends),
        "improving": sum(1 for t in trends.values() if t["change"] > 0),
        "declining": sum(1 for t in trends.values() if t["change"] < 0),
        "stable": sum(1 for t in trends.values() if t["change"] == 0),
        "avg_change_pct": 0.0,
        "goals_summary": {
            "total": len(goals),
            "achieved": sum(1 for g in goals.values() if g["status"] == "achieved"),
            "on_track": sum(1 for g in goals.values() if g["status"] == "on_track"),
            "at_risk": sum(1 for g in goals.values() if g["status"] == "at_risk"),
            "behind": sum(1 for g in goals.values() if g["status"] == "behind"),
        },
    }
    if trends:
        analytics["avg_change_pct"] = sum(
            t["change_pct"] for t in trends.values()
        ) / len(trends)

    logger.info("Computed analytics: %d KPIs, %d goals.", len(trends), len(goals))
    return analytics


def setup_logging(config: dict) -> None:
    """Configure logging from config dict."""
    log_config = config.get("logging", {})
    level = getattr(logging, log_config.get("level", "INFO").upper(), logging.INFO)
    log_file = log_config.get("file")

    handlers: list[logging.Handler] = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=handlers,
    )
    logger.info("Logging configured: level=%s", logging.getLevelName(level))
