"""
    https://numpy.org/doc/1.26/reference/routines.sort.html
"""

import numpy as np

surnames = ('Hertz', 'Galilei', 'Hertz')
first_names = ('Sara', 'Kevin', 'Sam')

x = np.array([3, 1, 2, 6, 7, 9, 8, 10])

a = np.array([
    [1, 4, 2],
    [3, 1, 5]
])

# ----------------------------------------------------------------
print(np.sort(a))  # create new array
print(np.sort(a, axis=0))
print(a.sort())  # change order main array (a)

print(np.lexsort((first_names, surnames)))  # [1 2 0] -> 1(Galilei) -> 2(Sam) -> 0(Sara)
print(np.argsort(x))  # [1 2 0 3 4 6 5 7] -> index x

# ------------------------------------------------------------------------------------------------
x_sort = np.sort(x)
print(np.searchsorted(x_sort, 4))  # 3 -> index
print(np.argmax(x))  # 7 -> index
print(np.argmin(x))  # 1 -> index
print(np.extract(np.mod(x, 3) == 0, x))  # [3 6 9]
print(np.nonzero(x > 3))  # (array([3, 4, 5, 6, 7]),) -> index

# -------------------------------------------------------------------------------------------------
print(np.count_nonzero(x > 3))  # -> 5
