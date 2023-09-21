def solution(s: str) -> str:
    return "".join([" " + x if x.isupper() else x for x in s])
