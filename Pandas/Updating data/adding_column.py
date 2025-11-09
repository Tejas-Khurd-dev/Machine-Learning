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
print(df)

df["Bonus"] = df["Salary"] * 10/100
print("\nAftert adding 10% Bonus:- \n",df)


# Using insert() method --> to add column at specific position
# df.insert(location, "column_name", some_data )
df.insert(0, "Employee Id", ["CB1012", "CB1056", "CB1512", "CB3412","CB1452","CB3421","CB2367","CB7853","CB2312","CB1212","CB1134","CB3454",])

print("\nAftert adding employee Id:- \n",df)
