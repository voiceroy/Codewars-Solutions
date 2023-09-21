def transpose(matrix: list) -> list:
    if matrix:
        if len(matrix[0]) > 0:
            return [
                [matrix[j][i] for j in range(len(matrix))]
                for i in range(len(matrix[0]))
            ]
        else:
            return [x[0] for x in matrix]
    else:
        return matrix
