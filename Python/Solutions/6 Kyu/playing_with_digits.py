def dig_pow(n: int, p: int) -> int:
    digits_sum = sum([x**y for y, x in enumerate([int(x) for x in str(n)], start=p)])

    result = digits_sum / n

    if result.is_integer():
        return result
    else:
        return -1
