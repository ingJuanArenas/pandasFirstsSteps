import pandas as pd

df = pd.read_csv("data.csv")
print(df.head(10))
print(df.describe())
print(df.info())
print("El numero de filas duplicadas es: ", df.duplicated().sum())
print("El numero de filas no disponible es: ", df.isna().sum())
df.drop_duplicates(inplace=True)
mean = df["price"].mean()
df.fillna({"price": mean}, inplace=True)
#excluding non-numeric columns for correlation
df_n= df.select_dtypes(include=['number'])
print(df_n.corr())
print(df.iloc[20:25, 4:7])
print(df.loc[10:15, ["category", "price"]])