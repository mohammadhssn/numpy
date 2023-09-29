# https://numpy.org/doc/1.26/reference/routines.io.html
import numpy as np

one = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

np.save('input_output/single_array.npy', one)
# np.savetxt('abc.txt', one)


print(np.load('input_output/single_array.npy'))
# np.loadtxt('abc.txt')

# --------------------------------------------------------
# multi array
two = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

three = np.array([
    [11, 22, 333],
    [44, 55, 66]
])

np.savez('input_output/multy_array.npz', two=two, three=three)

l = np.load('input_output/multy_array.npz')
print(l['two'])
print(l['three'])
