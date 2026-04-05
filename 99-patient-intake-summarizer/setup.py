from setuptools import setup, find_packages

setup(
    name="patient-intake-summarizer",
    version="1.0.0",
    description="AI-powered patient intake form summarization (HIPAA-friendly, 100% local)",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "requests",
        "rich",
        "click",
        "pyyaml",
        "streamlit",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"],
    },
    entry_points={
        "console_scripts": [
            "patient-intake-summarizer=patient_intake_summarizer.cli:cli",
        ],
    },
)
