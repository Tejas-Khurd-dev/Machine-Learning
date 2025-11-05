'''
vertically stacking
vstack(arr1,arr2,arr3,....) --> row wise

horizontally stacking
hstack(arr1,arr2,arr3,....) --> column wise
'''

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([8, 7, 2])

vstack_arr = np.vstack((arr1, arr2, arr3))
hstack_arr = np.hstack((arr1, arr2, arr3))

print(vstack_arr, "\n")  
print(hstack_arr, "\n")