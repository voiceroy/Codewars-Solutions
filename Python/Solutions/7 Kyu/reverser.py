def reverse(n: int, result: int = 0) -> int:
    return result if n == 0 else reverse(n // 10, result * 10 + n % 10)
