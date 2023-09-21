def f(n: int) -> int:
    if n == 0:
        return 1
    return n - m(f(n - 1))


def m(n: int) -> int:
    if n == 0:
        return 0
    return n - f(m(n - 1))
