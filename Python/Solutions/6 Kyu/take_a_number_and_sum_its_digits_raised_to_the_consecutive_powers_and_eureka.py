def sum_dig_pow(a: int, b: int) -> list:
    return [
        x
        for x in range(a, b + 1)
        if sum(int(x) ** p for p, x in enumerate(str(x), start=1)) == x
    ]
