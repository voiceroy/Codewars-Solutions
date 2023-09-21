def compute_sum(n: int) -> int:
    return sum(sum(int(x) for x in str(x)) for x in range(1, n + 1))
