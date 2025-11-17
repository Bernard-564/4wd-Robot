import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1+array2, "\n")
print(array1)

array2 = np.array([[4], [5], [6]])
print(array2, "\n")
print(array1 + array2, "\n")  # Broadcasting occurs here

array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([4,4,4])

print(array3, "\n")
print(array3 + array4)  # Broadcasting occurs here