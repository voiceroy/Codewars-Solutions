def scramble(s1: str, s2: str) -> bool:
    s1_count = {x: s1.count(x) for x in set(s1)}
    s2_count = {x: s2.count(x) for x in set(s2)}
    try:
        return all(
            [True if s1_count[x] >= s2_count[x] else False for x in s2_count.keys()]
        )
    except KeyError:
        return False
