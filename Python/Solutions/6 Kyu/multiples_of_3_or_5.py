def solution(number: int) -> int:
    return sum([x for x in range(1, number) if x % 3 == 0 or x % 5 == 0])
