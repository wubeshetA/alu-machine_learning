#!/usr/bin/env python3


""" Normal class module for Normal distribution calculations """


class Normal:
    """ Normal class
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """ Constructor
        """
        self.E = 2.7182818285
        self.PI = 3.1415926536

        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            else:
                self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = sum(data) / len(data)
            self.stddev = (sum([(x - self.mean) ** 2 for x in data])
                           / len(data)) ** 0.5

    def z_score(self, x):
        """ Calculates the z-score of a given x-value
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """ Calculates the x-value of a given z-score
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """ Calculates the value of the PDF for a given time period
        """
        return (self.E ** (-0.5 * ((x - self.mean) / self.stddev) ** 2)
                / (self.stddev * ((2 * self.PI) ** 0.5)))


if __name__ == "__main__":
    import numpy as np
    np.random.seed(0)
    data = np.random.normal(70, 10, 100).tolist()
    n1 = Normal(data)
    print('PSI(90):', n1.pdf(90))

    n2 = Normal(mean=70, stddev=10)
    print('PSI(90):', n2.pdf(90))
