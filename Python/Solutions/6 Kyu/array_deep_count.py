def deep_count(a: list) -> int:
    count = 0
    for x in a:
        if isinstance(x, list):
            count += deep_count(x)
        count += 1
    return count
