"""Core business logic for Medical Literature Summarizer."""

import logging
from typing import Any

from .config import load_config
from .utils import get_llm_client

logger = logging.getLogger(__name__)

SECTIONS = [
    ("title_authors", "Title & Authors", "Extract the paper title and list of authors. Format as:\nTitle: <title>\nAuthors: <authors>"),
    ("abstract_summary", "Abstract Summary", "Summarize the abstract of this paper in a clear paragraph."),
    ("methodology", "Methodology", "Describe the research methodology including study design, participants/samples, procedures, and tools used."),
    ("key_findings", "Key Findings", "List the key findings and results of this research."),
    ("statistical_results", "Statistical Results", "Extract and summarize any statistical results, p-values, confidence intervals, effect sizes, or quantitative outcomes."),
    ("conclusions", "Conclusions", "Summarize the main conclusions drawn by the authors."),
    ("limitations", "Limitations", "Identify the limitations of the study as noted by the authors or apparent from the methodology."),
    ("future_work", "Future Work", "Describe any future research directions or recommendations suggested by the authors."),
]

PICO_PROMPT = """Analyze this medical paper using the PICO framework:
- **P** (Population): Who were the participants/patients?
- **I** (Intervention): What intervention or exposure was studied?
- **C** (Comparison): What was the comparison/control group?
- **O** (Outcome): What were the measured outcomes?

For each element, provide specific details from the paper.

Paper:
{paper_text}"""

EVIDENCE_QUALITY_PROMPT = """Rate the quality of evidence in this medical paper. Assess:

1. **Study Design** (RCT, cohort, case-control, etc.) - Rate 1-5
2. **Sample Size** - Is it adequate? Rate 1-5
3. **Methodology Rigor** - Blinding, randomization, controls - Rate 1-5
4. **Statistical Analysis** - Appropriate methods, significance - Rate 1-5
5. **Bias Risk** - Selection, reporting, measurement bias - Rate 1-5
6. **Overall Evidence Level** - Rate using Oxford CEBM levels (1a-5)

Provide justification for each rating.

Paper:
{paper_text}"""

CITATION_PROMPTS = {
    "APA": "Format a citation for this paper in APA 7th edition style.",
    "MLA": "Format a citation for this paper in MLA 9th edition style.",
    "Chicago": "Format a citation for this paper in Chicago Manual of Style format.",
    "Vancouver": "Format a citation for this paper in Vancouver style.",
}


def extract_section(paper_text: str, section_key: str, section_prompt: str,
                    detail_level: str, config: dict | None = None) -> str:
    """Extract a specific section from a paper using the LLM."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    detail_instruction = cfg.get("detail_levels", {}).get(detail_level, cfg["detail_levels"]["standard"])
    system_prompt = (
        "You are an expert medical and scientific literature analyst. "
        "You carefully read research papers and extract structured information. "
        "Be accurate and faithful to the source material. "
        f"{detail_instruction}"
    )

    messages = [
        {
            "role": "user",
            "content": (
                f"Analyze the following medical/scientific paper and {section_prompt}\n\n"
                f"--- PAPER START ---\n{paper_text}\n--- PAPER END ---"
            ),
        }
    ]

    return chat(messages, system_prompt=system_prompt,
                temperature=cfg["llm"]["temperature"],
                max_tokens=cfg["llm"]["max_tokens"])


def summarize_paper(paper_text: str, detail_level: str = "standard",
                    config: dict | None = None) -> dict:
    """Summarize a medical paper into structured sections."""
    cfg = config or load_config()
    results = {}

    for section_key, section_title, section_prompt in SECTIONS:
        logger.info("Extracting %s...", section_title)
        try:
            results[section_key] = extract_section(
                paper_text, section_key, section_prompt, detail_level, cfg
            )
        except Exception as e:
            results[section_key] = f"[Error extracting section: {e}]"

    return results


def extract_pico(paper_text: str, config: dict | None = None) -> str:
    """Extract PICO framework elements from a medical paper."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    system_prompt = (
        "You are an expert in evidence-based medicine. "
        "Extract PICO framework elements accurately from research papers."
    )

    messages = [{"role": "user", "content": PICO_PROMPT.format(paper_text=paper_text)}]
    return chat(messages, system_prompt=system_prompt,
                temperature=cfg["llm"]["temperature"],
                max_tokens=cfg["llm"]["max_tokens"])


def rate_evidence_quality(paper_text: str, config: dict | None = None) -> str:
    """Rate the quality of evidence in a medical paper."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    system_prompt = (
        "You are an expert in research methodology and evidence-based medicine. "
        "Provide rigorous, objective quality assessments."
    )

    messages = [{"role": "user", "content": EVIDENCE_QUALITY_PROMPT.format(paper_text=paper_text)}]
    return chat(messages, system_prompt=system_prompt,
                temperature=cfg["llm"]["temperature"],
                max_tokens=cfg["llm"]["max_tokens"])


def format_citation(paper_text: str, style: str = "APA",
                    config: dict | None = None) -> str:
    """Format a citation for the paper in the specified style."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    prompt = CITATION_PROMPTS.get(style, CITATION_PROMPTS["APA"])
    messages = [
        {
            "role": "user",
            "content": f"{prompt}\n\nPaper:\n{paper_text[:3000]}",
        }
    ]

    return chat(messages,
                system_prompt="You are a librarian expert in academic citation formatting.",
                temperature=0.1, max_tokens=512)
