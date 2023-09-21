def comp(array1: list, array2: list) -> bool:
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        return False
