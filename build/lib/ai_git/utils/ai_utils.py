import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

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
