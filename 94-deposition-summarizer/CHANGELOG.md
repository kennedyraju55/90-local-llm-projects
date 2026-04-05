# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2025-07-17

### Added
- 🚀 Initial release
- Core deposition analysis with Gemma 4 LLM integration
- Key admission extraction
- Contradiction detection
- Important testimony extraction by topic
- Follow-up question generation
- Chronological timeline construction
- Witness profile analysis
- CLI interface with Click + Rich
- Streamlit web UI with dark theme and legal gold accents
- FastAPI REST API with Swagger docs
- Docker support with docker-compose (app, API, Ollama)
- GitHub Actions CI/CD pipeline
- Comprehensive test suite with pytest (20+ tests)
- Sample deposition transcript for testing
- Production-ready project structure

### Infrastructure
- Multi-stage Dockerfile
- Docker Compose with Ollama sidecar
- GitHub Actions CI (Python 3.10/3.11/3.12)
- Automated linting with flake8

### Privacy & Security
- 100% local processing — zero data leakage
- Attorney-client privilege protected
- No external API calls for analysis
- All LLM inference via local Ollama
