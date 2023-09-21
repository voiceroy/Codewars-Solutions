from textwrap import wrap


def hex_string_to_RGB(hex_string: str) -> dict:
    return {x: int(y, base=16) for x, y in zip("rgb", wrap(hex_string[1:], 2))}
