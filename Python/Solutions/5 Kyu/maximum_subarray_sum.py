def max_sequence(array: list) -> int:
    sums = []
    i = 0

    if not array:
        return 0

    while i <= len(array):
        j = i + 1
        while j <= len(array):
            sums.append(sum(array[i:j]))
            j += 1
        i += 1

    if max(sums) >= 0:
        return max(sums)
    else:
        return 0
