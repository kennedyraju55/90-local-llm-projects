from setuptools import setup, find_packages

setup(
    name="differential-diagnosis-assistant",
    version="1.0.0",
    description="AI-powered differential diagnosis assistant for educational purposes",
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
            "differential-diagnosis=differential_diagnosis.cli:cli",
        ],
    },
)
