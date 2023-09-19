#!/usr/bin/env python3
"""
Calculates the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """ Calculates the integral of a polynomial
    """
    integral = []
    if not isinstance(poly, list) and not isinstance(C, int):
        return None

    # integral.append(c)
    for i in range(len(poly)-1, 0, -1):

        integral.append(poly[i]/(i+1))
    integral.append(poly[0])
    integral.append(C)
    for i in range(len(integral)):
        if integral[i] % 1 == 0:
            integral[i] = int(integral[i])

    return integral[::-1]


# poly = [5, 3, 0, 1]
# print(poly_integral(poly, C=4))
