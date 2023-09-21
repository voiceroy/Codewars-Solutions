from functools import reduce


def persistence(n: int) -> int:
    count = 0
    while len(str(n)) != 1:
        n = reduce(lambda x, y: x * y, [int(x) for x in list(str(n))])
        count += 1
    return count
