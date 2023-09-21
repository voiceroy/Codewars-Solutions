def get_count(sentence: str) -> int:
    return sum([sentence.count(x) for x in set(sentence) if x in "aeiou"])
