'''
If you want to know the number of rows, columns, data types, and whether any values are missing, use the .info() method

.info() tells us about total row, column, what data is present in each column eg: int64, float64 and object
then it tells us non null counts and memory usage of the dataframe

here object mean --> string or categorical data

basically it give summary of dataset
'''

import pandas as pd

df = pd.read_csv("Pandas\Read Files\sales_data_sample.csv", encoding="latin1")

print("Displaying the info of 1st data set")
print(df.info())

print("\nDisplaying the info of 2nd data set")
df = pd.read_csv("Pandas\Write and Save Data\save_output.csv")
print(df.info())