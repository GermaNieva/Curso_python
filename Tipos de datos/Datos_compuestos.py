#Datos compuestos en Python
# Listas en Python
lista= ["ivi","germán",2,True,1.85]

print(lista[0])  #esto mostrará "ivi"
print(lista[1])  #esto mostrará "germán"

#la posicion 0 es el primer elemento de la lista, la posicion 1 es el segundo elemento, y así sucesivamente.

#tuplas en Python
# las tuplas son similares a las listas, pero son inmutables, lo que significa que no puedes cambiar sus elementos una vez que se han creado.
# Se definen con paréntesis en lugar de corchetes.

tupla= ("ivi","germán",2,True,1.85)
print(tupla[0])  #esto mostrará "ivi"
print(tupla[1])  #esto mostrará "germán"

lista[1]="Iván"  #cambiamos el segundo elemento de la lista
print(lista)  #esto mostrará ['ivi', 'Iván', 2, True, 1.85]

#tupla[1]="Iván"  #esto generará un error, ya que las tuplas son inmutables
#print(tupla)  #esto no se ejecutará debido al error anterior

# Creando un conjunto set en Python
# Los conjuntos son útiles cuando necesitas almacenar elementos únicos y no te importa el orden.
# Se definen con llaves {} o usando la función set().
#ejemplo con set()
conjunto = set(["ivi", "germán", 2, True, 1.85])
print(conjunto)  #esto mostrará los elementos del conjunto en un orden aleatorio
# Los conjuntos son colecciones desordenadas de elementos únicos. Se definen con llaves {}

conjunto= {"ivi","germán",2,True,1.85}
print(conjunto)  #esto mostrará los elementos del conjunto en un orden aleatorio

# Los conjuntos no permiten elementos duplicados, por lo que si intentas agregar un elemento que ya existe, no se añadirá.
conjunto.add("ivi")  #esto no cambiará el conjunto, ya que "ivi" ya está presente
print(conjunto)  #esto seguirá mostrando los mismos elementos

# no se puede acceder a los elementos de un conjunto por índice, ya que no tienen un orden definido.

# Diccionarios en Python
# Los diccionarios son colecciones de pares clave-valor. Se definen con llaves y dos puntos.

diccionario = {
    "nombre": "ivi",
    "apellido": "germán",
    "edad": 2,
    "activo": True,
    "altura": 1.85
}

print(diccionario["nombre"])  #esto mostrará "ivi"
print(diccionario["apellido"])  #esto mostrará "germán"

# Puedes agregar o modificar elementos en un diccionario usando su clave.
#se puede acceder a los valores del diccionario usando las claves entre corchetes.
diccionario["edad"] = 2  #cambiamos la edad a 2
diccionario["edad"] = 3  #cambiamos la edad a 3 

print(diccionario["edad"])  #esto mostrará 3
print(diccionario)  #esto mostrará el diccionario actualizado

# Puedes agregar un nuevo par clave-valor al diccionario.
diccionario["nacionalidad"] = "Colombiana"  #agregamos una nueva clave "nacionalidad"
print(diccionario["nacionalidad"])  #esto mostrará "Colombiana"
