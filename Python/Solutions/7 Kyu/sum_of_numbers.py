def get_sum(a: int, b: int) -> int:
    return sum(range(min(a, b), max(a, b) + 1)) if a != b else a
