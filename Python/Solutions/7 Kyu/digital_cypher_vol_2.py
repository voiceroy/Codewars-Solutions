from itertools import cycle


def decode(code: list, key: int) -> str:
    return "".join(chr(x + 96 - int(y)) for x, y in zip(code, cycle(str(key))))
