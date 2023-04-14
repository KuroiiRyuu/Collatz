import os # -> Para poder instalar la hoja de calculo
import pandas as pd # -> Para poder hacer una base de datos donde guardar los numeros
import numpy as np

# Variables
c = 4
n = 40
numero = 4
numero_inicial = 4
lista_numero = []

#Creacion del dataFrame
df = pd.DataFrame()

#Definicion de las filas y las comunas
def marcar_celda(fila, columna, numero):
    global df
    df.at[fila, columna] = numero



# Collatz
while c <= n:
  print(" ")
  print ("Contador:", str(c), "Numero final del contador:", str(n), "Numero inicial del contador:", str(numero))
  
  #Mirar si el numero esta por debajo de 4
  while numero >= 4:
    
    #Mirar si el numero es par
    if numero % 2 == 0:
      numero = numero / 2
      lista_numero.append(numero)
      marcar_celda(numero, c, "X")

    #Se deduce que si el numero no es par, sera impar
    else:
      numero = (numero * 3) + 1
      lista_numero.append(numero)
      marcar_celda(numero, c, "X")
      
  #print (lista_numero)
  lista_numero.clear() 
  c += 1
  numero_inicial += 1
  numero = numero_inicial  

#Almacenamiento de los datos dentro del DataFrame
max_num = df.index.max()
df = df.reindex(np.arange(max_num+1))
df = df.fillna(" ")

#Crear un excel con el DataFrame
print(df)
df.to_excel("output.xlsx", index=False)
