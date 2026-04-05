# 🔬 Medical Literature Summarizer

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Gemma%204-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow)

Production-grade medical literature analyzer with PICO framework extraction, evidence quality rating, citation formatting, and structured paper summarization.

## ✨ Features

- **Structured Extraction** — Title/authors, abstract, methodology, findings, statistics, conclusions, limitations, future work
- **PICO Framework** — Population, Intervention, Comparison, Outcome extraction
- **Evidence Quality Rating** — Study design, sample size, methodology rigor, bias risk assessment
- **Citation Formatter** — APA, MLA, Chicago, Vancouver citation styles
- **Adjustable Detail** — Brief, standard, or comprehensive summaries
- **Dual Interface** — CLI + Streamlit Web UI
- **Local & Private** — All processing via local Ollama

## 🚀 Installation

```bash
cd 14-medical-lit-summarizer
pip install -r requirements.txt
ollama serve && ollama pull gemma4
```

## 📋 CLI Usage

```bash
# Summarize a paper
python -m src.medical_summarizer.cli summarize --paper research.txt --detail standard

# PICO framework extraction
python -m src.medical_summarizer.cli pico --paper research.txt

# Evidence quality rating
python -m src.medical_summarizer.cli evidence --paper research.txt

# Format citation
python -m src.medical_summarizer.cli cite --paper research.txt --style APA
```

## 🌐 Web UI (Streamlit)

```bash
streamlit run src/medical_summarizer/web_ui.py
```

Features: Paper upload, structured summary, evidence table, PICO extraction, formatted citations.

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
```

## 📁 Project Structure

```
14-medical-lit-summarizer/
├── src/medical_summarizer/
│   ├── __init__.py, core.py, cli.py, web_ui.py, config.py, utils.py
├── tests/
│   ├── __init__.py, test_core.py, test_cli.py
├── config.yaml, setup.py, requirements.txt, Makefile, .env.example, README.md
```

## Part of

[90 Local LLM Projects](../README.md) — A collection of projects powered by local language models.
