def in_array(array1: list, array2: list) -> list:
    return sorted({x for x in array1 for y in array2 if x in y})
