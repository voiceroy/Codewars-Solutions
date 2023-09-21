def decrypt(encrypted_text: str, n: int) -> str:
    if not encrypted_text or encrypted_text is None or n <= 0:
        return encrypted_text

    middle = int(len(encrypted_text) / 2)

    if len(encrypted_text) % 2 != 0:
        last_char = encrypted_text[-1]
    else:
        last_char = ""

    for _ in range(n):
        left = encrypted_text[:middle]
        right = encrypted_text[middle:]

        encrypted_text = "".join(x + y for x, y in zip(right, left)) + last_char

    return encrypted_text


def encrypt(text: str, n: int) -> str:
    if text and n > 0:
        encrypted_text = text

        for i in range(n):
            encrypted_text = encrypted_text[1::2] + encrypted_text[::2]

        return encrypted_text
    else:
        return text
