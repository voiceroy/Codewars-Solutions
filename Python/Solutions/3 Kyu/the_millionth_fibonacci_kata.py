from gmpy2 import fib as f


def fib(n: int) -> int:
    if n < 0:
        if n % 2 == 0:
            return -int(f(abs(n)))
        else:
            return int(f(abs(n)))
    else:
        return int(f(n))
