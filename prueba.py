import pandas as pd
import numpy as np

# Crear DataFrame vacío
df = pd.DataFrame()

# Función para marcar una celda con el número
def marcar_celda(fila, columna, numero):
    global df
    df.at[fila, columna] = numero

# Ciclo para pedir números y marcar las celdas correspondientes
while True:
    numero_str = input("Ingrese un número (o presione Enter para terminar): ")
    if numero_str == "":
        break
    numero = int(numero_str)
    marcar_celda(numero, "1", "X")
    marcar_celda(numero, "2", "X")
    marcar_celda(numero, "3", "X")

# Reemplazar los valores NaN por los números faltantes
max_num = df.index.max()
df = df.reindex(np.arange(max_num+1))
df = df.fillna(" ")

# Imprimir el DataFrame en la consola
print(df)
