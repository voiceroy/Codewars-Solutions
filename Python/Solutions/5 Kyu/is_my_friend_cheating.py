def remov_nb(n: int) -> list:
    possibilities = []
    interval_sum = sum(range(1, n + 1))

    for a in range(1, n + 1):
        b = (interval_sum - a) / (a + 1)
        if b.is_integer() and b < n:
            possibilities.append((a, int(b)))

    return possibilities
