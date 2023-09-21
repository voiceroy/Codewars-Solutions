def mygcd(x: int, y: int) -> int:
    _, remainder = divmod(x, y)
    if remainder == 0:
        return y
    return mygcd(y, remainder)
