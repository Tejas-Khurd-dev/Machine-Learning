# .head() --> print first 5 rows from dataframe
# .tail() --> print last 5 rows from dataframe

# .head(n) --> print first n rows from dataframe
# .tail(n) --> print last n rows from dataframe

import pandas as pd

df = pd.read_csv("Pandas\Read Files\sales_data_sample.csv", encoding="latin1")
print("Display first 10 rows")
print(df.head(10))

print("\nDisplay last 10 rows")
print(df.tail(10))