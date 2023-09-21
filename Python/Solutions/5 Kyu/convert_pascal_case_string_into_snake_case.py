import re


def to_underscore(string: str) -> str:
    return (
        "_".join(x.lower() for x in re.findall(r"[A-Z][^A-Z]*", string))
        if type(string) != int
        else str(string)
    )
