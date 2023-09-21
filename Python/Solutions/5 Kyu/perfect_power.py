def isPP(n: int) -> list | None:
    for x in range(2, int(pow(n, 1 / 2) + 1)):
        y = n
        i = 0
        while y % x == 0:
            y /= x
            i += 1
            if y == 1:
                return [x, i]
    return None
