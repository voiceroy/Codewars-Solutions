def is_triangle(a: int, b: int, c: int) -> bool:
    return sum(sorted([a, b, c])[:-1]) > max(a, b, c)
