memo = {0: 0, 1: 1}


def fibonacci(n: int, memo: dict = memo) -> int:
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
