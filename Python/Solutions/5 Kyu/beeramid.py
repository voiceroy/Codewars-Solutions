def beeramid(bonus: int, price: float) -> int:
    if bonus <= 0 or price <= 0:
        return 0

    total_cans = bonus // price
    cans = 0
    layers = 0

    while True:
        if cans == total_cans:
            return layers

        if cans > total_cans:
            return layers - 1

        layers += 1
        cans += layers**2
