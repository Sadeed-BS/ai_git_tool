# ai_git/__main__.py

import argparse
from ai_git.commands import (
    natural, commit, pr, issue, clone, analyze
)

def main():
    parser = argparse.ArgumentParser(prog="ai-git", description="AI-powered Git CLI Tool")
    subparsers = parser.add_subparsers(title="Commands", dest="command")

    # Register subcommands
    natural.add_subparser(subparsers)
    commit.add_subparser(subparsers)
    pr.add_subparser(subparsers)
    issue.add_subparser(subparsers)
    clone.add_subparser(subparsers)
    analyze.add_subparser(subparsers)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
