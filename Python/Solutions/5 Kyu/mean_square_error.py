def solution(array_a: list, array_b: list) -> float:
    return sum((x - y) ** 2 for x, y in zip(array_a, array_b)) / len(array_a)
