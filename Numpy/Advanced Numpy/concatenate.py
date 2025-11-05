'''
np.concatenate((array1, arrray2), axis = 0)
--> Passing arrays as tuple

axis = 0 --> vertical stacking
axis = 1 --> horizontal stacking
'''

import numpy as np

arr1 = np.array([1,2])
arr2 = np.array([3,4])
concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr, "\n")


arr1 = np.array([[1, 2]])
arr2 = np.array([[3, 4]])
concatenated_arr = np.concatenate((arr1, arr2), axis=0)
print(concatenated_arr, "\n")