from gmpy2 import is_prime


def prime(n: int) -> list:
    return [x for x in range(n + 1) if is_prime(x)]
