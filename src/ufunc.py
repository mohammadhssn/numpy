"""
    https://numpy.org/doc/1.26/reference/ufuncs.html
"""

import numpy as np

# This code is done by Python
t = 0
for i in np.arange(10000):  # 
    t += i

# ----------------------------------------------------------------
# This code is done by C (vectorized)
np.sum(np.arange(10000))

one = np.array([1, 2, 3])
two = np.array([4, 5, 6])

print(np.add(one, two))  # element-wise -> [5 7 9]

# Methods
print(np.add.reduce(one))  # 6
print(np.add.accumulate(one))  # [1, 3, 6]
print(np.add.outer(one, two))
"""[[5 6 7]
 [6 7 8]
 [7 8 9]]
"""
