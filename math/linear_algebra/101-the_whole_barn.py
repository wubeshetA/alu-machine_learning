#!/usr/bin/env python3

"""
Matrix addition
"""
import numpy as np


def add_matrices(mat1, mat2):
    """Add the two matrices

    Args:
        mat1 (_type_): _description_
        mat2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    matrix1 = np.array(mat1)
    matrix2 = np.array(mat2)
    if matrix1.shape != matrix2.shape:
        return None
    return matrix1 + matrix2

# mat1 = [1, 2, 3]
# mat2 = [4, 5, 6]
# print(add_matrices(mat1, mat2))
# mat1 = [[1, 2], [3, 4]]
# mat2 = [[5, 6], [7, 8]]

# print(add_matrices(mat1, mat2))

# mat1 = [[[[1, 2, 3, 4], [5, 6, 7, 8]],
#          [[9, 10, 11, 12], [13, 14 ,15, 16]],
#          [[17, 18, 19, 20], [21, 22, 23, 24]]],
#         [[[25, 26, 27, 28], [29, 30, 31, 32]],
#          [[33, 34, 35, 36], [37, 38, 39, 40]],
#          [[41, 42, 43, 44], [45, 46, 47, 48]]]]
# mat2 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
#          [[19, 110, 111, 112], [113, 114 ,115, 116]],
#          [[117, 118, 119, 120], [121, 122, 123, 124]]],
#         [[[125, 126, 127, 128], [129, 130, 131, 132]],
#          [[133, 134, 135, 136], [137, 138, 139, 140]],
#          [[141, 142, 143, 144], [145, 146, 147, 148]]]]
# mat3 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
#          [[117, 118, 119, 120], [121, 122, 123, 124]]],
#         [[[125, 126, 127, 128], [129, 130, 131, 132]],
#          [[141, 142, 143, 144], [145, 146, 147, 148]]]]
# print(add_matrices(mat1, mat2))
# print(add_matrices(mat1, mat3))
