# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2025-07-15

### Added
- 🚀 Initial release
- SOAP note generation from encounter descriptions
- Support for 6 note types (general, follow-up, urgent, pediatric, psychiatric, surgical)
- 6 medical specialty modes
- Individual section generation (S, O, A, P)
- Note refinement with physician feedback
- Diagnosis extraction from notes
- CLI interface with Click + Rich
- Streamlit web UI with professional dark theme
- FastAPI REST API with Swagger docs
- Docker support with docker-compose
- GitHub Actions CI/CD pipeline
- Comprehensive test suite with pytest

### Infrastructure
- Multi-stage Dockerfile
- Docker Compose with Ollama sidecar
- GitHub Actions CI (Python 3.10/3.11/3.12)
- Automated linting with flake8
