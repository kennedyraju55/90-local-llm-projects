# Contributing to 90 Local LLM Projects

Thank you for your interest in contributing! This project is about building privacy-first AI tools using local LLMs.

## How to Contribute

### Reporting Bugs
- Open an issue using the **Bug Report** template
- Include your OS, Python version, and Ollama version
- Provide steps to reproduce the issue

### Suggesting New Projects
- Open an issue using the **Feature Request** template
- Describe the use case and which industry sector it fits
- Explain why a local LLM is a good fit for this tool

### Submitting Code
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Follow the existing project structure and coding style
4. Include tests (aim for the existing test coverage standard)
5. Ensure Docker compatibility
6. Submit a pull request

### Code Style
- Python 3.10+
- Use type hints
- Follow PEP 8
- Include docstrings for public functions
- Use `pytest` for testing

### Project Structure
Each project follows this standard structure:
```
project-name/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation & SVGs
├── Dockerfile     # Docker configuration
├── requirements.txt
└── README.md
```

### Running Tests
```bash
cd project-name
pip install -r requirements.txt
pytest tests/ -v
```

## Code of Conduct

Be respectful, constructive, and welcoming. We're all here to build useful tools that respect user privacy.

## Questions?

Open a discussion or issue — happy to help!
