# np.isinf(array)
# It is use to handle large numbers such as 10^1000 
# and illegal operation: 1/0

import numpy as np

arr = np.array([1,2,3, np.inf, 5, -np.inf])
print(np.isinf(arr))