from math import floor


def get_average(marks: list) -> int:
    return floor(sum(marks) / len(marks))
