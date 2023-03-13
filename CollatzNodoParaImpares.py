#Variables
counter_3 = 0
number_3 = 0
pared= 0
limite_3 = 0
camino = 0
caminosPosibles = []
caminosNoPosibles = []

#Collatz
while counter_3 <= 1000:
  if number_3%2 == 0:
    print ("")
    counter_3 = counter_3 + 1
    number_3 = number_3 + 1
  else:
    if (number_3 -1)%3 == 0 :
      print (number_3)
      camino = camino + 1
      caminosPosibles.append(number_3)
    else: 
      pared = pared + 1
      caminosNoPosibles.append(number_3)
      
    counter_3 = counter_3 + 1
    number_3 = number_3 + 1
    
#Outpus
print ("caminos posibles")
print(camino)
print ("Numeros con caminos posibles")
print(caminosPosibles)
print("no tienen camino")
print(pared - 1)
print ("Numeros sin salida")
print(caminosNoPosibles)