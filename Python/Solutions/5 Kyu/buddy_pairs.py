from math import isqrt


def sum_of_divisors(n):
    result = 1
    div = 1
    while True:
        for div in range(div + 1, isqrt(n) + 1):
            if not n % div:
                mul = 1
                while not n % div:
                    n //= div
                    mul = 1 + mul * div
                result *= mul
                break
        else:
            if n > 1:
                result *= 1 + n
            return result


s = lambda n: sum_of_divisors(n) - n


def buddy(start: int, limit: int) -> list | str:
    for n in range(start, limit + 1):
        m = s(n) - 1
        if m > n and s(m) == n + 1:
            return [n, m]
    return "Nothing"
