import enum


def valid_ISBN10(isbn: str) -> bool:
    if len(isbn) != 10:
        return False

    if not isbn[-1].isnumeric() and isbn[-1] != "X":
        return False

    if not isbn[:-1].isnumeric():
        return False

    return (
        sum(
            int(char) * index if char != "X" else 100
            for index, char in enumerate(isbn, start=1)
        )
        % 11
        == 0
    )
