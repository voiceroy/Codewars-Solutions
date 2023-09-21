from hashlib import md5


def crack(hash: str) -> str:
    i = 0
    while i < 99999:
        str_i = str(i).rjust(5, "0")
        if md5(str_i.encode("utf-8")).hexdigest() == hash:
            return str_i
        i += 1
    return ""
