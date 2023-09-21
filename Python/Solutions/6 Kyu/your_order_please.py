def order(sentence: str) -> str:
    return " ".join(sorted(sentence.split(), key=min))
