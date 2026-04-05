"""Core logic for Stock Report Generator."""

import os
import sys
import csv
import json
import logging
from typing import Any, Dict, List, Optional, Tuple, Union

import yaml

logger = logging.getLogger(__name__)

_config: Optional[dict] = None


def load_config(config_path: str = None) -> dict:
    """Load configuration from config.yaml."""
    global _config
    if _config is not None and config_path is None:
        return _config
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")
    try:
        with open(config_path, "r") as f:
            _config = yaml.safe_load(f) or {}
    except FileNotFoundError:
        logger.warning("Config file not found at %s, using defaults", config_path)
        _config = {}
    return _config


def get_llm_client() -> Tuple[Any, ...]:
    """Get LLM client with proper path setup."""
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    parent_dir = os.path.dirname(project_root)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    from common.llm_client import chat, check_ollama_running
    return chat, check_ollama_running


def load_stock_data(file_path: str) -> list[dict]:
    """Load stock data from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            raise ValueError("CSV file is empty.")
        logger.info("Loaded %d data points from %s", len(rows), file_path)
        return rows
    except Exception as e:
        if isinstance(e, (FileNotFoundError, ValueError)):
            raise
        raise ValueError(f"Error reading CSV: {e}")


def _find_close_column(data: list[dict]) -> str:
    """Find the close price column in the data."""
    for candidate in ["Close", "close", "Adj Close", "adj_close", "price", "Price"]:
        if candidate in data[0]:
            return candidate
    return list(data[0].keys())[-1]


def _extract_prices(data: list[dict], close_col: str) -> list[float]:
    """Extract numeric prices from data."""
    prices = []
    for row in data:
        try:
            prices.append(float(row[close_col].replace(",", "")))
        except (ValueError, KeyError):
            continue
    return prices


def compute_metrics(data: list[dict]) -> dict:
    """Compute basic technical analysis metrics from stock data."""
    close_col = _find_close_column(data)
    prices = _extract_prices(data, close_col)

    if len(prices) < 2:
        return {"error": "Insufficient price data"}

    current = prices[-1]
    previous = prices[0]
    high = max(prices)
    low = min(prices)
    avg = sum(prices) / len(prices)
    change_pct = ((current - previous) / previous) * 100

    sma_5 = sum(prices[-5:]) / min(5, len(prices)) if len(prices) >= 5 else avg
    sma_20 = sum(prices[-20:]) / min(20, len(prices)) if len(prices) >= 20 else avg

    variance = sum((p - avg) ** 2 for p in prices) / len(prices)
    volatility = variance ** 0.5

    returns = [(prices[i] - prices[i - 1]) / prices[i - 1] * 100 for i in range(1, len(prices))]
    avg_daily_return = sum(returns) / len(returns) if returns else 0
    positive_days = sum(1 for r in returns if r > 0)
    negative_days = sum(1 for r in returns if r < 0)

    return {
        "current_price": current,
        "period_start_price": previous,
        "period_high": high,
        "period_low": low,
        "average_price": avg,
        "change_percent": change_pct,
        "sma_5": sma_5,
        "sma_20": sma_20,
        "volatility": volatility,
        "avg_daily_return": avg_daily_return,
        "positive_days": positive_days,
        "negative_days": negative_days,
        "total_data_points": len(prices),
    }


def compute_technical_indicators(data: list[dict]) -> dict:
    """Compute advanced technical indicators."""
    close_col = _find_close_column(data)
    prices = _extract_prices(data, close_col)

    if len(prices) < 14:
        return {"rsi": None, "bollinger": None, "macd": None}

    # RSI (14-period)
    gains, losses = [], []
    for i in range(1, min(15, len(prices))):
        diff = prices[i] - prices[i - 1]
        gains.append(diff if diff > 0 else 0)
        losses.append(abs(diff) if diff < 0 else 0)

    avg_gain = sum(gains) / len(gains) if gains else 0
    avg_loss = sum(losses) / len(losses) if losses else 0.001
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    # Bollinger Bands (20-period)
    period = min(20, len(prices))
    recent = prices[-period:]
    bb_mean = sum(recent) / len(recent)
    bb_std = (sum((p - bb_mean) ** 2 for p in recent) / len(recent)) ** 0.5
    bollinger = {
        "upper": round(bb_mean + 2 * bb_std, 2),
        "middle": round(bb_mean, 2),
        "lower": round(bb_mean - 2 * bb_std, 2),
    }

    # MACD (simplified)
    ema_12 = sum(prices[-12:]) / min(12, len(prices))
    ema_26 = sum(prices[-26:]) / min(26, len(prices))
    macd_line = ema_12 - ema_26
    signal = "bullish" if macd_line > 0 else "bearish"

    return {
        "rsi": round(rsi, 2),
        "rsi_signal": "overbought" if rsi > 70 else ("oversold" if rsi < 30 else "neutral"),
        "bollinger": bollinger,
        "macd_line": round(macd_line, 2),
        "macd_signal": signal,
    }


def assess_risk(metrics: dict, indicators: dict) -> dict:
    """Assess investment risk based on metrics and indicators."""
    risk_factors = []
    risk_score = 50  # Start neutral

    volatility = metrics.get("volatility", 0)
    avg_price = metrics.get("average_price", 1)
    vol_ratio = volatility / avg_price * 100 if avg_price > 0 else 0

    if vol_ratio > 5:
        risk_factors.append("High volatility relative to price")
        risk_score += 15
    elif vol_ratio > 2:
        risk_factors.append("Moderate volatility")
        risk_score += 5

    change = metrics.get("change_percent", 0)
    if abs(change) > 20:
        risk_factors.append(f"Large price movement: {change:.1f}%")
        risk_score += 10

    if indicators:
        rsi = indicators.get("rsi")
        if rsi and (rsi > 70 or rsi < 30):
            risk_factors.append(f"RSI at extreme level: {rsi}")
            risk_score += 10

    neg_days = metrics.get("negative_days", 0)
    pos_days = metrics.get("positive_days", 1)
    if neg_days > pos_days:
        risk_factors.append("More down days than up days")
        risk_score += 10

    risk_score = min(100, max(0, risk_score))
    risk_level = "low" if risk_score < 35 else ("medium" if risk_score < 65 else "high")

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "risk_factors": risk_factors,
    }


def compare_tickers(datasets: dict[str, list[dict]]) -> dict:
    """Compare metrics across multiple tickers."""
    comparison = {}
    for ticker, data in datasets.items():
        metrics = compute_metrics(data)
        if "error" not in metrics:
            comparison[ticker] = metrics
    return comparison


def generate_report(data: list[dict], metrics: dict, ticker: str,
                    indicators: dict = None, risk: dict = None) -> str:
    """Generate a narrative analysis report using the LLM."""
    chat, _ = get_llm_client()
    sample_start = "\n".join(str(row) for row in data[:3])
    sample_end = "\n".join(str(row) for row in data[-3:])
    metrics_text = "\n".join(f"  {k}: {v}" for k, v in metrics.items())

    extra_context = ""
    if indicators:
        extra_context += f"\n\nTechnical Indicators:\n{json.dumps(indicators, indent=2)}"
    if risk:
        extra_context += f"\n\nRisk Assessment:\n{json.dumps(risk, indent=2)}"

    system_prompt = (
        "You are a senior financial analyst. Write a professional stock analysis "
        "report based on the provided metrics and data. Include trend identification, "
        "technical analysis narrative, support/resistance levels, risk assessment, "
        "and a forward outlook. Format with markdown. Be data-driven and cite specific numbers."
    )

    messages = [{"role": "user", "content": (
        f"Generate a stock analysis report for {ticker}.\n\n"
        f"Technical Metrics:\n{metrics_text}\n\n"
        f"Data Sample (earliest):\n{sample_start}\n\n"
        f"Data Sample (latest):\n{sample_end}"
        f"{extra_context}\n\n"
        "Write a comprehensive analysis report covering:\n"
        "1. Executive Summary\n"
        "2. Price Action Analysis\n"
        "3. Technical Indicators\n"
        "4. Risk Assessment\n"
        "5. Outlook & Key Levels to Watch"
    )}]

    return chat(messages, system_prompt=system_prompt, temperature=0.4, max_tokens=4000)
