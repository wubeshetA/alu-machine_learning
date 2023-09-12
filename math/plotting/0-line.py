#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)
plt.plot(x, y, c="r")
# set left and right limits
plt.xlim(left=0, right=10)
plt.show()
