def two_sum(numbers: list, target: int) -> list:
    for i in range(len(numbers)):
        for j in [x for x in range(len(numbers)) if x != i]:
            if numbers[i] + numbers[j] == target:
                return [i, j]
    else:
        return []
