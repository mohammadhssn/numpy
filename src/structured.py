"""
    https://numpy.org/doc/1.26/user/basics.rec.html
"""

import numpy as np

names = np.array(['mohammadhssn', 'sara', 'kevin'])
ages = np.array([24, 25, 26])

na = np.zeros(
    3,
    # dtype={'names': ('names', 'ages'), 'formats': ('U10', 'i4')},
    dtype={'names': ('names', 'ages'), 'formats': ((np.str_, 15), np.int8)}
)
na['names'] = names
na['ages'] = ages
print(na)  # [('mohammadhs', 24) ('sara', 25) ('kevin', 26)]
print(na[0]['names'])  # mohammadhssn
print(na[na['ages'] > 25])  # [('kevin', 26)]
