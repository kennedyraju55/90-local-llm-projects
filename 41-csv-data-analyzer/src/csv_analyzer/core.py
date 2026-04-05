"""Core logic for CSV Data Analyzer."""

import os
import sys
import logging
import json
from typing import Any, Dict, List, Optional, Tuple, Union

import pandas as pd
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


def load_csv(file_path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError("CSV file is empty.")
        logger.info("Loaded CSV: %d rows x %d columns", df.shape[0], df.shape[1])
        return df
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty or malformed.")


def detect_column_types(df: pd.DataFrame) -> dict:
    """Auto-detect and categorize column types."""
    type_map = {}
    for col in df.columns:
        dtype = str(df[col].dtype)
        if "int" in dtype or "float" in dtype:
            type_map[col] = "numeric"
        elif "datetime" in dtype:
            type_map[col] = "datetime"
        elif "bool" in dtype:
            type_map[col] = "boolean"
        else:
            nunique = df[col].nunique()
            ratio = nunique / len(df) if len(df) > 0 else 0
            if ratio < 0.3 and nunique < 20:
                type_map[col] = "categorical"
            elif pd.to_datetime(df[col], errors="coerce", format="mixed").notna().mean() > 0.8:
                type_map[col] = "datetime"
            elif pd.to_numeric(df[col], errors="coerce").notna().mean() > 0.8:
                type_map[col] = "numeric"
            else:
                type_map[col] = "text"
    logger.debug("Detected column types: %s", type_map)
    return type_map


def generate_statistical_summary(df: pd.DataFrame) -> dict:
    """Generate comprehensive statistical summaries."""
    summary = {
        "shape": {"rows": df.shape[0], "columns": df.shape[1]},
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "null_counts": df.isnull().sum().to_dict(),
        "null_percentages": (df.isnull().sum() / len(df) * 100).round(2).to_dict(),
    }

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if numeric_cols:
        desc = df[numeric_cols].describe().to_dict()
        summary["numeric_stats"] = desc
        summary["skewness"] = df[numeric_cols].skew().to_dict()
        summary["kurtosis"] = df[numeric_cols].kurtosis().to_dict()

    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if categorical_cols:
        summary["categorical_stats"] = {}
        for col in categorical_cols:
            summary["categorical_stats"][col] = {
                "unique_count": int(df[col].nunique()),
                "top_values": df[col].value_counts().head(5).to_dict(),
                "mode": str(df[col].mode().iloc[0]) if not df[col].mode().empty else None,
            }

    return summary


def compute_correlations(df: pd.DataFrame) -> Optional[dict]:
    """Compute correlation matrix for numeric columns."""
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if len(numeric_cols) < 2:
        return None
    corr = df[numeric_cols].corr()
    strong_correlations = []
    for i in range(len(numeric_cols)):
        for j in range(i + 1, len(numeric_cols)):
            val = corr.iloc[i, j]
            if abs(val) > 0.5:
                strong_correlations.append({
                    "col1": numeric_cols[i],
                    "col2": numeric_cols[j],
                    "correlation": round(val, 4),
                    "strength": "strong" if abs(val) > 0.7 else "moderate",
                })
    return {
        "matrix": corr.round(4).to_dict(),
        "strong_correlations": strong_correlations,
    }


def suggest_charts(df: pd.DataFrame, column_types: dict) -> list[dict]:
    """Suggest appropriate chart types based on data characteristics."""
    suggestions = []
    numeric_cols = [c for c, t in column_types.items() if t == "numeric"]
    categorical_cols = [c for c, t in column_types.items() if t == "categorical"]
    datetime_cols = [c for c, t in column_types.items() if t == "datetime"]

    if len(numeric_cols) >= 2:
        suggestions.append({
            "type": "scatter",
            "columns": numeric_cols[:2],
            "reason": "Explore relationship between numeric variables",
        })
    if numeric_cols:
        suggestions.append({
            "type": "histogram",
            "columns": [numeric_cols[0]],
            "reason": "Understand distribution of numeric data",
        })
    if categorical_cols and numeric_cols:
        suggestions.append({
            "type": "bar",
            "columns": [categorical_cols[0], numeric_cols[0]],
            "reason": "Compare numeric values across categories",
        })
    if datetime_cols and numeric_cols:
        suggestions.append({
            "type": "line",
            "columns": [datetime_cols[0], numeric_cols[0]],
            "reason": "Show trends over time",
        })
    if categorical_cols:
        suggestions.append({
            "type": "pie",
            "columns": [categorical_cols[0]],
            "reason": "Show distribution of categorical values",
        })

    return suggestions


def generate_data_summary(df: pd.DataFrame) -> str:
    """Generate a text summary of the DataFrame for the LLM."""
    summary_parts = []
    summary_parts.append(f"Dataset shape: {df.shape[0]} rows x {df.shape[1]} columns")
    summary_parts.append(f"Columns: {', '.join(df.columns.tolist())}")
    summary_parts.append(f"\nColumn types:\n{df.dtypes.to_string()}")
    summary_parts.append(f"\nBasic statistics:\n{df.describe(include='all').to_string()}")
    summary_parts.append(f"\nFirst 5 rows:\n{df.head().to_string()}")

    null_counts = df.isnull().sum()
    if null_counts.any():
        summary_parts.append(f"\nNull values per column:\n{null_counts[null_counts > 0].to_string()}")

    column_types = detect_column_types(df)
    summary_parts.append(f"\nDetected column types: {json.dumps(column_types)}")

    correlations = compute_correlations(df)
    if correlations and correlations["strong_correlations"]:
        summary_parts.append("\nStrong correlations found:")
        for c in correlations["strong_correlations"]:
            summary_parts.append(f"  {c['col1']} <-> {c['col2']}: {c['correlation']} ({c['strength']})")

    return "\n".join(summary_parts)


def analyze_data(df: pd.DataFrame, query: str) -> str:
    """Send the data summary and query to the LLM for analysis."""
    chat, _ = get_llm_client()
    data_summary = generate_data_summary(df)

    system_prompt = (
        "You are a data analyst expert. You are given a summary of a CSV dataset "
        "and a question about the data. Analyze the data summary carefully and "
        "provide a clear, accurate, and insightful answer. Use specific numbers "
        "from the data when possible. Format your response with markdown."
    )

    user_message = (
        f"Here is the dataset summary:\n\n{data_summary}\n\n"
        f"Question: {query}\n\n"
        "Please analyze the data and answer the question thoroughly."
    )

    messages = [{"role": "user", "content": user_message}]
    return chat(messages, system_prompt=system_prompt, temperature=0.3)


def export_insights(df: pd.DataFrame, output_path: str) -> str:
    """Export comprehensive insights to a JSON file."""
    column_types = detect_column_types(df)
    stats = generate_statistical_summary(df)
    correlations = compute_correlations(df)
    charts = suggest_charts(df, column_types)

    insights = {
        "column_types": column_types,
        "statistics": stats,
        "correlations": correlations,
        "chart_suggestions": charts,
    }

    with open(output_path, "w") as f:
        json.dump(insights, f, indent=2, default=str)

    logger.info("Exported insights to %s", output_path)
    return output_path
