def alphabet_position(text: str) -> str:
    positions = {
        alpha: position
        for alpha, position in zip("abcdefghijklmnopqrstuvwxyz", range(1, 27))
    }
    return " ".join([str(positions[char.lower()]) for char in text if char.isalpha()])
