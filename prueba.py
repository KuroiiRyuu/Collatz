import pandas as pd

# Definir los nombres de las columnas
nombres_columnas = ["Columna 1", "Columna 2", "Columna 3"]

# Crear DataFrame vacío con los nombres de las columnas
df = pd.DataFrame(columns=nombres_columnas)

# Función para marcar una celda con "X"
def marcar_celda(fila, columna):
    global df
    df.at[fila, columna] = "X"

# Ciclo para pedir números y marcar las celdas correspondientes
while True:
    numero_str = input("Ingrese un número (o presione Enter para terminar): ")
    if numero_str == "":
        break
    numero = int(numero_str)
    marcar_celda(numero, "Columna 2")

# Imprimir el DataFrame en la consola
print(df)
