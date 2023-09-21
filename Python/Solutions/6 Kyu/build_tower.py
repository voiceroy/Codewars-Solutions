def tower_builder(n_floors: int) -> list:
    return [f"{'*'*(2*n+1):^{2*n_floors-1}}" for n in range(n_floors)]
