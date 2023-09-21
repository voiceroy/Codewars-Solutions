def cakes(recipe: dict, available: dict) -> int:
    try:
        no_of_cakes = [
            available[ingredient] // recipe[ingredient] for ingredient in recipe
        ]
    except KeyError:
        return 0

    return min(no_of_cakes)
