'''
If you want to select specific row 
and want to filter rows
and cobime multiple conditions

use square bracket to access specific column
and use boolean conditions to filter rows

Selecting columns
column = df["column_Name"] --> return series
columns = df[["column1_Name", "column2_Name",...]] --> return dataframe

Filtering rows
1) Based on single condition:
df = df[df["Salary"] > 50000]
df = df[(df["Salary"] > 50000) & (df["Salary"] < 80000)]
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
        70000, 48000, 58000,
        53000, 75000, 47000, 62000
    ],

    "Performance Score": [
        85, 90, 78, 92, 88,
        95, 80, 89,
        91, 87, 82, 93
    ]
}

df = pd.DataFrame(data)

name_column = df["Names"]
print(name_column)

columns_subset = df[["Names", "Salary"]]
print("\n",columns_subset)
