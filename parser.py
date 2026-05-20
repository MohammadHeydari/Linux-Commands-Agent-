import re

def extract_action(text):
    match = re.search(r"Action Input: (.*)", text)
    if match:
        return match.group(1)
    return None