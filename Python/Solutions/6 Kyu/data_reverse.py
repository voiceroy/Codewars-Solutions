def data_reverse(data: list) -> list:
    return [
        y for x in [data[x : x + 8] for x in range(0, len(data), 8)][::-1] for y in x
    ]
