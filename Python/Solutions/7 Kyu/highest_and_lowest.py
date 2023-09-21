def high_and_low(numbers: str) -> str:
    numbers = sorted([int(x) for x in numbers.split()])
    return f"{numbers[-1]} {numbers[0]}"
