# 📄 Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Gemma%204-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow)

Production-grade resume analysis tool with ATS score simulation, keyword gap analysis, multi-resume comparison, and actionable improvement suggestions — all powered by a local LLM via Ollama.

## ✨ Features

- **General Analysis** — Skills, experience, education, strengths, weaknesses, overall scoring
- **JD Scoring** — Match percentage with skill gap analysis and keyword gaps
- **ATS Simulation** — Applicant Tracking System compatibility scoring
- **Multi-Resume Comparison** — Compare multiple candidates side by side
- **Improvement Suggestions** — Section-by-section actionable feedback with power words
- **Dual Interface** — CLI for power users, Streamlit Web UI for visual analysis
- **Local & Private** — All processing runs locally via Ollama

## 🚀 Installation

```bash
cd 12-resume-analyzer
pip install -r requirements.txt
ollama serve && ollama pull gemma4
```

## 📋 CLI Usage

```bash
# General analysis
python -m src.resume_analyzer.cli analyze --resume resume.txt

# Score against job description
python -m src.resume_analyzer.cli score --resume resume.txt --jd job.txt

# ATS score simulation
python -m src.resume_analyzer.cli ats --resume resume.txt --jd job.txt

# Improvement suggestions
python -m src.resume_analyzer.cli improve --resume resume.txt
```

## 🌐 Web UI (Streamlit)

```bash
streamlit run src/resume_analyzer/web_ui.py
```

Features: Resume upload, job description input, score dashboard, suggestions panel, multi-resume comparison.

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
```

## 📁 Project Structure

```
12-resume-analyzer/
├── src/resume_analyzer/
│   ├── __init__.py, core.py, cli.py, web_ui.py, config.py, utils.py
├── tests/
│   ├── __init__.py, test_core.py, test_cli.py
├── config.yaml, setup.py, requirements.txt, Makefile, .env.example, README.md
```

## Part of

[90 Local LLM Projects](../README.md) — A collection of projects powered by local language models.
