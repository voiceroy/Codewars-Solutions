def reverse_letter(string: str) -> str:
    return "".join([x for x in string[::-1] if x.isalpha()])
