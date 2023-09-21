def high(x: str) -> str:
    words = [x for x in x.lower().split()]
    scores = [sum([ord(x) - 96 for x in x]) for x in words]
    return words[scores.index(max(scores))]
