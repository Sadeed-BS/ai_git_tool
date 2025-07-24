# ai-git-cli

**ai-git-cli** is an AI-powered command-line tool that enhances your Git workflow with features like AI-generated commit messages, codebase analysis, and seamless GitHub integration. It also supports all standard Git commands.

## Features

- **AI-powered commit messages**: Generate meaningful commit messages using Gemini.
- **Codebase analysis**: Analyze your repository with LangGraph-compatible tools.
- **GitHub integration**: Create issues and pull requests directly from the CLI.
- **Full Git support**: Use any standard Git command via `ai-git <command>`.
- **Easy to use**: Drop-in replacement for the `git` command.

## Installation

```bash
pip install .
```

## Usage

All standard Git commands are supported:

```bash
ai-git status
ai-git log
ai-git checkout main
```

AI-powered features:

```bash
ai-git commit --repo .
ai-git analyze <path>
ai-git issue <repo> <title> <body>
ai-git pr --repo <user/repo> --branch <feature-branch> --base main --ai
```

## Requirements

- Python 3.7+
- Git installed and available in your PATH

## License

MIT

## Author

[Sadeed Bin Sadik](https://github.com/Sadeed-BS)