def decode(string: str) -> str:
    kv = {x: y for x, y in zip("1234567890", "9876043215")}
    return string.translate(str().maketrans(kv))
