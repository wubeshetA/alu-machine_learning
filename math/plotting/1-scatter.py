#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pprint

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
# print(x)
# calculate mean
y_mean = np.mean(y)
print("mean of y = ", y_mean)
x_mean = np.mean(x)
print("mean of x: ", x_mean)

y += 180

plt.scatter(x, y, c='m')
plt.title("Men's Height vs Weight")
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.show()
