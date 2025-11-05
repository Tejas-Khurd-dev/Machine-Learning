'''
np.delete(array, index, axis = None)
'''

import numpy as np
print(".....................For 1d array.........................\n")
arr = np.array([10, 20, 30, 40, 50, 60])
new_arr = np.delete(arr, 2)

print(new_arr) 


print(".....................For 2d array.........................\n")
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

new_arr = np.delete(arr, 1, axis=1)
# axis = 1 --> for column
# axis = 0 --> for row 
print(new_arr)