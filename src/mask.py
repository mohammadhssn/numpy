"""
    https://numpy.org/doc/1.26/reference/maskedarray.html
"""

import numpy as np
import numpy.ma as ma

one = np.arange(-3, 5)

one_mask = ma.masked_where(one <= 0, one)  # Negative numbers are masked
print(one_mask)
one_mask2 = ma.masked_values(one, 0)
print(one_mask2)
# ------------------------------------------------------------------
two = np.array(
    [
        [1, 2, 3], [4, np.NAN, 6]
    ]
)

# two_mask = ma.masked_array(two, mask=[0, 0, 0, 0, 1, 0])  # -> np.NaN masked
two_mask = ma.masked_invalid(two)
print(two_mask)
