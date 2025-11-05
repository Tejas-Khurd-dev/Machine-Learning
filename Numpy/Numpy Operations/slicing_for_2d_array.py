import numpy as np

arr2 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

# arr[row_start:row_end, col_start:col_end]

print(arr2[1], "\n") # select a single row

print(arr2[:,1], "\n") # select a single column

print(arr2[0:2, 1:3], "\n") # select a sub-matrix

print(arr2[:, :2], "\n") # select all rows, first two columns
