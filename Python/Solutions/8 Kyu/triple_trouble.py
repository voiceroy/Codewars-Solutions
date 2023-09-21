def triple_trouble(one: str, two: str, three: str) -> str:
    return "".join([x[i] for i in range(len(one)) for x in [one, two, three]])
