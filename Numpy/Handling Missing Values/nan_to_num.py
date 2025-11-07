# np.nan_to_num(array, nan=value) --> default value is  
# Give result in float so if you want you can convert it into int

import numpy as np

arr = np.array([1,2,3, np.nan, 5, np.nan])
cleaned_arr1 = np.nan_to_num(arr)
cleaned_arr1 = cleaned_arr1.astype(int)
print(cleaned_arr1)

cleaned_arr2 = np.nan_to_num(arr, nan=11)
cleaned_arr2 = cleaned_arr2.astype(int)
print(cleaned_arr2)