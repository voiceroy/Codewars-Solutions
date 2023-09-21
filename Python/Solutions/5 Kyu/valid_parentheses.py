def valid_parentheses(string: str) -> bool:
    cnt = 0
    for char in string:
        if char == "(":
            cnt += 1
        if char == ")":
            cnt -= 1
        if cnt < 0:
            return False
    return not bool(cnt)
