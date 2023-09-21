from string import ascii_lowercase


def is_pangram(s: str) -> bool:
    return {x for x in s.lower() if x in ascii_lowercase} == set(ascii_lowercase)
