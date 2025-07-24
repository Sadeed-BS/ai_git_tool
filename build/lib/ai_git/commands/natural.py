# ai_git/commands/natural.py

import subprocess
from ai_git.utils.ai_utils import interpret_command

def run(args):
    prompt = " ".join(args.prompt)
    print(f"[🧠 Interpreting]: {prompt}")
    
    shell_command = interpret_command(prompt)
    
    if shell_command:
        print(f"[✅ Running]: {shell_command}")
        subprocess.run(shell_command, shell=True)
    else:
        print("[⚠️] Couldn't understand the command.")
