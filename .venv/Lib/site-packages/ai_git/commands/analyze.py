# ai_git/commands/analyze.py

from ai_git.core.git_ops import analyze_repo

def run(args):
    print(f"📊 Analyzing repository at {args.path}")
    analyze_repo(args.path)

def add_subparser(subparsers):
    parser = subparsers.add_parser(
        "analyze", help="Analyze a git repository"
    )
    parser.add_argument("path", help="Path to the git repository")
    parser.set_defaults(func=run)
