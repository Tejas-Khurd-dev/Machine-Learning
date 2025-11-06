import numpy as np

arr_2d = np.array([[1,2,3,4], [4,5,6,2]]) # --> shape(2,3)
vector_arr = np.array([10,20]) # --> shape(2)

# result_arr =  arr_2d + vector_arr
# print(result_arr)

arr_2d_reshaped = arr_2d.reshape(4,2)
print(arr_2d_reshaped, "\n")
result_arr =  arr_2d_reshaped + vector_arr
print(result_arr, "\n")