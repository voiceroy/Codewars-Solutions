def get_middle(s: str) -> str:
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1 : len(s) // 2 + 1]
