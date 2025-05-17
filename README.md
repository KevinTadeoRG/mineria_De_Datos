# mineria_De_Datos

# 📊 Proyecto de Análisis de Datos: Bike Sharing Dataset

Este proyecto cubre el flujo completo de análisis de datos usando el dataset de uso de bicicletas compartidas. Se han implementado técnicas de limpieza, visualización, estadística, modelado y análisis de texto.

## 🔢 1. Limpieza de Datos

- Dataset: [Bike Sharing Dataset - UCI](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)
- Archivo usado: `day.csv`
- Filtrado y validación de:
  - Variables numéricas: `temp`, `hum`, `windspeed`, `cnt`
  - Variables alfanuméricas: `weekday`, `season`
  - Fechas: `dteday`
  - Más de 17,000 filas

## 📊 2. Estadísticas Descriptivas

- Se analizan distribuciones, medias y valores únicos.
- Agrupamiento por entidad (`weekday`, `season`) para entender patrones.
- Se define un diagrama de relaciones entre entidades.

## 📈 3. Visualización de Datos

Se generaron diferentes tipos de gráficos:
- Histogramas
- Diagramas de torta (pie charts)
- Boxplots
- Diagramas de dispersión (scatter plots)
- Visualizaciones en bucle (`for`) sobre columnas numéricas

## 🧪 4. Pruebas Estadísticas

- Se usó **ANOVA** y **Kruskal-Wallis** para comparar el uso entre temporadas (`season`).
- Resultado: diferencias estadísticamente significativas entre grupos.

## 📐 5. Modelos Lineales y Correlación

- Modelo de regresión lineal con variables: `temp`, `hum`, `windspeed`
- Métrica: **R² Score**
- Se genera gráfica de predicciones vs valores reales

## 🔍 6. Clasificación de Datos

- Modelo: **k-Nearest Neighbors (kNN)**
- Clasificación binaria: alta vs baja demanda
- Métrica: exactitud (accuracy)

## 🔀 7. Agrupamiento (Clustering)

- Modelo: **k-Means**
- Agrupamiento de días según condiciones meteorológicas
- Visualización de clusters

## 📆 8. Pronóstico (Forecasting)

- Modelo de series temporales con regresión autoregresiva (AutoReg)
- Predicción de uso de bicicletas para los próximos 30 días

## ☁️ 9. Análisis de Texto

- Generación de nube de palabras (**Word Cloud**) usando nombres de los días (`weekday`)

---

## ⚙️ Requisitos

- Python 3.x
- Bibliotecas:
  - pandas
  - matplotlib
  - seaborn
  - sklearn
  - scipy
  - statsmodels
  - wordcloud

```bash
pip install pandas matplotlib seaborn scikit-learn scipy statsmodels wordcloud
