# https://numpy.org/doc/1.26/reference/arrays.html

import numpy as np

zero_dimension = np.array(10)
one_dimension = np.array([1, 2, 3])
multi_dimension = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.uint8)

print(one_dimension.ndim)  # 1
print(multi_dimension.ndim)  # 2
# ----------------------------------------------------------------
print(one_dimension.shape)  # (3,)
print(multi_dimension.shape)  # (2, 3)

# ----------------------------------------------------------------
convert_type = np.array([1, 'mohammadhssn'])
print(convert_type)  # ['1', 'mohammadhssn']
# ----------------------------------------------------------------------------------------------------------------------

# https://numpy.org/doc/1.26/reference/arrays.scalars.html
print(one_dimension.dtype)  # int64
print(multi_dimension.dtype)  # uint8
