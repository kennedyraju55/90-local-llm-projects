"""Core business logic for the Report Generator."""

from typing import Optional, List, Dict, Any, Tuple, Union
import csv
import os
import statistics
import logging
from collections import Counter
from datetime import datetime

from .utils import setup_sys_path

setup_sys_path()
from common.llm_client import chat, check_ollama_running

logger = logging.getLogger(__name__)

REPORT_TEMPLATES = {
    "executive": (
        "Generate a comprehensive executive report on the topic: **{topic}**\n\n"
        "Here is the data summary:\n```\n{data_summary}\n```\n\n"
        "Structure the report with these sections:\n"
        "1. **Executive Summary** - Brief overview of findings (2-3 paragraphs)\n"
        "2. **Key Findings** - Top insights from the data (use bullet points)\n"
        "3. **Data Analysis** - Detailed breakdown with specific numbers\n"
        "4. **Chart Descriptions** - Describe 2-3 charts that would visualize the data\n"
        "5. **Recommendations** - Actionable next steps based on the data\n"
        "6. **Conclusion** - Final summary\n\n"
        "Use markdown formatting: headers, bold, bullet points, and tables where appropriate. "
        "Reference actual numbers from the data summary."
    ),
    "technical": (
        "Generate a detailed technical analysis report on: **{topic}**\n\n"
        "Data:\n```\n{data_summary}\n```\n\n"
        "Structure:\n"
        "1. **Overview** - Technical summary\n"
        "2. **Methodology** - How the data was analyzed\n"
        "3. **Statistical Analysis** - Detailed statistics and distributions\n"
        "4. **Chart Descriptions** - Statistical visualizations to create\n"
        "5. **Findings** - Technical observations\n"
        "6. **Technical Recommendations** - Data-driven suggestions\n"
    ),
    "summary": (
        "Generate a brief summary report on: **{topic}**\n\n"
        "Data:\n```\n{data_summary}\n```\n\n"
        "Keep it concise with:\n"
        "1. **Summary** - 3-5 sentence overview\n"
        "2. **Key Metrics** - Top 5 numbers\n"
        "3. **Action Items** - 3 quick recommendations\n"
    ),
}


def read_csv_data(filepath: str) -> tuple[list[str], list[dict]]:
    """Read CSV file and return headers and rows.

    Args:
        filepath: Path to the CSV file.

    Returns:
        Tuple of (column_names, list_of_row_dicts).

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the CSV file is empty or malformed.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")

    with open(filepath, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV file is empty or has no header row.")
        headers = list(reader.fieldnames)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV file contains headers but no data rows.")

    logger.info("Read %d rows with %d columns from %s", len(rows), len(headers), filepath)
    return headers, rows


def summarize_data(headers: list[str], rows: list[dict]) -> str:
    """Build a statistical summary of the CSV data for LLM context.

    Args:
        headers: Column names from the CSV.
        rows: List of row dictionaries.

    Returns:
        A formatted string summarizing the dataset.
    """
    summary_parts = [
        "Dataset Overview:",
        f"  - Total rows: {len(rows)}",
        f"  - Columns ({len(headers)}): {', '.join(headers)}",
        "",
    ]

    for col in headers:
        values = [row.get(col, "").strip() for row in rows if row.get(col, "").strip()]
        if not values:
            summary_parts.append(f"  [{col}]: all empty")
            continue

        numeric_vals = []
        for v in values:
            try:
                numeric_vals.append(float(v.replace(",", "")))
            except (ValueError, AttributeError):
                pass

        if numeric_vals and len(numeric_vals) >= len(values) * 0.5:
            col_min = min(numeric_vals)
            col_max = max(numeric_vals)
            col_mean = statistics.mean(numeric_vals)
            col_sum = sum(numeric_vals)
            parts = [
                f"  [{col}] (numeric, {len(numeric_vals)} values):",
                f"    min={col_min:,.2f}, max={col_max:,.2f}, "
                f"mean={col_mean:,.2f}, sum={col_sum:,.2f}",
            ]
            if len(numeric_vals) >= 2:
                col_stdev = statistics.stdev(numeric_vals)
                col_median = statistics.median(numeric_vals)
                parts.append(f"    median={col_median:,.2f}, stdev={col_stdev:,.2f}")
            summary_parts.extend(parts)
        else:
            unique = set(values)
            summary_parts.append(
                f"  [{col}] (text, {len(values)} values, {len(unique)} unique):"
            )
            if len(unique) <= 10:
                counts = Counter(values).most_common(10)
                for val, cnt in counts:
                    summary_parts.append(f"    '{val}': {cnt}")
            else:
                summary_parts.append(f"    sample: {', '.join(list(unique)[:5])} ...")

    return "\n".join(summary_parts)


def generate_report(
    topic: str,
    data_summary: str,
    template: str = "executive",
    config: dict = None,
) -> str:
    """Use the LLM to generate a structured markdown report.

    Args:
        topic: The report topic / title.
        data_summary: Statistical summary of the source data.
        template: Report template name ('executive', 'technical', 'summary').
        config: Optional configuration dictionary.

    Returns:
        Markdown-formatted report string.
    """
    config = config or {}
    llm_config = config.get("llm", {})

    system_prompt = (
        "You are an expert business analyst and report writer. "
        "Generate professional, data-driven reports in clean Markdown format. "
        "Use specific numbers from the data provided. Be concise but thorough."
    )

    template_text = REPORT_TEMPLATES.get(template, REPORT_TEMPLATES["executive"])
    user_message = template_text.format(topic=topic, data_summary=data_summary)

    messages = [{"role": "user", "content": user_message}]

    report = chat(
        messages=messages,
        system_prompt=system_prompt,
        temperature=llm_config.get("temperature", 0.5),
        max_tokens=llm_config.get("max_tokens", 4096),
    )

    logger.info("Generated report with template '%s' (%d chars)", template, len(report))
    return report


def save_report(content: str, output_path: str, topic: str, fmt: str = "markdown") -> str:
    """Save the generated report to a file with metadata header.

    Args:
        content: The markdown report body.
        output_path: Destination file path.
        topic: Report topic for the header.
        fmt: Output format ('markdown', 'html', 'text').

    Returns:
        The absolute path of the saved file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if fmt == "html":
        full_content = _to_html(content, topic, timestamp)
        if not output_path.endswith(".html"):
            output_path = output_path.rsplit(".", 1)[0] + ".html"
    elif fmt == "text":
        full_content = f"Title: {topic}\nGenerated: {timestamp}\n\n{content}"
        if not output_path.endswith(".txt"):
            output_path = output_path.rsplit(".", 1)[0] + ".txt"
    else:
        header = (
            f"---\n"
            f'title: "{topic}"\n'
            f'generated: "{timestamp}"\n'
            f'generator: "report-generator"\n'
            f"---\n\n"
        )
        full_content = header + content

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_content)

    logger.info("Report saved to %s (format: %s)", output_path, fmt)
    return os.path.abspath(output_path)


def _to_html(content: str, topic: str, timestamp: str) -> str:
    """Convert markdown content to basic HTML."""
    try:
        import markdown
        body = markdown.markdown(content, extensions=["tables", "fenced_code"])
    except ImportError:
        body = f"<pre>{content}</pre>"

    return (
        f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<title>{topic}</title>"
        f"<style>body{{font-family:sans-serif;max-width:800px;margin:auto;padding:20px}}"
        f"table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ddd;padding:8px}}</style>"
        f"</head><body>"
        f"<p><em>Generated: {timestamp}</em></p>"
        f"{body}</body></html>"
    )
