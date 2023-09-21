# Formula used for calculating the exponents of prime factors, https://en.wikipedia.org/wiki/en/Legendre's_formula

from math import floor, log2

from gmpy2 import next_prime


def decomp(n: int) -> str:
    prime = 2
    powers = {}

    while prime <= n:
        powers[prime] = int(
            sum(
                floor(n / prime**i)
                for i in range(1, floor(log2(n) / log2(prime)) + 1)
            )
        )

        prime = next_prime(prime)

    return " * ".join(f"{k}^{v}" if v > 1 else f"{k}" for k, v in powers.items())
