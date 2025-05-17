import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('day.csv')
# Histogram
df[['temp', 'hum', 'windspeed']].hist(bins=30, figsize=(10, 6))

# Pie chart: % of rental counts by season
season_counts = df.groupby('season')['cnt'].sum()
season_counts.plot.pie(autopct='%1.1f%%')

# Boxplot
sns.boxplot(data=df, x='season', y='cnt')

# Scatter plot
sns.scatterplot(data=df, x='temp', y='cnt')

# Loop-generated plots
cols = ['temp', 'hum', 'windspeed']
for col in cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
