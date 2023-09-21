def positive_sum(arr: list) -> int:
    return sum([x for x in arr if x > 0]) if arr else 0