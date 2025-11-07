# np.nan_to_num(arr, posinf = value, neginf = value)
# posinf = positive infinite value, neginf = negative infinte value
# you can set any value, +ve or -ve --> eg:-
# np.nan_to_num(arr, posinf = -11, neginf = 11) 

import numpy as np

arr = np.array([1,2,3, np.inf, 5, -np.inf])
print(np.isinf(arr), "\n")

cleaned_arr1 = np.nan_to_num(arr)
print(cleaned_arr1, "\n")

cleaned_arr2 = np.nan_to_num(arr, posinf=11)
print(cleaned_arr2, "\n")

cleaned_arr3 = np.nan_to_num(arr, posinf=-11, neginf=11)
cleaned_arr3 = cleaned_arr3.astype(int)
print(cleaned_arr3, "\n")