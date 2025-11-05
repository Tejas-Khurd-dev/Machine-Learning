'''
.ravel() --> view (shallow copy)
.flatten() --> copy (deep copy)
'''

import numpy as np

array_2d = np.array([[1,5,3],[4,8,6],[7,4,10]])
print(array_2d.ravel())
print(array_2d.flatten())
