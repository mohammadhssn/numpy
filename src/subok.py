"""
    https://numpy.org/doc/1.26/reference/generated/numpy.array.html
"""

import numpy as np
import numpy.ma as ma

one = np.array([1, 2, 3])
two = np.array(one, copy=False)
two[0] = 11
print(one)  # [11, 2, 3]
print(two)  # [11, 2, 3]

# ----------------------------------------------------------------

three = ma.masked_array([1, 2, 3])
four = np.array(three, subok=True)

print(type(three))  # <class 'numpy.ma.core.MaskedArray'>
print(type(four))  # <class 'numpy.ma.core.MaskedArray'>

# ----------------------------------------------------------------

five = np.array([1, 2, 3], ndmin=4)
print(five)  # [[[[1 2 3]]]]

# ----------------------------------------------------------------

six = np.array([
    [1, 2, 3],
    [4, 5, 6]
], order='C')  # C = C  -> order default is C

print(six.itemsize)  # 8
print(six.strides)  # (24, 8)

seven = np.array([
    [1, 2, 3],
    [4, 5, 6]
], order='F')  # F = Fortran
print(seven.itemsize)  # 8
print(seven.strides)  # (8, 16)
