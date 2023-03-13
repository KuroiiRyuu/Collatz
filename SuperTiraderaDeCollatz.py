# Variables
c = 4
n = 20
numero = 4
numero_inicial = 4
lista_numero = []

# Collatz
while c <= n:
  print(" ")
  print ("Contador:", str(c), "Numero final del contador:", str(n), "Numero inicial del contador:", str(numero))
  
  while numero >= 4:
    if numero % 2 == 0:
      numero = numero / 2
      lista_numero.append(numero)

    else:
      numero = (numero * 3) + 1
      lista_numero.append(numero)
  print (lista_numero)
  lista_numero.clear() 
  c += 1
  numero_inicial += 1
  numero = numero_inicial  
    
   
  
  
  #Hago un clear para hacer un bucle de crear y crear mas listas con diferentes numeros.
  

    


    