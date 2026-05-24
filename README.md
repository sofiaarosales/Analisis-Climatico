# Proyecto: Análisis de Datos Climáticos

Trabajo Práctico: Organización Empresarial - UTN TUP

## Integrantes
* Sofía Rosales - P1 (Líder y Organizador)
* Alejandro Abrigo - P2 (Desarrollador Técnico)
* Sofía Rosales - P3 (Revisor y QA)

## Escenario Seleccionado
Escenario A - Análisis de Datos Climáticos.
El proyecto consiste en un script que procesa registros meteorológicos históricos a nivel global. El objetivo es calcular indicadores estadísticos básicos de temperatura (promedio, máxima y mínima) y visualizar su evolución temporal de forma reproducible.

## Dataset
Se utilizó el dataset "Global Temperature Time Series" de DataHub. El archivo annual.csv contiene el registro histórico de anomalías anuales de la temperatura media global en grados Celsius.

## Estructura del Repositorio
* /datos: Directorio para el dataset de origen (annual.csv).
* /scripts: Directorio del código fuente (analisis_datos.py).
* /resultados: Directorio de salida para los gráficos generados por el script.

## Instrucciones de Ejecución
Para reproducir el análisis, clonar el repositorio, ubicarse en el directorio raíz y ejecutar el script principal:

```bash
git clone [https://github.com/sofiaarosales/Analisis-Climatico.git](https://github.com/sofiaarosales/Analisis-Climatico.git)
cd Analisis-Climatico
python3 scripts/analisis_datos.py
