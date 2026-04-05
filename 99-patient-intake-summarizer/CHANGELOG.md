# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-04-05

### Added
- 🚀 Initial release
- Core intake form summarization with Gemma 4 LLM integration
- Medical history extraction into 9 standardized categories
- Risk factor identification from intake text
- Missing information flagging
- Pre-visit summary generation for physicians
- CLI interface with Click + Rich (5 commands)
- Streamlit web UI with professional dark theme
- FastAPI REST API with Swagger docs
- Docker support with docker-compose
- GitHub Actions CI/CD pipeline
- Comprehensive test suite with pytest (15+ tests)
- 100% local processing — HIPAA-friendly

### Infrastructure
- Multi-stage Dockerfile
- Docker Compose with Ollama sidecar
- GitHub Actions CI (Python 3.10/3.11/3.12)
- Automated linting with flake8
