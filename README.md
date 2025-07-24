# ai-git-cli

**ai-git-cli** is an AI-powered command-line tool that supercharges your Git workflow. It provides AI-generated commit messages, codebase analysis, natural language Git commands, and seamless GitHub integration—all from your terminal. It also supports all standard Git commands, acting as a drop-in replacement for `git`.

---

## Features

- **AI-powered commit messages:** Generate concise, meaningful commit messages using Gemini (and easily extensible to other LLMs).
- **Natural language Git:** Describe what you want to do, and let AI translate it into the right Git command.
- **Codebase analysis:** Analyze your repository with LangGraph-compatible tools (future extensibility).
- **GitHub integration:** Create issues and pull requests directly from the CLI, with optional AI-generated PR titles/descriptions.
- **Full Git support:** Use any standard Git command via `ai-git <command>`.
- **Easy to use:** Drop-in replacement for the `git` command.

---

## Installation

```bash
pip install .
```

---

## Usage

### Standard Git Commands

You can use all standard Git commands:

```bash
ai-git status
ai-git log
ai-git checkout main
```

### AI-powered Features

```bash
ai-git commit --repo .
ai-git analyze <path>
ai-git issue <repo> <title> <body>
ai-git pr <repo> <head-branch> <base-branch> --ai
ai-git natural "create a new branch called feature-x"
```

### Choosing an LLM (Planned/Extensible)

You can extend the tool to support multiple LLMs (e.g., Gemini, OpenAI GPT). For example:

```bash
ai-git commit --repo . --model gemini
ai-git commit --repo . --model openai
```

---

## Configuration

- **API Keys:**  
  Store your `GEMINI_API_KEY` and `GITHUB_TOKEN` in a `.env` file in your project root:

  ```
  GEMINI_API_KEY=your-gemini-api-key
  GITHUB_TOKEN=your-github-token
  ```

---

## Requirements

- Python 3.8+
- Git installed and available in your PATH

---

## Contributing

Contributions are welcome! Please open issues or pull requests for new features, bug fixes, or improvements.

---

## License

MIT

---

## Author

[Sadeed Bin Sadik](https://github.com/Sadeed-BS)