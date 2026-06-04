import re

def analyze_text(text):

    if not isinstance(text, str):
        return None

    return {
        "words": len(text.split()),
        "numbers": len(re.findall(r'\d+', text)),
        "special_chars": len(re.findall(r'[^a-zA-Z0-9\s]', text)),
        "spaces": text.count(' ')
    }
