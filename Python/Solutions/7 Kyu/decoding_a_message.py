from string import ascii_lowercase


def decode(message: str) -> str:
    return message.translate(message.maketrans(ascii_lowercase, ascii_lowercase[::-1]))
