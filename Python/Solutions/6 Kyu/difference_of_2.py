def twos_difference(lst: list) -> list:
    return sorted(((x - 2, x) for x in lst if x - 2 in lst))
