def solution(s: str) -> list:
    if len(s) % 2 == 0:
        return [s[x : x + 2] for x in range(0, len(s), 2)]
    else:
        s = s + "_"
        return [s[x : x + 2] for x in range(0, len(s), 2)]
