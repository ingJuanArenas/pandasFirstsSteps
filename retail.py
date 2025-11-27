import pandas as pd

df = pd.read_csv("data.csv")
print(df.head(10))
print(df.describe())
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


df['Discounted_price'] = df['price'].apply(lambda x : x*0.9 if x>650 else x) 
print(df.head(10))

df['date'] = pd.to_datetime(df['date'])
print(df.info())



def stablish_Season(row)-> str:
    month = row['date'].month
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'
    
df['Season'] = df.apply(stablish_Season, axis=1)
print(df.iloc[36:50])


city_stats= df.groupby('city')
category_stats= df.groupby('category')

print(city_stats['price'].agg(['mean', 'sum', 'max', 'min']))
print(category_stats['price'].agg(['mean', 'sum', 'max', 'min']))


# the 3 firsts cities with high sales
top_cities = city_stats['price'].sum().sort_values(ascending=False).head(3)
print("Top 3 cities with highest sales:", top_cities)

top_Day = df.groupby('date')['order_id'].count().sort_values().head(5)
print("Day with highest number of orders:",top_Day)


errors = df[df['total'] != df['quantity'] * df['price']]
print(errors)