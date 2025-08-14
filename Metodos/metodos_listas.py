# Metodos de listas

lista = [1, 2, 3, 4, 5]

cantidad_elementos = len(lista)  # Longitud de la lista
print("Cantidad de elementos en la lista:", cantidad_elementos)

#agregando elementos a la lista
lista.append(6)  # Agrega un elemento al final de la lista
print("Lista después de agregar un elemento:", lista)

lista.extend([7, 8])  # Agrega varios elementos al final de la lista
print("Lista después de extenderla:", lista)

lista.insert(0, 0)  # Inserta un elemento en una posición específica
print("Lista después de insertar un elemento en la posición 0:", lista)

# eliminando elementos de la lista
lista.pop()  # Elimina el último elemento de la lista
print("Lista después de eliminar el último elemento:", lista)
lista.remove(3)  # Elimina el primer elemento con el valor especificado
print("Lista después de eliminar el elemento 3:", lista)
del lista[0]  # Elimina el elemento en la posición especificada
print("Lista después de eliminar el elemento en la posición 0:", lista)

#eliminar todos los elementos de la lista
lista.clear()  # Elimina todos los elementos de la lista
print("Lista después de limpiarla:", lista)
# lista ahora está vacía

lista = [1, 2, 3, 4, 5]  #recreamos la lista

lista.sort()  # Ordena la lista en orden ascendente
print("Lista ordenada en orden ascendente:", lista)
lista.sort(reverse=True)  # Ordena la lista en orden descendente
print("Lista ordenada en orden descendente:", lista)

lista.reverse()  # Invierte el orden de los elementos en la lista
print("Lista después de invertir el orden:", lista)

indice = lista.index(4)  # Encuentra el índice del primer elemento con el valor especificado
print("Índice del elemento 4 en la lista:", indice)


