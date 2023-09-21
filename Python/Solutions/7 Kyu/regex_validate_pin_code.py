import re


def validate_pin(pin: str) -> bool:
    return bool(re.fullmatch(r"\d{4}|\d{6}", pin))
