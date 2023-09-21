def parse(data: str) -> list:
    array = []
    i = 0

    for char in data:
        match char:
            case "i":
                i += 1
            case "d":
                i -= 1
            case "s":
                i **= 2
            case "o":
                array.append(i)

    return array
