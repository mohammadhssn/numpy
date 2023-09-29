# https://numpy.org/doc/1.26/user/basics.broadcasting.html
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

b = np.array([
    [4, 5, 6]
])

print(a + b)
"""
[[ 5  7  9]
 [ 8 10 12]]
"""

# ----
three = np.array([
    [1, 2, 3],
])

four = np.array([
    [4],
    [5],
    [6]
])

print(three + four)
"""
[[5 6 7]
 [6 7 8]
 [7 8 9]]
"""
