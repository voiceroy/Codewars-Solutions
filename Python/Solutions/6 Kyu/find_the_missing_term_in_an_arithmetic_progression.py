def find_missing(sequence: list) -> int:
    a = sequence[0]
    n = len(sequence) + 1  # Since only 1 element is missing
    l = sequence[-1]
    d = (l - a) / (n - 1)

    return int((n * (a + l) / 2) - sum(sequence))
