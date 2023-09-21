def prime_factors(n: int) -> str:
    i = 2
    num = n

    factors = []

    while num > 1:
        while num % i == 0:
            factors.append(i)
            num /= i
        i += 1

    factors = {x: factors.count(x) for x in factors}

    return "".join(
        f"({i}**{count})" if count > 1 else f"({i})" for i, count in factors.items()
    )
