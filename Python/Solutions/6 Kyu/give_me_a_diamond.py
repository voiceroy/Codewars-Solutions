def diamond(n: int) -> str:
    if n % 2 == 0 or n < 1:
        return None

    return (
        "".join(
            " " * ((n - i) // 2) + "*" * i + "\n" for i in range(1, n, 2)
        )  # Upper half
        + ("*" * n + "\n")  # Middle row
        + "".join(
            " " * ((n - i) // 2) + "*" * i + "\n" for i in range(n - 2, -1, -2)
        )  # Lower half
    )
