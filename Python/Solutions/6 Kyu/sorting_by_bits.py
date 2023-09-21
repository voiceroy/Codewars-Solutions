def sort_by_bit(arr: list) -> None:
    arr.sort(key=lambda x: (bin(x).count("1"), x))
