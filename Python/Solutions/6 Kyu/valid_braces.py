def valid_braces(string: str) -> bool:
    parentheses = []
    pairs = {"{": "}", "[": "]", "(": ")", "}": "{", "]": "[", ")": "("}

    for brace in string:
        if brace in "({[":
            parentheses.append(brace)
        else:
            if not parentheses:
                return False
            elif pairs[brace] == parentheses[-1]:
                parentheses.pop()
            else:
                return False

    if parentheses:
        return False

    return True
