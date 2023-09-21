def multiplication_table(size: int) -> list:
    ret = []
    for row in range(1, size + 1):
        ret.append([row * x for x in range(1, size + 1)])
    return ret
