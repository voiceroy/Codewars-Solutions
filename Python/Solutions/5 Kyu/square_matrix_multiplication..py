import numpy as np


def matrix_mult(a: list, b: list) -> list:
    return (np.matrix(a) * np.matrix(b)).tolist()
