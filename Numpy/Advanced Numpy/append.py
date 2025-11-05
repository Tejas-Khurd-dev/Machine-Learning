import numpy as np
print(".....................For 1d array.........................\n")
arr1 = np.array([1,2,3,4,5])
new_arr1 = np.append(arr1, [3,4])

print(new_arr1, "\n")


print(".....................For 2d array.........................\n")
arr2 = np.array([
                [10, 20, 30],
                [40, 50, 60]
                ])
print("2d row \n", arr2, "\n")
new_arr2_row = np.append(arr2, [[70, 80, 90]], axis=0)
print("Append row:\n", new_arr2_row, "\n")

new_arr2_col = np.append(arr2, [[100], [200]], axis=1)
print("Append column:\n", new_arr2_col, "\n")