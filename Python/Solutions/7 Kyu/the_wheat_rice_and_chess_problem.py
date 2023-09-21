def squares_needed(grains: int) -> int:
    return 0 if grains == 0 else 1 + squares_needed(grains // 2)
