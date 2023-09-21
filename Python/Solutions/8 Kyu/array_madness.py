def array_madness(a: list, b: list) -> bool:
    return sum(x**2 for x in a) > sum(y**3 for y in b)
