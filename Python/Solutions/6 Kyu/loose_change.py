def loose_change(cents: int) -> dict:
    changes = {"Pennies": 0, "Nickels": 0, "Dimes": 0, "Quarters": 0}

    if cents <= 0:
        return changes

    denominations = {
        25: "Quarters",
        10: "Dimes",
        5: "Nickels",
        1: "Pennies",
    }

    amount = cents

    for denomation_value in denominations:
        nos = amount // denomation_value

        changes[denominations[denomation_value]] = nos

        amount -= nos * denomation_value

    return changes
