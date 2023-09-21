from itertools import cycle


def encode(message: str, key: int) -> list:
    return [sum((ord(x) - 96, int(y))) for x, y in zip(message, cycle(str(key)))]
