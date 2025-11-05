'''
np.insert(array, index, value, axis=None)
array = original array
index = index position
value = data which want to insert 
axis = None --> for 1d array

.........For 2d array........
axis = 0 --> to insert data in row
axis = 1 --> to insert data in column
'''

import numpy as np
print(".....................For 1d array.........................\n")
arr1 = np.array([1,2,3,4,5])
new_arr1 = np.insert(arr1, 2, 20, axis=None)
# OR --> new_arr = np.insert(arr, 2, 20)
print(arr1, "\n")
print(new_arr1, "\n")


print(".....................For 2d array.........................\n")

arr2 = np.array([[10, 20, 30],
                [40, 50, 60]])

new_arr2 = np.insert(arr2, 0, [100, 200, 300], axis=0)
print(arr2, "\n")
print(new_arr2, "\n")
new_arr2 = np.insert(arr2, 0, [100, 200, 300], axis=None)
print(new_arr2, "\n")