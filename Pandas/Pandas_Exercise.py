import pandas as pd
pd.options.display.max_rows

#doc file csv
data = pd.read_csv("Data_for_Pandas.csv")


#doc file json
# j = pd.read_json("data.json")
# print(j.to_string())

# xoa cac dong co chua gia tri null
new_data = data.dropna()

# xoa cac o chua gia tri null trong cot Calories
data.dropna(subset=["Calories"],inplace=True)

# replace empty values
data["Calories"].fillna(round(data["Calories"].mean(),3),inplace=True)
data["Duration"].fillna(data["Duration"].median(),inplace=True)
data["Pulse"].fillna(data["Pulse"].mode(),inplace=True)

# update invalid values
for x in data.index:
    if data.loc[x,"Duration"] >60:
        data.loc[x,"Duration"] = 60

# kiem tra cac gia tri trung nhau
data.duplicated()
data.drop_duplicates(inplace=True)

print(data.to_string())


