def digital_root(n: int) -> int:
    dr = sum([int(x) for x in str(n)])
    return dr if dr < 10 else digital_root(dr)
