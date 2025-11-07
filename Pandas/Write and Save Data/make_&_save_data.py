import pandas as pd

data = {
  "name" : ["Tejas", "Aryan", "Raj"],
  "age" : [18, 20, 22],
  "city" : ["Mumbai", "Pune", "Nagpur"]
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("pandas\save_output.csv", index=False) # --> index = False, will not show indexing  eg:- 0, 1, 2

df.to_excel("pandas\save_output.xlsx", index=False)

df.to_json("pandas\save_output.json", index=False)