def descending_order(num: int) -> int:
    return int("".join(sorted(str(num), reverse=True)))
