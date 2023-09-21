def good_vs_evil(good: str, evil: str) -> str:
    good_sum = sum(int(x) * y for x, y in zip(good.split(" "), [1, 2, 3, 3, 4, 10]))
    bad_sum = sum(int(x) * y for x, y in zip(evil.split(" "), [1, 2, 2, 2, 3, 5, 10]))

    if good_sum > bad_sum:
        return "Battle Result: Good triumphs over Evil"
    elif good_sum < bad_sum:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
