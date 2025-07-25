# ai_git/commands/natural.py

import subprocess
from ai_git.utils.ai_utils import interpret_command
import argparse

def suggest_undo(command):
    # Heuristic undo logic
    command = command.strip()
    if "git checkout -b" in command:
        branch = command.split()[-1]
        return f"git branch -d {branch}"
    elif command == "git add .":
        return "git reset"
    elif "git commit" in command:
        return "git reset --soft HEAD~1"
    elif "git push" in command:
        return "git push --force"
    return "⚠️ Undo not available for this command."

def run(args):
    prompt = " ".join(args.prompt)
    print(f"[🧠 Interpreting]: {prompt}")

    try:
        shell_command = interpret_command(prompt)
        if not shell_command:
            print("[⚠️] Couldn't understand the command.")
            return

        print(f"[🤖 AI Suggestion]: {shell_command}")

        if args.preview:
            print("🔍 Preview mode: Command not executed.")
            return

        if args.undo:
            undo_cmd = suggest_undo(shell_command)
            print(f"↩️ Suggested undo: {undo_cmd}")
            return

        if not args.yes:
            confirm = input("❓ Do you want to run this command? [y/N]: ").strip().lower()
            if confirm != 'y':
                print("❌ Command cancelled by user.")
                return

        print(f"[🚀 Running]: {shell_command}")
        result = subprocess.run(shell_command, shell=True, text=True)

        if result.returncode == 0:
            print("✅ Command executed successfully.")
        else:
            print(f"❌ Command failed with exit code {result.returncode}.")

    except Exception as e:
        print(f"[❌ Error] {e}")


def add_subparser(subparsers):
    parser = subparsers.add_parser(
        "natural",
        help="Use natural language to run a git command (powered by Gemini)"
    )
    parser.add_argument("prompt", nargs="+", help="Natural language instruction")
    parser.add_argument("--yes", action="store_true", help="Run without confirmation")
    parser.add_argument("--preview", action="store_true", help="Only show the command, do not execute")
    parser.add_argument("--undo", action="store_true", help="Suggest undo for the interpreted command")
    parser.set_defaults(func=run)
