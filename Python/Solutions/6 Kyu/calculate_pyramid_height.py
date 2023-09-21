def pyramid_height(n: int) -> int:
    layers = 0
    blocks = 0

    while True:
        if blocks == n:
            return layers

        if blocks > n:
            return layers - 1

        layers += 1
        blocks += layers**2
