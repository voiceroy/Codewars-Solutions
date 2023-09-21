import numpy as np


def determinant(matrix: list) -> int:
    return (
        np.round(np.linalg.det(np.matrix(matrix)), decimals=0)
        if len(matrix) > 1
        else matrix[0][0]
    )
