import re

def contains_markdown_code(text: str) -> bool:
    if re.search(r"```[\s\S]*?```", text): 
        return True

    if re.search(r"`[^`]+`", text):
        return True

    return False
