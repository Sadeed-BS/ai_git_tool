from setuptools import setup, find_packages

setup(
    name='ai-git-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        r.strip() for r in open('requirements.txt').readlines() if r.strip()
    ],
    entry_points={
        'console_scripts': [
            'ai-git=ai_git.cli:main',  # `main()` in cli.py
        ],
    },
    author='Sadeed Bin Sadik',
    description='AI-powered Git CLI using LangGraph and GitHub API',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sadeed-BS/ai_git_tool',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.7',
)
