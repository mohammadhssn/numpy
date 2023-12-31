# https://numpy.org/doc/1.26/reference/routines.array-creation.html
import numpy as np

one = np.empty(shape=(3, 4), dtype=np.int8)
print(one)

like = ([1, 2, 3], [4, 5, 6])
print(np.empty_like(prototype=like, shape=(3, 2)))

# ----------------------------------------------------------------

print(np.eye(4, 5, 2))
"""
[[0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]
 [0. 0. 0. 0. 0.]]
"""
# ----------------------------------------------------------------
print(np.identity(4))
"""
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
"""
# ----------------------------------------------------------------
print(np.ones(shape=(2, 3)))
"""
[[1. 1. 1.]
 [1. 1. 1.]]
"""
# ----------------------------------------------------------------
print(np.zeros(shape=(2, 3)))
"""
[[0. 0. 0.]
 [0. 0. 0.]]
"""
# ----------------------------------------------------------------
print(np.full(shape=(3, 3), fill_value=7))
"""
[[7 7 7]
 [7 7 7]
 [7 7 7]]
"""
# ----------------------------------------------------------------
range_array = np.arange(9, 90)
range_array.reshape((9, 9))
