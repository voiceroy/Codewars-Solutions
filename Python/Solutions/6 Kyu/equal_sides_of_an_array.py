def find_even_index(array: list) -> int:
    try:
        return [
            x
            for x in range(len(array))
            if sum(array[:x]) == sum(array[x + 1 :]) and x < len(array)
        ][0]
    except IndexError:
        return -1
