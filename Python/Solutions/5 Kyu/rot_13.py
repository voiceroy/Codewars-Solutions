import codecs


def rot13(message: str) -> str:
    return codecs.encode(message, "rot13")
