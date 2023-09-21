def anagrams(word: str, words: list) -> list:
    return [x for x in words if set(word) == set(x) and len(word) == len(x)]
