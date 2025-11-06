import numpy as np

arr_2d = np.array([[1,2,3], [4,5,6]]) # --> shape(2,3)
vector_arr = np.array([10,20,30]) # --> shape(3)

result_arr =  arr_2d + vector_arr
print(result_arr)