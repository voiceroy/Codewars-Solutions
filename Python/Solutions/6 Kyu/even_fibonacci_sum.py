def even_fib(m: int) -> int:
    fibs = [0, 1]

    current_fib = fibs[-1]

    while current_fib < m:
        fibs.append(fibs[-1] + fibs[-2])
        current_fib = fibs[-1]

    return sum(x for x in fibs if x < m and x % 2 == 0)
