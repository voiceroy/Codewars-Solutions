def to_weird_case(words: str) -> str:
    result = ""

    flag = 1
    for i in range(len(words)):
        if words[i] in " ":
            result += " "
            flag = 1
            continue

        if flag == 1:
            result += words[i].upper()
            flag = 0

        else:
            result += words[i].lower()
            flag = 1

    return result
