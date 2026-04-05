"""Setup script for Medical Literature Summarizer."""

from setuptools import setup, find_packages

setup(
    name="medical-summarizer",
    version="1.0.0",
    description="Production-grade medical literature summarizer using local LLM",
    python_requires=">=3.11",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests", "rich", "click", "pyyaml", "streamlit", "python-dotenv",
    ],
    extras_require={"dev": ["pytest", "pytest-cov"]},
    entry_points={"console_scripts": ["medical-summarizer=medical_summarizer.cli:main"]},
)
