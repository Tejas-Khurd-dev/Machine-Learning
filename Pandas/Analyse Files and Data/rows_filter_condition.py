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

high_salary = df[df["Salary"] > 50000]

print("\nEmployees with salary greater than 50000")
print(high_salary)

print("\nEmployees with salary greater than 50000 and age greater than 30")
print(df[(df["Salary"] > 50000) & (df["Age"] > 30)])

print("\nEmployees with performance score greater than 90 or age greater than 35")
print(df[(df["Age"] > 35) | (df["Performance Score"] > 90)])
