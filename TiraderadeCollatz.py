# Variables
numero = 6

contador = 0
lista_numero = []

# Collatz
print ("numero: " + str(numero))

while numero >= 2:
  if numero % 2 == 0:
    numero = numero / 2
    contador +=1
    lista_numero.append(numero)

  else:
    numero = (numero * 3) + 1
    contador +=1
    lista_numero.append(numero)
  
  
  
  
  #Hago un clear para hacer un bucle de crear y crear mas listas con diferentes numeros.
  

print ("longitud del numero: " + str(contador-3))
print (lista_numero)
lista_numero.clear

    