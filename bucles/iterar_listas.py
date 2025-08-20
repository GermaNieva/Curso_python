#clase de iteracion de listas (bucles)

lista=["dato1","dato2","dato3","dato4"]

for dato in lista:
    print(dato)
    
# bucles con una lista de numeros
numeros=[1,2,3,4,5]
for numero in numeros:
    numero*2
    print(numero*2)
    
    
# iterando dos listas al mismo tiempo
nombres=["juan","maria","pedro"]
apellidos=["perez","lopez","garcia"]
for nombre, apellido in zip(nombres, apellidos):
    print(f"{nombre} {apellido}")
    
#estas deben tener la misma cantidad de elementos para que no se salte ninguno

#iterando con range  #esta es una forma de iterar usando indices #no es correcto usar esta forma para iterar listas
#pero es util para iterar cuando necesitamos el indice del elemento
for i in range(len(lista)):
    print(f"Elemento {i}: {lista[i]}")
    
lista=["dato1","dato2","dato3","dato4"]
    
# iterando con enumerate #esta es una forma de iterar usando indices y el elemento al mismo tiempo
for i, dato in enumerate(lista):
    print(f"Elemento {i}: {dato}")

for num in enumerate(lista):
    indice= num[0]  # El primer elemento de la tupla es el índice
    elemento = num[1]  # El segundo elemento de la tupla es el elemento de la lista
    print(f"Índice: {indice}, Elemento: {elemento}") # Esto imprimirá tuplas con el índice y el elemento, como (0, 'dato1'), (1, 'dato2'), etc.
    
    
#usando el forelse para iterar una lista
for dato in lista:
    if dato == "dato3":
        print("Dato encontrado:", dato)
        break
else:
    print("Dato no encontrado en la lista")
    
# El bloque else se ejecuta si el bucle no se interrumpe con un break
# En este caso, si "dato3" no se encuentra en la lista, se imprimirá "Dato no encontrado en la lista"

#todo lo anterior funciona igual para tuplas.

#iterando conjuntos
conjunto={"dato1","dato2","dato3","dato4"}
for dato in conjunto:
    print(dato)