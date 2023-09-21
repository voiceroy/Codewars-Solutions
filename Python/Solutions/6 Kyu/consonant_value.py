import re


def solve(s: str) -> int:
    return max(
        sum(ord(x) - 96 for x in y) for y in (re.sub(r"[aeiou]", " ", s).split())
    )
