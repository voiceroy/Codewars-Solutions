import re


def count_smileys(arr: list) -> int:
    return len(re.findall(r"[:;][-~]?[)D]", " ".join(arr)))
