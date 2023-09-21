def narcissistic(value: int) -> bool:
    return sum([pow(int(x), len(str(value))) for x in str(value)]) == value
