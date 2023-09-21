import re


def to_camel_case(text: str) -> str:
    pattern = r"[-_]"
    matches = re.split(pattern, text)
    return "".join(
        [matches[x].title() if x > 0 else matches[x] for x in range(len(matches))]
    )
