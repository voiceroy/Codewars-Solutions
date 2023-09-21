def digitize(n: int) -> list:
    return [int(x) for x in str(n)[::-1]]
