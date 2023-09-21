def encrypt_this(text: str) -> str:
    if text:
        words = []

        for word in text.split():
            if len(word) > 1:
                last_letter = word[-1]
                second_letter = word[1]

                word = word[:-1] + second_letter
                word = word[0] + last_letter + word[2:]
                word = str(ord(word[0])) + word[1:]

                words.append(word)
            else:
                words.append(str(ord(word)))

        return " ".join(words)
    else:
        return ""
