import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('day.csv')  # 👈 Asegúrate que esté en la misma carpeta

kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(df[['temp', 'hum', 'windspeed']])
print("Clusters:", clusters)
