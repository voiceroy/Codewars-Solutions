from math import floor, log2


def zeros(n: int) -> int:
    # Refer https://mathworld.wolfram.com/Factorial.html for the formula
    return (
        sum(floor(n / (5 ** (x))) for x in range(1, floor(log2(n) / log2(5)) + 1))
        if n > 0
        else 0
    )
