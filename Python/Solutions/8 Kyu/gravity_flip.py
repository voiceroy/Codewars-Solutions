def flip(d: str, a: list) -> list:
    return sorted(a) if d.lower() == "r" else sorted(a, reverse=True)
