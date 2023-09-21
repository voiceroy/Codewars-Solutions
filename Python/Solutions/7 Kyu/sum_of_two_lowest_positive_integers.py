def sum_two_smallest_numbers(numbers: list) -> int:
    return sum(sorted(numbers)[:2])
