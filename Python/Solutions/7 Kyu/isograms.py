def is_isogram(string: str) -> bool:
    return len(string.lower()) == len(set(string.lower()))
