from textwrap import wrap


def int32_to_ip(int32: int) -> str:
    return ".".join(str(int(x, base=2)) for x in wrap(bin(int32)[2:].rjust(32, "0"), 8))
