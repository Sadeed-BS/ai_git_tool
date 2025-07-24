# ai_git/commands/commit.py

import argparse
from ai_git.core.git_ops import ai_commit

def run(args):
    print(f"🔍 Running AI-generated commit in: {args.repo}")
    ai_commit(args.repo)

def add_subparser(subparsers):
    parser = subparsers.add_parser(
        "commit", help="Commit staged changes with AI-generated message"
    )
    parser.add_argument(
        "--repo", default=".", help="Path to the git repository (default: current directory)"
    )
    parser.set_defaults(func=run)
