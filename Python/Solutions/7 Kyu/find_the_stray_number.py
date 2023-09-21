def stray(arr: list) -> int:
    return max(x for x in arr if arr.count(x) == 1)
