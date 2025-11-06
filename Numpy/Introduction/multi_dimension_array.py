import numpy as np

array_3d = np.array([[[1,2,3], [4,5,6]],[[2,3,4], [5,6,7]], [[3,3,4], [8,6,7]]])
# This is (3,2,3) array as 3 main blocks, 2 rows and 3 columns
print(array_3d)

array_4d = np.array([
    [
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]]
    ],
    [
        [[2, 3, 4], [5, 6, 7]],
        [[8, 9, 10], [11, 12, 13]]
    ]
])

print(array_4d)
# This is (2,2,2,2) array as 2 main blocks, 2 sub-blocks, 2 rows and 3 columns
