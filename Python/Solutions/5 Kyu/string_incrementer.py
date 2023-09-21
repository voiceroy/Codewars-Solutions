def increment_string(string: str) -> str:
    strng = string.rstrip("0123456789")
    num = string[len(strng) :]

    if num == "":
        return strng + "1"

    return strng + str(int(num) + 1).zfill(len(num))
