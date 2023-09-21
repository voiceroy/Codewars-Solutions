def square_digits(num: int) -> int:
    return int("".join([str(int(x) ** 2) for x in str(num)]))
