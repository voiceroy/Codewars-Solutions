from itertools import permutations as permute


def permutations(s: str) -> list:
    permuted = list({"".join(x) for x in permute(s)})
    return permuted
