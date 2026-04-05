# Changelog

All notable changes to Court Filing Generator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2025-07-03

### Added
- Initial release of Court Filing Generator
- Core filing generation engine with 10 filing types
- Motion generation (dismiss, summary judgment, compel, in limine)
- Discovery request generation (interrogatories, RFP, RFA)
- Filing validation and completeness checking
- Standard court document header formatting
- CLI interface with Rich-formatted output
- Streamlit web UI with dark theme and gold accents
- FastAPI REST API with full CRUD endpoints
- Filing templates for all 10 document types
- 100% local processing with Gemma 4 via Ollama
- Docker and Docker Compose support
- Comprehensive test suite
- CI/CD pipeline with GitHub Actions

### Security
- All processing occurs locally — no data leaves the machine
- Designed for attorney-client privilege preservation
- No external API calls or telemetry
