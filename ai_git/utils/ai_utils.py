import google.generativeai as genai
import os

# Load Gemini API key from environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def interpret_command(prompt: str) -> str:
    system_prompt = "You are a shell expert. Translate the request into only one line git bash command."
    response = model.generate_content(system_prompt + "\n" + prompt)
    return response.text.strip().split("\n")[0]

def generate_commit_message(changes: str) -> str:
    """
    Generate a commit message using Gemini based on given code/diff.
    """
    system_prompt = (
        "You're an assistant writing git commit messages. "
        "Based on the following code changes, return a meaningful commit message."
    )
    response = model.generate_content(system_prompt + "\n\n" + changes)
    return response.text.strip().split("\n")[0]

def generate_pr_message(title: str, changes: str) -> str:
    """
    Generate a pull request description based on title and changes.
    """
    system_prompt = (
        f"You are writing a detailed GitHub pull request description.\n"
        f"Title: {title}\n"
        f"Changes:\n{changes}\n\n"
        "Write a professional and detailed PR description in markdown."
    )
    response = model.generate_content(system_prompt)
    return response.text.strip()
