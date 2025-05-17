import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Cargar los datos
df = pd.read_csv('day.csv')

# Mapear la columna 'season' a nombres legibles
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
df['season_name'] = df['season'].map(season_map)

# Verificar si hay datos válidos
if df['season_name'].dropna().empty:
    print("No hay datos válidos en la columna 'season_name'.")
else:
    # Unir todas las estaciones como texto
    text = ' '.join(df['season_name'])

    # Generar la nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Mostrarla
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Nube de palabras para la columna 'season'")
    plt.show()
