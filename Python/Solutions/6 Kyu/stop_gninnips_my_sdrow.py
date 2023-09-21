def spin_words(sentence: str) -> str:
    return " ".join([x if len(x) < 5 else x[::-1] for x in sentence.split()])
