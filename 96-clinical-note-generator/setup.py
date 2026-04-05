from setuptools import setup, find_packages

setup(
    name="clinical-note-generator",
    version="1.0.0",
    description="AI-powered SOAP note generation from patient encounters - 100% local, HIPAA-friendly",
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
            "clinical-note-generator=clinical_note_generator.cli:cli",
        ],
    },
)
