from collections import Counter


def number_of_pairs(gloves: list) -> int:
    pairs = Counter(gloves)
    return sum(pairs[x] // 2 for x in pairs)
