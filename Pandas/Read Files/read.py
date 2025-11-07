import pandas as pd

# read data from file to dataframe

# df = pd.read_csv("Pandas\sales_data_sample.csv", encoding="latin1") #csv --> comma separated value
# If encoding fail use your own by adding it separatly in function
# There are two types of encoding "utf-8" and "latin1"

# df = pd.read_excel("Pandas\SampleSuperstore.xlsx")

df = pd.read_json("Pandas\sample_Data.json")
print(df)