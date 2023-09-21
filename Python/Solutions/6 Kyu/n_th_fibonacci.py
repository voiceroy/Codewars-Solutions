memo = {1: 0, 2: 1}


def nth_fib(n: int, memo: dict = memo) -> int:
    if n in memo:
        return memo[n]
    else:
        return nth_fib(n - 1) + nth_fib(n - 2)
