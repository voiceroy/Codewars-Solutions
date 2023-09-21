def sum_strings(x: str, y: str) -> str:
    if len(x) == 0 and len(y) == 0:
        return "0"

    max_len = max(len(x), len(y))
    x, y = x.zfill(max_len), y.zfill(max_len)

    result = ""
    carry = 0
    for i, j in zip(reversed(x), reversed(y)):
        carry, total = divmod(int(i) + int(j) + carry, 10)
        result += str(total)

    return ("1" * carry + result[::-1]).lstrip("0") or "0"
