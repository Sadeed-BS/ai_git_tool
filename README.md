
# 🧠 ai-git-cli

**ai-git-cli** is an AI-powered command-line tool that supercharges your Git workflow. It provides AI-generated commit messages, natural language Git commands, codebase analysis, and GitHub integration—all from your terminal. It also supports all standard Git commands, acting as a drop-in replacement for `git`.


## ✨ Features

- 🔥 **AI-powered commit messages** — Generate concise, meaningful messages using **Gemini**.
- 💬 **Natural language Git** — Describe your intent in plain English and execute the corresponding Git command.
- 🧠 **Codebase analysis** — Analyze code with LangGraph-compatible tools (future support).
- 🐙 **GitHub integration** — Create issues and pull requests from your terminal with optional AI-generated titles and descriptions.
- 🧰 **Full Git support** — Use any standard Git command via `ai-git <command>`.
- 🪄 **Drop-in usability** — Seamless experience as an enhanced `git` wrapper.


## ⚙️ Installation

Install my-project with npm

```bash
git clone https://github.com/Sadeed-BS/ai_git_tool.git
cd ai_git_tool
pip install . 
```
    
## 🚀 Usage/Examples

Use ai-git just like git:

```
ai-git status
ai-git log
ai-git checkout main
```

## 🤖 AI-powered Features

```
ai-git commit --repo .
ai-git analyze <path>
ai-git issue <repo> <title> <body>
ai-git pr <repo> <head-branch> <base-branch> --ai
ai-git natural "create a new branch called feature-x"
```


## 🔐 Configuration

Create a .env file in your project root and store your API keys:

```
GEMINI_API_KEY=your-gemini-api-key
GITHUB_TOKEN=your-github-token
```
## 🧱 Project Structure

```
ai_git_tool/
├── cli.py                # CLI entry point
├── main.py               # Command routing
├── commands/             # Git logic and wrappers
│   └── git_commands.py
├── core/                 # Gemini interpreter logic
│   └── interpreter.py
├── requirements.txt
├── setup.py
└── .env.example
```
## ✅ Requirements

- Python 3.8+

- Git installed and available in your system PATH

- Gemini API Key from Google

- (Optional) GitHub token for PR/issue automation
## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repo, open issues, and submit pull requests for new features or improvements.


## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)


## 👤 Author

- Developed by [Sadeed Bin Sadik](https://www.github.com/Sadeed-BS)