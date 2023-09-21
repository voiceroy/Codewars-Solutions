def is_opposite(s1: str, s2: str) -> bool:
    return s1.swapcase() == s2 if s1 and s2 else False
