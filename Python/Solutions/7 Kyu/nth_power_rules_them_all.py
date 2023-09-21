def modified_sum(a: list, n: int) -> int:
    return sum(x**n for x in a) - sum(a)