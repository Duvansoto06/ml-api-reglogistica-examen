# ===============================
# DATA UNDERSTANDING (CRISP-DM)
# ===============================

# Importamos librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
# Cargar el dataset

df = pd.read_csv("data/estudiantes_examen.csv")

# Mostrar las primeras filas
# Esto permite ver cómo vienen los datos (estructura y valores)
print(df.head())

# ===============================
# DESCRIPCIÓN GENERAL DE LOS DATOS
# ===============================

# describe() muestra estadísticas básicas:
# - count: cantidad de datos
# - mean: promedio
# - std: desviación estándar
# - min/max: valores extremos
# - percentiles: distribución
print(df.describe())


# ===============================
# DISTRIBUCIÓN DE HORAS DE ESTUDIO
# ===============================

# Histograma: muestra cuántos estudiantes hay en cada rango de horas
df['HorasEstudio'].hist()

# Título del gráfico
plt.title("Distribución de Horas de Estudio")

# Etiquetas
plt.xlabel("Horas de Estudio")
plt.ylabel("Cantidad de Estudiantes")

# Mostrar gráfico
plt.show()


# ===============================
# ANÁLISIS POR RESULTADO
# ===============================

# Agrupar por Resultado (Si / No)
# count() cuenta cuántos registros hay por cada grupo
resultado_count = df.groupby('Resultado').count()

print(resultado_count)