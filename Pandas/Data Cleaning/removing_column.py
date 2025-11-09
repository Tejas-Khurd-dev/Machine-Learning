''' 
.drop(columns = ["Column_Name"], inplace = True)
'''
import pandas as pd

data = {
    "Names": [
        "Harsh", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi",
        "Jagdish", "Raj"
    ],

    "Age": [
        28, 34, 22, 30, 29,
        40, 25
    ],

    "Salary": [
        50000, 60000, 45000, 52000, 49000,
        70000, 55000
    ],

    "Performance Score": [
        85, 90, 78, 92, 88,
        95, 80
    ]
}
df = pd.DataFrame(data)
print("Modified dataframe (removed performance score and age columns)")
# df.drop(columns = ["Performance Score"], inplace = True)
# above example was for single column

df.drop(columns = ["Performance Score", "Age"], inplace = True)
# above example was for multiple column
print(df)
