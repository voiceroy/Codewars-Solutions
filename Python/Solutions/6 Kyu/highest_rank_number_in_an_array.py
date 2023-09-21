def highest_rank(arr: list) -> int:
    counts = {arr.count(x): x for x in sorted(set(arr))}
    return counts[max(counts.keys())]
