def accum(s: str) -> str:
    return "-".join([str(x * i).title() for (i, x) in enumerate(s, start=1)])
