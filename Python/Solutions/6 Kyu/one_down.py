def one_down(txt: str) -> str:
    if type(txt) != str:
        return "Input is not a string"

    return txt.translate(
        txt.maketrans(
            "bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA",
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )
    )
