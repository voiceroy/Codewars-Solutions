def find_it(seq: list) -> int:
    return [x for x in set(seq) if seq.count(x) % 2 != 0][0]
