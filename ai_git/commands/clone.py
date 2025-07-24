# ai_git/commands/clone.py

from ai_git.core.git_ops import clone_repo

def run(args):
    clone_repo(args.url)

def add_subparser(subparsers):
    parser = subparsers.add_parser(
        "clone", help="Clone a git repository"
    )
    parser.add_argument("url", help="Git repository URL")
    parser.set_defaults(func=run)
