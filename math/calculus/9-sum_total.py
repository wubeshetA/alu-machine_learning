#!/usr/bin/env python3
"""
Summation of squared values
"""


def summation_i_squared(n):
    """ Sum i squared

    Args:
        n (_type_): _description_
    """
    if n == 1:
        return 1
    if n < 1:
        return None
    else:
        return n**2 + summation_i_squared(n-1)

# print(summation_i_squared(0))
