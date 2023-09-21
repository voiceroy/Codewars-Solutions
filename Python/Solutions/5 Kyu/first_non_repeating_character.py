def first_non_repeating_letter(string: str) -> str:
    try:
        return [x for x in string if string.lower().count(x.lower()) == 1][0]
    except IndexError:
        return ""
