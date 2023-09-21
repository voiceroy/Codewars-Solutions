from gmpy2 import next_prime


def gap(g: int, m: int, n: int) -> list | None:
    prime = int(next_prime(m - 1))
    prev_prime = prime

    while prime <= n:
        if prime - prev_prime == g:
            return [prev_prime, prime]

        prev_prime = prime
        prime = int(next_prime(prime))
    else:
        return None
