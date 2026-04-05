# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2025-07-14

### Added
- 🚀 Initial release
- Core lab results interpretation with Gemma 4 LLM integration
- Abnormality detection and highlighting
- Follow-up test recommendations
- Individual lab value explanations
- Comprehensive reference ranges (CBC, BMP, Lipid Panel, Liver Panel, Thyroid, Urinalysis)
- CLI interface with Click + Rich
- Streamlit web UI with professional dark theme
- FastAPI REST API with Swagger docs
- Lab session tracking with history
- Docker support with docker-compose
- GitHub Actions CI/CD pipeline
- Comprehensive test suite with pytest (15+ tests)
- 100% local processing — HIPAA-friendly

### Infrastructure
- Multi-stage Dockerfile
- Docker Compose with Ollama sidecar (web:8501, api:8000, ollama:11434)
- GitHub Actions CI (Python 3.10/3.11/3.12)
- Automated linting with flake8
