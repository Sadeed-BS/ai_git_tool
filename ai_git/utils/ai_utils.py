# ai_git/utils/ai_utils.py

import google.generativeai as genai
import textwrap
from dotenv import load_dotenv
import os
from pathlib import Path

# Always load .env from project root, no matter where the CLI is run
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

import google.generativeai as genai

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set in environment!")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-pro")


def interpret_command(prompt: str) -> str:
    """
    Convert natural language prompt to a one-line Git bash command.
    """
    try:
        system_prompt = textwrap.dedent(
            "You are a shell expert. Translate the following request "
            "into a one-line Git bash command ONLY. No explanations or comments."
        )
        response = model.generate_content(system_prompt + "\n" + prompt)
        return response.text.strip().split("\n")[0].strip("`").strip()
    except Exception as e:
        print(f"❌ Error using Gemini for interpret_command: {e}")
        return "echo 'Failed to interpret command'"


def generate_commit_message(changes: str) -> str:
    """
    Generate a short, meaningful git commit message from code changes.
    """
    try:
        system_prompt = textwrap.dedent(
            "You're an assistant writing concise git commit messages. "
            "Based on the following code changes, return a one-line commit message:"
        )
        response = model.generate_content(system_prompt + "\n\n" + changes)
        return response.text.strip().split("\n")[0].strip("`").strip()
    except Exception as e:
        print(f"❌ Error using Gemini for commit message: {e}")
        return "update code"


def generate_pr_message(changes: str, title: str = "Pull Request") -> tuple[str, str]:
    """
    Generate a title and detailed PR description based on the code diff.
    """
    try:
        system_prompt = textwrap.dedent(
            f"You are a GitHub assistant. Generate a short PR title and a detailed PR description.\n"
            f"Changes:\n{changes}\n\n"
            "Respond in this format:\n"
            "Title: <title>\n\nDescription:\n<markdown description>"
        )
        response = model.generate_content(system_prompt)
        lines = response.text.strip().splitlines()

        pr_title = next((line.replace("Title:", "").strip() for line in lines if line.lower().startswith("title:")), title)
        description_index = next((i for i, line in enumerate(lines) if line.lower().startswith("description")), -1)
        pr_description = "\n".join(lines[description_index + 1:]).strip() if description_index != -1 else "Auto-generated PR"

        return pr_title, pr_description
    except Exception as e:
        print(f"❌ Error using Gemini for PR message: {e}")
        return title, "Auto-generated pull request description."
