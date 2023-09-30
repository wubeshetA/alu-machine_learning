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


if __name__ == "__main__":
    import numpy as np
    np.random.seed(0)
    data = np.random.normal(70, 10, 100).tolist()
    n1 = Normal(data)
    print('Mean:', n1.mean, ', Stddev:', n1.stddev)

    n2 = Normal(mean=70, stddev=10)
    print('Mean:', n2.mean, ', Stddev:', n2.stddev)
