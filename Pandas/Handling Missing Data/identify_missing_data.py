'''
NaN (Not a number)
None (for object data types)

isnull()
True --> Value is missing
False --> Value is present

isnull().sum --> for total number of missing values
'''

import pandas as pd

data = {
    "Names": [
        "Harsh", "Shyam", None, "Dhanshyam", "Aditi",
        "Jagdish", "Raj"
    ],

    "Age": [
        28, 34, None, 30, 29,
        40, 25
    ],

    "Salary": [
        50000, 60000, None, 52000, 49000,
        70000, 55000
    ],

    "Performance Score": [
        85, 90, None, 92, 88,
        95, 80
    ]
}

df = pd.DataFrame(data)
print(df, "\n")
print(df.isnull(), "\n")
print(df.isnull().sum())

 