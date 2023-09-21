def pythagorean_triple(integers: list) -> bool:
    integers = sorted(integers)
    return integers[0] ** 2 + integers[1] ** 2 == integers[2] ** 2
