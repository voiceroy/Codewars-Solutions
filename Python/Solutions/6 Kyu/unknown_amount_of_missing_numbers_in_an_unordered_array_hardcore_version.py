def miss_nums_finder(arr: list) -> list:
    return sorted(set(range(1, max(arr))).difference(set(arr)))
