import subprocess
from tools import TOOLS

def run_tool(tool_name: str, args: dict = None):

    if tool_name not in TOOLS:
        return f"BLOCKED: tool '{tool_name}' not allowed"

    command = TOOLS[tool_name]

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=5
        )

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "ERROR: timeout"