def rgb(r: int, g: int, b: int) -> str:
    clamp = lambda n: max(min(255, n), 0)
    r, g, b = map(clamp, [r, g, b])
    return "".join([hex(x)[2:].zfill(2) for x in (r, g, b)]).upper()
