# np.isnan(array) # --> nan mean not a number

import numpy as np

arr = np.array([1,2,3, np.nan, 5, np.nan])
print(np.isnan(arr))

# Interview question --> can you compare np.nan with np.nan --> answer is no we can't campare np.nan with np.nan

# print(np.nan == np.nan) 