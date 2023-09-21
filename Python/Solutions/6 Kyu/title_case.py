from turtle import title


def title_case(title: str, minor_words: str = "") -> str:
    title_words = title.split(" ")
    minor_words_ = set(minor_words.lower().split(" "))

    result_string = []

    for i in range(len(title_words)):
        if i == 0:
            result_string.append(title_words[i].title())
        elif (word := title_words[i]).lower() in minor_words_:
            result_string.append(word.lower())
        else:
            result_string.append(word.title())

    return " ".join(result_string)
