'''
If you want to know how big is your dataset 
and what are the names of the columns

use shape and column attributes
shaper will return tuple with two values consist of no. of rows and no. of columns
column will return names of the columns
'''

import pandas as pd

data = {
    "Name": [
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
print("Shape: ", df.shape, "\n")
print("Columns names: ", df.columns)