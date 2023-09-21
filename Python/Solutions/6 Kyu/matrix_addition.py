def matrix_addition(a: list, b: list) -> list:
    result = [list() for x in range(len(a))]

    for row in range(len(a)):
        for column in range(len(a[0])):
            result[row].append(a[row][column] + b[row][column])

    return result
