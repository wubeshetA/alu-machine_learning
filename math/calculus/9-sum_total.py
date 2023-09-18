#!/usr/bin/env python3
"""
Summation of squared values
"""


def summation_i_squared(n):
    """ Sum i squared

    Args:
        n (_type_): _description_
    """
    if n < 1:
        return None
    else:
        return sum([i**2 for i in range(1, n+1)])