#!/usr/bin/env python3
"""
Calculates the integral of a polynomial
"""


def poly_integral(poly, c=0):
    """ Calculates the integral of a polynomial

    Args:
        poly (_type_): _description_
        c (int, optional): _description_. Defaults to 0.
    """
    integral = []
    if not isinstance(poly, list) and not isinstance(c, int):
        return None

    # integral.append(c)
    for i in range(len(poly)-1, 0, -1):

        integral.append(poly[i]/(i+1))
    integral.append(poly[0])
    integral.append(c)
    return integral[::-1]

# poly = [5, 3, 0, 1]
# print(poly_integral(poly))
