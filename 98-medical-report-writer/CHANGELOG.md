# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2025-07-18

### Added
- 🚀 Initial release
- Core report generation with Gemma 4 LLM integration
- 6 report types: discharge summary, referral letter, consultation note, operative report, progress note, transfer summary
- CLI interface with Click + Rich
- Streamlit web UI with professional dark theme
- FastAPI REST API with Swagger docs
- Report formatting (standard, compact, detailed)
- Key findings extraction
- Session-based report tracking
- Docker support with docker-compose
- GitHub Actions CI/CD pipeline
- Comprehensive test suite with pytest
- 100% local processing — HIPAA-friendly

### Infrastructure
- Multi-stage Dockerfile
- Docker Compose with Ollama sidecar and API service
- GitHub Actions CI (Python 3.10/3.11/3.12)
- Automated linting with flake8
