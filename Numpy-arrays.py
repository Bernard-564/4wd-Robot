import numpy as np 

Array = np.arange(16)
Array1 = np.arange(1,16)
Array2 = np.arange(1,16,2)
Array3 = np.arange(16).reshape(4,4)

"""print(Array)
print(Array1)
print(Array2)
print(Array3)"""

# arrays from lists
from_list = np.array([[1,3,5,7],[0,2,4,6]])
D2matrix = (from_list.reshape(2,2,2))
#print(type(from_list[0]))
#print(from_list)
print(D2matrix)
print(D2matrix.shape)