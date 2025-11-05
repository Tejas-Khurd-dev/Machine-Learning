'''
np.split() --> for equal split

np.hsplit() --> for horizontal split (along columns)

np.vsplit() --> for vertical split (along rows)
''' 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
split_array = np.split(arr, 2)
print(split_array, "\n")

split_array = np.hsplit(arr, 4) 
print(split_array, "\n")


arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8], [2, 1, 4, 5], [7, 8, 5, 6]])
split_array = np.split(arr, 4)
print(split_array, "\n")

split_array = np.hsplit(arr, 2) 
print(split_array, "\n")

split_array = np.vsplit(arr, 4) 
print(split_array, "\n")