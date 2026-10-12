# # Numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
zeros = np.zeros((2,3))
print(zeros)

# rand = np.random.randint(1, 10, 5)
# print(rand)

# arr = np.array([5, 3, 7, 2, 1])
# print(arr)

ones = np.ones((2,3))
print(ones)

# rand = np.random.randint([1, 100, 4])
# print(rand)

# Array Attributes (Shapes, dtype, size, ndim)

# a = np.array([1, 2, 3], [4, 5, 6])

# print(a.shape)
# print(a.dtype)
# print(a.size)
# print(a.ndim)

# n = np.array([1, 2, 3], [4, 5, 6, 7])

# print(n.shape)
# print(n.dtype)
# print(n.size)
# print(n.ndim)

# n = np.array([1.0, 2.0, 3.0], [4, 5, 6, 7])

# print(n.dtype)

# Array MEthods (Reshape, max/min, argmax/argmin)

# b = np.aray([3, 7, 1, 9, 4])

# print(b.reshape(5, 1))
# print(b. max(), b.min())
# print(b.argmax(), b.argmin())

# c = np.array([4, 5, 6, 7, 8, 9])
# print(c.reshape(2, 3))

# rand = np.random.randint([1, 100, 8])
# print(c. max(), c.min())
# print(c.argmax(), c.argmin())

# Coping, Appending & Inserting

# c = np.array([1, 2, 3])
# c_copy = c.copy()
# c_copy[0] = 99
# print(c, c_copy)

# d = np.array([1, 2, 3])
# print(np.append(d, [4, 5]))
# print(np.insert(d,1,100))

# c = np.array([1, 2, 3])
# c_copy = c.copy()
# c_copy[0] = 21
# print(c, c_copy)

# d = np.array([1, 2, 3])
# print(np.append(d, [4, 5, 6]))
# print(np.insert(d,2,21))

# Sorting, Deleting, Combining & Splitting

# e = np.array([5, 2, 8, 1])
# print(np.sort(e))
# print(np.delete(e, 0))

# f1, f2 = np.array([1, 2]), np.array([3, 4])
# print(np.concatenate((f1, f2)))
# print(np.array_split(np.arange(1, 7), 3))

# e = np.array([5, 2, 8, 1, 3, 6])
# print(np.sort(e))
# print(np.delete(e, 2))

# f1, f2 = np.array([1, 2, 3]), np.array([4, 5, 6])
# print(np.concatenate((f1, f2)))
# print(np.array_split(np.arange(1, 7), 2))

# Data Loading and Saving

# arr = np.array([1, 2, 3, 4, 5])
# np.save("my_array.npy", arr)
# loaded = np.load("my_array.npy")
# print(loaded)

# Indexing and Selection (2D, Logical)

# g = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(g[1, 2])
# print(g[g > 5])

# g = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# ?

# Broadcasting

# h = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(h + 10)

# h = np.array([1, 2, 3, 4, 5])
# print(h + 100)

# h = np.array([1, 2, 3, 4, 5])
# print(h * 3)
# print(h - 1)

# Type Casting and Arithmetic Operations

# i = np.array([1.5, 2.7, 3.1])
# print(i.astype(int))

# j = np.array([1, 2, 3])
# k = np.array([4, 5, 6])
# print(j + k, j - k, j * k)
# print(j / k, j**2)

# i = np.array([2.5, 3.7, 4.1])
# print(i.astype(int))

# j = np.array([1, 2, 3, 4])
# k = np.array([5, 6, 7, 8])
# print(j + k, j - k, j * k)
# print(j / k, j**2)

# Universal Array Functions (sqrt, exp, sin, etc)

# m = np.array([1, 4, 9, 16])
# print(np.sqrt(m))

# n = np.array([1, 2, 3, 4])
# print(np.exp(n))

# n = np.array([45, 60, 90, 180])
# print(np.sqrt(n))

# n = np.array([45, 60, 90, 180])
# print(np.sin(n))
