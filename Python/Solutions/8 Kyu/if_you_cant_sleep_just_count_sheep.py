def count_sheep(n: int) -> str:
    return "".join([f"{x} sheep..." for x in range(1, n + 1)])
