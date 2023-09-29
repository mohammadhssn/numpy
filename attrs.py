import numpy as np

one_dimension = np.array(
    [[11], [22], [33]],
    dtype=np.uint8
)

multi_dimension = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=np.uint8)

# ----------------------------------------------------------------
print(multi_dimension.ndim)  # 2
print(multi_dimension.size)  # 9
print(multi_dimension.shape)  # (3,3)

print(multi_dimension.reshape(1, 9))  # [[1 2 3 4 5 6 7 8 9]]
print(multi_dimension.reshape(9, 1))

print(multi_dimension[0, 2])  # 3
print(multi_dimension[0: 2])  # [[1 2 3] [4 5 6]]
# --------
# print(np.vstack((multi_dimension, one_dimension)))
# print(np.hstack((multi_dimension, one_dimension)))

print(np.concatenate((multi_dimension, one_dimension), axis=1))
# --------
print(np.vsplit(multi_dimension,
                3))  # [array([[1, 2, 3]], dtype=uint8), array([[4, 5, 6]], dtype=uint8), array([[7, 8, 9]], dtype=uint8)]

print(np.hsplit(multi_dimension, 3))
# --------
print(np.sort(multi_dimension))
# --------
new_array = multi_dimension.copy()  # create new array
copy_multi_dimension = multi_dimension.view()  # reference to multi_dimension array

print(copy_multi_dimension.base)
print(new_array.base)  # None
