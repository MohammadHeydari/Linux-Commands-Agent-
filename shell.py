import subprocess

ALLOWED_COMMANDS = [
    "date",
    "uname",
    "ip addr show",
    "whoami",
    "ls"
]

def is_allowed(command: str) -> bool:
    return any(command.startswith(cmd) for cmd in ALLOWED_COMMANDS)

def run_command(command: str):
    command = command.strip()

    if not is_allowed(command):
        return f"BLOCKED: '{command}' is not allowed"

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=5
        )

        return result.stdout + result.stderr

    except subprocess.TimeoutExpired:
        return "ERROR: command timeout"