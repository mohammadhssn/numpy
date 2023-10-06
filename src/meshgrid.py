"""
    https://numpy.org/doc/1.26/reference/generated/numpy.meshgrid.html#numpy-meshgrid
"""

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

xx, yy = np.meshgrid(x, y)

plt.plot(xx, yy, marker='o', color='k', linestyle='none')
plt.xticks(x)
plt.yticks(y)
plt.show()

# ---------------------------------------------------------------
print(xx)
print('**********')
print(yy)
"""
[[1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]]
**********
[[5 5 5 5]
 [6 6 6 6]
 [7 7 7 7]
 [8 8 8 8]]
"""
