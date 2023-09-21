from gmpy2 import is_prime, next_prime


def backwards_prime(start: int, stop: int) -> list:
    result = []

    last_prime = int(next_prime(start - 1))
    reversed_prime = int(str(last_prime)[::-1])

    while last_prime <= stop:
        if is_prime(reversed_prime) and last_prime != reversed_prime:
            result.append(last_prime)

        last_prime = int(next_prime(last_prime))
        reversed_prime = int(str(last_prime)[::-1])

    return result
