def animals(heads: int, legs: int) -> tuple | str:
    x = (2 * heads - legs / 2, legs / 2 - heads)
    return x if legs % 2 == 0 and x[0] >= 0 and x[1] >= 0 else "No solutions"
