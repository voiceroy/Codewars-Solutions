def duplicate_count(text: str):
    text = text.lower()
    return len([x for x in set(text) if text.count(x) > 1])
