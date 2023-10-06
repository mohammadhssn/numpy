"""
    https://numpy.org/doc/1.26/reference/generated/numpy.linspace.html#numpy-linspace
"""

import numpy as np

print(np.linspace(1, 99, 40, retstep=True))
"""
(array([ 1.        ,  3.51282051,  6.02564103,  8.53846154, 11.05128205,
       13.56410256, 16.07692308, 18.58974359, 21.1025641 , 23.61538462,
       26.12820513, 28.64102564, 31.15384615, 33.66666667, 36.17948718,
       38.69230769, 41.20512821, 43.71794872, 46.23076923, 48.74358974,
       51.25641026, 53.76923077, 56.28205128, 58.79487179, 61.30769231,
       63.82051282, 66.33333333, 68.84615385, 71.35897436, 73.87179487,
       76.38461538, 78.8974359 , 81.41025641, 83.92307692, 86.43589744,
       88.94871795, 91.46153846, 93.97435897, 96.48717949, 99.        ]), 2.5128205128205128)
"""

# ----------------------------------------------------------------
l = [i * i for i in range(1, 11)]
print(np.fromiter(iter=l, dtype=np.int8))  # [  1   4   9  16  25  36  49  64  81 100]
# ----------------------------------------------------------------
print(np.fromstring('1,2,3,4,5,6', dtype=np.int8, sep=','))  # [1 2 3 4 5 6]
# ----------------------------------------------------------------
print(np.radians(360))  # 6.283185307179586
print(np.degrees(6.283185307179586))  # 360.0
