#!/usr/bin/env python3
# write module documentation here
""" Poisson class module for Poisson distribution calculations """


class Poisson:
    """ Poisson class
    """

    def __init__(self, data=None, lambtha=1.):
        """ Constructor
        """
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


if __name__ == '__main__':
    import numpy as np
    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
    # count, bins, ignored = plt.hist(data, 14, density=True)
    # plt.show()
    print(data)
