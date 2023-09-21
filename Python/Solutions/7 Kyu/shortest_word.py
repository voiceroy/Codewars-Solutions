def find_short(s: str) -> int:
    return len(sorted(s.split(), key=lambda x: len(x))[0])
