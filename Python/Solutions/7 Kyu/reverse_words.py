def reverse_words(text: str) -> str:
    return " ".join([x[::-1] for x in text.split(" ")]).strip()
