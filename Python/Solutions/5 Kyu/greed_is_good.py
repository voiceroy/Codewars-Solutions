from collections import Counter


def score(dice: list) -> int:
    rolls = Counter(dice)

    threes = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    singles = {1: 100, 5: 50}

    score = 0

    for roll in rolls:
        if rolls[roll] >= 3:
            score += threes[roll]
            rolls[roll] -= 3

        if roll in singles:
            score += rolls[roll] * singles[roll]

    return score
