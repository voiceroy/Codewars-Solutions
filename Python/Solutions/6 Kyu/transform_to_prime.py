from gmpy2 import is_prime, next_prime


def minimum_number(numbers: list) -> int:
    sum_numbers = sum(numbers)

    if is_prime(sum_numbers):
        return 0

    return next_prime(sum_numbers) - sum_numbers
