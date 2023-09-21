precalculated = [0, 1, 1]


def u(n: int) -> int:
    if n < len(precalculated):
        return precalculated[n]
    else:
        value = u(n - u(n - 1)) + u(n - u(n - 2))
        precalculated.append(value)
        return value


def length_sup_u_k(n: int, k: int) -> int:
    return sum(1 for i in range(1, n + 1) if u(i) >= k)


def comp(n: int) -> int:
    return sum(1 for i in range(1, n + 1) if u(i) < u(i - 1))
