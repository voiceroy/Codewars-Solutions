from math import sqrt


def find_next_square(sq: int) -> int:
    if not sqrt(sq).is_integer():
        return -1

    return int(pow(sqrt(sq) + 1, 2))
