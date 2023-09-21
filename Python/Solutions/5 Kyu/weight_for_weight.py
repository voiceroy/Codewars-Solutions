def order_weight(strng: str) -> str:
    weights = [[int(x), sum(int(i) for i in x)] for x in strng.split()]
    return " ".join(str(x[0]) for x in sorted(weights, key=lambda x: [x[1], str(x[0])]))
