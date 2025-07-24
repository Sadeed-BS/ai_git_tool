from setuptools import setup, find_packages

setup(
    name="ai-git-cli",
    version="0.1.0",
    description="AI-powered Git CLI using Gemini",
    author="Sadeed Bin Sadik",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "google-generativeai",
        "python-dotenv",
        "requests",
        "gitpython"
    ],
    entry_points={
        "console_scripts": [
            "ai-git=ai_git.__main__:main"
        ]
    },
    python_requires=">=3.8",
)
