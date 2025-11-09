'''
.loc(row_index, "column_name") = new_value
'''

import pandas as pd

data = {
    "Names": [
        "Harsh", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi",
        "Jagdish", "Raj", "Simran",
        "Kavita", "Manish", "Rekha", "Arjun"
    ],

    "Age": [
        28, 34, 22, 30, 29,
        40, 25, 32,
        27, 38, 26, 31
    ],

    "Salary": [
        50000, 60000, 45000, 52000, 49000,
        70000, 55000, 58000,
        53000, 75000, 47000, 62000
    ],

    "Performance Score": [
        85, 90, 78, 92, 88,
        95, 80, 89,
        91, 87, 82, 93
    ]
}

df = pd.DataFrame(data)
print("Before incrementing salary of Harsh")
print(df[(df["Salary"] == 50000) & (df["Names"] == "Harsh" )])

df.loc[0, "Salary"] = 55000 
print("\nAfter incrementing salary of Harsh")
print(df[(df["Salary"] == 55000) & (df["Names"] == "Harsh" )])
 