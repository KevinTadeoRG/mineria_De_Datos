import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('day.csv') 

df['high_demand'] = (df['cnt'] > df['cnt'].median()).astype(int)
X = df[['temp', 'hum', 'windspeed']]
y = df['high_demand']

X_train, X_test, y_train, y_test = train_test_split(X, y)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

print("KNN Accuracy:", knn.score(X_test, y_test))
