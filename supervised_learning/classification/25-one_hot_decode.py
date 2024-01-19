#!/usr/bin/env python3

""" One-Hot Encode
"""


import numpy as np


def one_hot_decode(one_hot):
    """Converts a one-hot matrix into a vector of labels

    Args:
        one_hot (_type_): _description_
    """
    shape = one_hot.shape
    label = np.zeros(shape[0])
    for i in range(shape[0]):
        for j in range(shape[1]):
            if one_hot[i][j] == 1:
                label[j] = i

    # covert all element of the vector to int
    label = label.astype(int)
    return label
