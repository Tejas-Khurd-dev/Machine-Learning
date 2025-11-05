import numpy as np

# astype
float_arr = np.array([1.2, 2.3, 6.8, 5.6])
int_arr = float_arr.astype(int)
print(int_arr)

str_arr = float_arr.astype(str)
print(str_arr)
