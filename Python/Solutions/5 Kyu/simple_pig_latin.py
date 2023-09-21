def pig_it(text: str) -> str:
    return " ".join([x[1:] + x[0] + "ay" if x.isalpha() else x for x in text.split()])
