#!/usr/bin/env python3
""" Normalize"""

import numpy as np

def shuffle_data(X, Y):
    """ Shuffle data points in two matrices the same way

    Args:
        X (_type_): _description_
        Y (_type_): _description_
    """
    return np.random.permutation(X), np.random.permutation(Y)