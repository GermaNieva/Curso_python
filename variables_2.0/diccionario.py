#Creando diccionarios con dict()

diccionario=dict({"nombre":"juan","edad":30})
print(diccionario)
 #con dict se pueden crrear diccionarios vacios
diccionario_vacio=dict()

#las listas no pueden ser llaves de un diccionario pero las tuplas si
diccionario2={("nombre","apellido"):["juan","perez"],"edad":30}
print(diccionario2)

#si usamos frozenset como llave del diccionario este sera inmutable
diccionario3={frozenset(["nombre","apellido"]):["juan","perez"],"edad":30}
print(diccionario3)

#creandi diccionarios con fromkeys
llaves=["nombre","apellido","edad"]
diccionario4=dict.fromkeys(llaves)
print(diccionario4)

#esto sirve para crear un diccionario con llaves pero sin valores asignados
diccionario5=dict.fromkeys(llaves,"valor por defecto")
print(diccionario5)

#podemos acceder a los valores del diccionario usando las llaves
print(diccionario2["edad"])
print(diccionario2[("nombre","apellido")])
print(diccionario3[frozenset(["nombre","apellido"])])
print(diccionario5["nombre"])