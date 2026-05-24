import pandas as pd
import os
import matplotlib.pyplot as plt

# CONFIGURACIÓN DE RUTAS RELATIVAS:

# Se obtiene el directorio donde se está ejecutando el script.
# Esto garantiza que el código sea independiente de dónde se llame.
base_dir = os.getcwd()

# Desde la carpeta raíz -analisis-climatico-, la ruta a los datos es directa.
# Se utiliza el archivo 'annual.csv' sugerido por la cátedra.
relative_path = os.path.join(base_dir, 'datos', 'annual.csv')

# Si la ejecución del script ocurre dentro de 'scripts', se ajusta la ruta retrocediendo un nivel.
if 'scripts' in base_dir:
    relative_path = os.path.join(os.path.dirname(base_dir), 'datos', 'annual.csv')

print(f"La ruta relativa al archivo es: {relative_path}")


# CARGAR DATOS Y CALCULAR INDICADORES:

# Se lee el archivo CSV utilizando pandas. read_csv()
# permite cargar los datos tabulares del archivo en un DataFrame.
df_clima = pd.read_csv(relative_path)

# Se verifica la columna 'Mean' (que contiene las temperaturas en este dataset) para asegurar que los valores sean numéricos.
# El método `pd.to_numeric` convertirá la columna, se utiliza `errors='coerce'` para que cualquier dato corrupto
# o texto se reemplace con `NaN` (Not a Number), evitando errores en la ejecución.
df_clima['Mean'] = pd.to_numeric(df_clima['Mean'], errors='coerce')

# Se calcula la temperatura promedio de la columna 'Mean'.
# El método `.mean()` obtiene la media aritmética de la serie,
# lo cual proporciona el valor central de las anomalías térmicas registradas.
temperatura_promedio = df_clima['Mean'].mean()

# Se calcula la temperatura máxima de la columna 'Mean'.
# El método `.max()` devuelve el valor más alto de la serie,
# permitiendo detectar los picos extremos en el historial.
temperatura_maxima = df_clima['Mean'].max()

# Se calcula la temperatura mínima de la columna 'Mean'.
# El método `.min()` devuelve el valor más bajo,
# permitiendo identificar los puntos de enfriamiento registrados en el dataset.
temperatura_minima = df_clima['Mean'].min()

# Se imprimen los resultados en pantalla para la verificación inicial:
print(f"\nTemperatura Promedio: {temperatura_promedio:.2f}°C")
print(f"Temperatura Máxima: {temperatura_maxima:.2f}°C")
print(f"Temperatura Mínima: {temperatura_minima:.2f}°C")


# GRAFICADO Y GUARDADO DE RESULTADOS

# Se define la ruta de la carpeta de resultados en base al directorio raíz.
ruta_resultados = os.path.join(base_dir, 'resultados')
if 'scripts' in base_dir:
    ruta_resultados = os.path.join(os.path.dirname(base_dir), 'resultados')

# Se verifica que la carpeta '/resultados' exista.
# Se utiliza `os.makedirs` con `exist_ok=True` para la creación de la carpeta; 
# si ya existe, evita la generación de excepciones en el código.
os.makedirs(ruta_resultados, exist_ok=True)

# Se crea una figura con `plt.figure`.
plt.figure(figsize=(10, 6))

# Se utiliza `plt.plot` para generar un gráfico de líneas y representar la serie temporal, 
# evaluando la evolución de la temperatura (Eje Y: Mean) a lo largo de los años (Eje X: Year).
plt.plot(df_clima['Year'], df_clima['Mean'], color='darkred', linestyle='-', linewidth=1.5)

# Se añaden títulos y etiquetas en los ejes con `plt.title`, `plt.xlabel` y `plt.ylabel`
# cumpliendo con los estándares de documentación exigidos.
plt.title('Evolución de la Temperatura Global en el Tiempo')
plt.xlabel('Año')
plt.ylabel('Temperatura Media / Anomalía (°C)')

# Se agrega una cuadrícula de fondo con `plt.grid(True)` para facilitar la lectura del gráfico.
plt.grid(True, linestyle='--', alpha=0.6)

# Nombre del archivo final.
ruta_grafico = os.path.join(ruta_resultados, 'gráfico_resultados.png')

# Se guarda el gráfico en formato PNG.
plt.savefig(ruta_grafico, bbox_inches='tight')

print(f"\nGráfico generado con éxito y guardado en: {ruta_grafico}")
