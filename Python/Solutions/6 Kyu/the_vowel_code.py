def encode(st: str) -> str:
    return st.translate(st.maketrans("aeiou", "12345"))


def decode(st: str) -> str:
    return st.translate(st.maketrans("12345", "aeiou"))
