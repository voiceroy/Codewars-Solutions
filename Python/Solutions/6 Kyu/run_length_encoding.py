def run_length_encoding(s: str) -> list:
    prev_char = None

    encoding = []
    encoding_index = 0

    for char in s:
        if prev_char == None:
            prev_char = char
            encoding.append([1, char])

        elif char != prev_char:
            prev_char = char

            encoding_index += 1
            encoding.append([1, char])

        elif char == prev_char:
            encoding[encoding_index][0] += 1

    return encoding
