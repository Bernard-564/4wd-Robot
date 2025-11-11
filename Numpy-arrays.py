import numpy as np 

Array = np.arange(16)
Array1 = np.arange(1,16)
Array2 = np.arange(1,16,2)
Array3 = np.arange(16).reshape(4,4)


'''print(Array)
print(Array1)
print(Array2)
print(Array3)'''

# arrays from lists
from_list = np.array([1,2,3,4,5])
#print(type(from_list[0]))
#print(from_list)

# 2d array
from_list = np.array([[1,2,3,4,5],[1,4,9,16,25]])
array_2d = np.array((np.arange(25,100,5), np.arange(20,95,5)))
print("1D Shape:", Array2.shape)
print("2D Shape:", from_list.shape)

#empty arrays
empty_array = np.zeros((4,4))
empty_array = np.ones((4,4))
empty_array = np.empty((2,2))
#print(empty_array)


eye_array = np.eye(4, k=-1)
eye_array[eye_array == 0] = 4
eye_array[eye_array < 2] = 9
eye_array[3:] = 7
#eye_array[:2] = 8
eye_array[2:, :2] = 6
print(eye_array, "\n")

sorted_array = np.sort(eye_array, axis=0)
print(sorted_array)

#copying arrays
array_copy = eye_array.copy()
array_view = eye_array.view()
print(array_copy)