def find_uniq(arr: list) -> float | int:
    return [x for x in set(arr) if arr.count(x) == 1][0]
