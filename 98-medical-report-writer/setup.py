from setuptools import setup, find_packages

setup(
    name="medical-report-writer",
    version="1.0.0",
    description="AI-powered clinical report generation using local LLMs",
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
            "medical-report-writer=medical_report_writer.cli:cli",
        ],
    },
)
