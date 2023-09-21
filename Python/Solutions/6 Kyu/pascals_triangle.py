from math import comb

memo = {}


def pascals_triangle(n: int, memo: dict = memo) -> list:
    flat_triangle = []

    for i in range(n):
        if i not in memo:
            memo[i] = [comb(i, k) for k in range(i + 1)]
            flat_triangle.extend(memo[i])
        else:
            flat_triangle.extend(memo[i])

    return flat_triangle
