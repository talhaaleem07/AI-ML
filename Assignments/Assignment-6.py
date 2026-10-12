import numpy as np
from numpy import random

# NumPy Creating Arrays

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

arr = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [1, 2, 3]]])
print(arr)

# Check how many dimensions the arrays have:

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# NumPy Array Indexing

# Access the third element of the second array of the first array:

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# Print the last element from the 2nd dim:

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# NumPy Array Slicing

# Slice elements from index 4 to the end of the array:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

# Slice from the index 3 from the end to index 1 from the end:

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

# Data Types in Python

# Change data type from float to integer by using 'i' as parameter value:

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# NumPy Array Copy 

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# NumPy Array Shape

# Print the shape of a 2-D array:

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# NumPy Array Reshaping

# Convert the following 1-D array with 12 elements into a 2-D array.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Convert the following 1-D array with 12 elements into a 3-D array.s

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

# Convert the array into a 1D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

# NumPy Array Iterating

# Iterate on the elements of the following 2-D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

# Iterate on each scalar element of the 2-D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

# NumPy Joining Array

# Join two arrays

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Join two 2-D arrays along rows (axis=1):

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# NumPy Splitting Array

# Split the array in 3 parts:

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# Access the splitted arrays:

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# Split the 2-D array into three 2-D arrays.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

# NumPy Searching Arrays

# Find the indexes where the value is 4:

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Find the indexes where the values are odd:

arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr%2 == 1)
print(x)

# NumPy Sorting Arrays

# Sort the array:

arr = np.array([3, 2, 4, 1, 5])
print(np.sort(arr))

# Sort the array alphabetically:

arr = np.array(['z', 'a', 'c', 'b'])
print(np.sort(arr))

# Sort a 2-D array:

arr = np.array([[3, 2, 4], [1, 5, 6]])
print(np.sort(arr))

# NumPy Random Numbers 

# Generate a 1-D array containing 5 random integers from 0 to 100:

arr = np.random.randint(0, 100, 5)
print(arr)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

arr = np.random.randint(0, 100, (3, 5))
print(arr)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:

x = np.random.rand(3, 5)
print(x)
