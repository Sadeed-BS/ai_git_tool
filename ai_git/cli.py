import argparse
import sys
import subprocess
from ai_git.core.git_ops import clone_repo, analyze_repo, ai_commit
from ai_git.utils.github_api import create_issue, create_pull_request
from ai_git.commands import natural, commit, pr, issue, analyze, clone  # or other commands you have


import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="ai-git",
        description="🧠 AI-powered Git CLI using Gemini"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Attach all subcommands
    natural.add_subparser(subparsers)
    commit.add_subparser(subparsers)
    pr.add_subparser(subparsers)
    issue.add_subparser(subparsers)
    analyze.add_subparser(subparsers)
    clone.add_subparser(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
