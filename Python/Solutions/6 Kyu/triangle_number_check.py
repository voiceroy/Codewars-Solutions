from math import sqrt


def is_triangle_number(number: int) -> bool:
    return (
        ((-1 + sqrt(8 * number + 1)) / 2).is_integer() if type(number) == int else False
    )
