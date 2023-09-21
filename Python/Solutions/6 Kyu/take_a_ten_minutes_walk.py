def is_valid_walk(walk: list) -> bool:
    return (
        True
        if walk.count("n") == walk.count("s")
        and walk.count("e") == walk.count("w")
        and len(walk) == 10
        else False
    )
