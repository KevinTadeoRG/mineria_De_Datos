import pandas as pd

df = pd.read_csv('day.csv')
print(df.info())
print(df.describe())
print(df.nunique())


# Group by example
grouped = df.groupby('weekday')[['casual', 'registered', 'cnt']].mean()
print(grouped)
