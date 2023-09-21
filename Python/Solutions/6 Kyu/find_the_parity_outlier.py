def find_outlier(integers: list) -> int:
    truth = {x: x % 2 == 0 for x in integers}
    return [
        x
        for x in integers
        if truth[x]
        == sorted([x for x in truth.values() if list(truth.values()).count(x) == 1])[0]
    ][0]
