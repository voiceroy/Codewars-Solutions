def rps(p1: str, p2: str) -> str:
    cond = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    if cond[p1] == p2:
        return "Player 1 won!"
    elif cond[p2] == p1:
        return "Player 2 won!"
    else:
        return "Draw!"
