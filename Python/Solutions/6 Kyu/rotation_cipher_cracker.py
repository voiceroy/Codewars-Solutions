from collections import deque
from string import ascii_lowercase


def decode(msg: str, contents: str) -> list:
    possible = list()
    for i in range(26):
        letters = deque(ascii_lowercase, maxlen=26)
        letters.rotate(i)

        decoded_with_i_rot = msg.translate(
            msg.maketrans(ascii_lowercase, str("".join(x for x in letters)))
        )

        if contents in decoded_with_i_rot:
            possible.append(decoded_with_i_rot)

    return sorted(possible)
