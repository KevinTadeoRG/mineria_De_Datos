from statsmodels.tsa.ar_model import AutoReg
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('day.csv') 
df['dteday'] = pd.to_datetime(df['dteday'])
df.set_index('dteday', inplace=True)
df = df.asfreq('D')  # <- Añade la frecuencia diaria explícitamente

# Modelo y pronóstico
model = AutoReg(df['cnt'], lags=30).fit()
forecast = model.predict(start=len(df), end=len(df)+30)

# Graficar resultado
forecast.plot()
plt.title("30-Day Forecast of Rentals")
plt.xlabel("Date")
plt.ylabel("Count")
plt.grid(True)
plt.show()
