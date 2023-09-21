import re


def dashatize(n: int) -> str:
    return (
        re.sub(r"([13579])", lambda x: "-" + x.group(0) + "-", str(n))
        .replace("--", "-")
        .strip("-")
    )
