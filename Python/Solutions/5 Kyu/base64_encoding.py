import base64


def to_base_64(string: str) -> str:
    return base64.b64encode(string.encode()).decode("ascii").replace("=", "")


def from_base_64(string: str) -> str:
    return base64.b64decode(string + "==").decode("ascii")
