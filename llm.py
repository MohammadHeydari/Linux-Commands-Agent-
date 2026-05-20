import requests
import json
import re

OLLAMA_URL = "http://10.29.201.75:11434/api/chat"
MODEL = "gemma3:4b"

SYSTEM_PROMPT = """
You are a strict JSON tool router.

Return ONLY valid JSON:

{
  "tool": "tool_name",
  "args": {}
}

Available tools:
- time
- hostname
- uptime
- system
- user
- list_files
- list_sorted
- tree
- find_py
- disk
- mem
- ip
- ports
- processes
- top_cpu
- pwd

Docker tools:
- docker_ps
- docker_images
- docker_stats
- docker_version
- docker_info
- docker_all_containers

Rules:
- Only choose from allowed tools
- If unsure → {"tool":"none","args":{}}
- NEVER explain
"""

def clean_json(text):
    text = text.strip()

    # remove ```json fences
    text = re.sub(r"```json|```", "", text)

    return text.strip()

def ask_llm(user_input):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "stream": False
    }

    res = requests.post(OLLAMA_URL, json=payload)
    data = res.json()

    raw = data["message"]["content"]

    print("\nRAW LLM:", raw)

    try:
        cleaned = clean_json(raw)
        return json.loads(cleaned)
    except:
        return {"tool": "none", "args": {}}