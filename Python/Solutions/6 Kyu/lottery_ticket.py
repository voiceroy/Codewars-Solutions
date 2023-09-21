def bingo(ticket: list, win: int) -> str:
    return (
        "Winner!"
        if sum(1 for lot in ticket if chr(lot[1]) in lot[0]) >= win
        else "Loser!"
    )
