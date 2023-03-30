import pandas as pd
import numpy as np

# Variables
c = 4
n = 10
numero = 4
numero_inicial = 4
lista_numero = []

df = pd.DataFrame()

def marcar_celda(fila, columna, numero):
    global df
    df.at[fila, columna] = numero



# Collatz
while c <= n:
  print(" ")
  print ("Contador:", str(c), "Numero final del contador:", str(n), "Numero inicial del contador:", str(numero))
  
  while numero >= 4:
    if numero % 2 == 0:
      numero = numero / 2
      lista_numero.append(numero)
      marcar_celda(numero, c, "X")

    else:
      numero = (numero * 3) + 1
      lista_numero.append(numero)
      marcar_celda(numero, c, "X")
  #print (lista_numero)
  lista_numero.clear() 
  c += 1
  numero_inicial += 1
  numero = numero_inicial  

max_num = df.index.max()
df = df.reindex(np.arange(max_num+1))
df = df.fillna(" ")

# Imprimir el DataFrame en la consola
print(df)
