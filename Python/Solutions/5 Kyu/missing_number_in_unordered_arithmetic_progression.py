def find(seq: list) -> int:
    sorted_seq = sorted(seq)
    a = sorted_seq[0]
    l = sorted_seq[-1]
    n = len(sorted_seq) + 1
    d = (l - a) / (n - 1)

    return int((n * (a + l) / 2) - sum(sorted_seq))
