import pandas as pd

df = pd.read_csv("data.csv")
##inplace is used to modify the original dataframe without creating a copy
df.dropna(inplace= True)
## get the mean
mean = df["Age"].mean()
## replace empty values with mean
df.fillna({"Age":mean}, inplace=True)
print(df.head())
print(df.describe())
print(df.info())
print(df.duplicated())
df.corr()