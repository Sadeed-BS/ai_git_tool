import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def generate_pr_message(diff_text):
    from google.generativeai import GenerativeModel
    model = GenerativeModel("gemini-pro")
    prompt = f"""You are an expert developer.

Here's the git diff between two branches:

{diff_text}

Generate a PR title and detailed description.
Format:
Title: <title>
Description:
<bullet-point summary of changes>"""

    try:
        response = model.generate_content(prompt)
        output = response.text.strip()

        if "Title:" in output:
            parts = output.split("Title:", 1)[1].strip().split("Description:")
            title = parts[0].strip()
            description = parts[1].strip() if len(parts) > 1 else ""
        else:
            title, description = "Auto-generated PR", output
        return title, description
    except Exception as e:
        print(f"[Gemini PR Gen Error] {e}")
        return "Auto-generated PR", ""


def generate_commit_message(diff_text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""You are an assistant that writes concise, clear, and useful Git commit messages.
Here is a git diff of the staged changes:

{diff_text}

Write a commit message (no explanations, just the message):"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Error] {e}")
        return "chore: commit message (fallback)"
