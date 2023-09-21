import operator


def meeting(s: str) -> str:
    return "".join(
        f"({x[1]}, {x[0]})"
        for x in sorted(
            (x.split(":") for x in s.upper().split(";")),  # [First, Last]
            key=operator.itemgetter(1, 0),
        )
    )
