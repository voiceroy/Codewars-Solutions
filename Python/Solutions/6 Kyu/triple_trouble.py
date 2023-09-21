def triple_double(num1: int, num2: int) -> int:
    return any(x * 3 in str(num1) and x * 2 in str(num2) for x in "0123456789")
