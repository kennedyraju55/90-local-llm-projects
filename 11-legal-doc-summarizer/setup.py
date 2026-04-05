"""Setup script for Legal Document Summarizer."""

from setuptools import setup, find_packages

setup(
    name="legal-summarizer",
    version="1.0.0",
    description="Production-grade legal document summarizer using local LLM",
    author="Legal Summarizer Team",
    python_requires=">=3.11",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests",
        "rich",
        "click",
        "PyPDF2",
        "pyyaml",
        "streamlit",
        "python-dotenv",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"],
    },
    entry_points={
        "console_scripts": [
            "legal-summarizer=legal_summarizer.cli:main",
        ],
    },
)
