#Variables
lista = []

a = "a"

c = 0

b = 0

#Explicacion del codigo
print("Este programa ejecutara todas las secuencias de collatz que introduzacas")
print("Para introducir un numero, pones el mismo y luego apretas espacio y asi sucesiva mente")
print("Una vez hayas acabado pondras un asterisco '#' y se te mostraran todas las cadenas de numeros que querias consultar")


#Bucle para confirmar si se ha introducido el #
while a != "#":

    a = input()

    c += 1

    lista.append(a)

lista.pop(-1) #Eliminar el # de la lista de elementos

#Ir uno a uno los elementos de la lista
for numero in lista:
    contador = 0
    lista_numero = []

    # Aplicar Collatz
    print(" ")
    print ("numero: " + str(numero))

    while int(numero) >= 2:
        if int(numero) % 2 == 0:
            numero = int(numero) / 2
            contador +=1
            lista_numero.append(numero)

        else:
            numero = (int(numero) * 3) + 1
            contador +=1
            lista_numero.append(numero)
    
    
    #Salida de la estructura de collatz
    print ("longitud del numero: " + str(contador-3))
    print (lista_numero)
    lista_numero.clear()#Clear para hacer un bucle de crear y crear mas listas con diferentes numeros.

#Salida final del programa
    
print(" ")

print("Numeros intrducidos:")

print(lista)