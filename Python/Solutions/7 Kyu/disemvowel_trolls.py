def disemvowel(string: str) -> str:
    return "".join([x for x in string if x.lower() not in "aeiou"])
