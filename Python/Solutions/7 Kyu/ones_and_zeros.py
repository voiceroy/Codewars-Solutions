def binary_array_to_number(arr: list) -> int:
    return int("".join([str(x) for x in arr]), 2)
