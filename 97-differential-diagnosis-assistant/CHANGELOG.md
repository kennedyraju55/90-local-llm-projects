# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-04-05

### Added
- 🚀 Initial release
- Core differential diagnosis engine with Gemma 4 LLM integration
- Ranked differential generation from symptoms, patient info, and exam findings
- Workup recommendation engine
- Diagnosis comparison tool
- CLI interface with Click + Rich (diagnose, workup, compare, chat commands)
- Streamlit web UI with professional dark theme and tabbed interface
- FastAPI REST API with Swagger docs
- Docker support with docker-compose
- GitHub Actions CI/CD pipeline
- Comprehensive test suite with pytest (15+ tests)
- 100% HIPAA-friendly — no patient data leaves the machine
- Production-ready project structure

### Infrastructure
- Multi-stage Dockerfile
- Docker Compose with Ollama sidecar
- GitHub Actions CI (Python 3.10/3.11/3.12)
- Automated linting with flake8
