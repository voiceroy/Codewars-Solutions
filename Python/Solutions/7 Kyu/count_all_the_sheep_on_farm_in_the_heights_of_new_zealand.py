def lost_sheep(friday: list, saturday: list, total: int) -> int:
    return total - sum(friday + saturday)
