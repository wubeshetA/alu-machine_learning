#!/usr/bin/env python3

""" Poisson class module for Poisson distribution calculations """


class Poisson:
    """ Poisson class
    """

    def __init__(self, data=None, lambtha=1.):
        """ Constructor
        """
        self.E = 2.7182818285
        self.PI = 3.1415926536

        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data) / len(data))

    def factorial(self, k):
        result = 1
        for i in range(1, k+1):
            result *= i
        return result

    def pmf(self, k):
        """ Calculates the value of the PMF for a given number of "successes."

        Args:
            k (int): number of "successes"
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        p = (self.lambtha ** k) * (self.E ** -self.lambtha) / self.factorial(k)
        return p

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of "successes."

        Args:
            k (int): is the number of successes.
        """

        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        def p(k):

            p = (self.lambtha ** k) * (self.E ** -
                                       self.lambtha) / self.factorial(k)
            return p
        return sum([p(k) for k in range(0, k+1)])
