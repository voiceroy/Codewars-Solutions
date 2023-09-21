from itertools import groupby


def set_reducer(inp: list) -> int:
    return (
        inp[0] if len(inp) == 1 else set_reducer([len([*g]) for _, g in groupby(inp)])
    )
