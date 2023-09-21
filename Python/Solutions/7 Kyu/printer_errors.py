def printer_error(s: str) -> str:
    return f"{sum([1 for x in s if x not in 'abcdefghijklm'])}/{len(s)}"
