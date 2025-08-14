# Metodos de Diccionarios

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

claves = diccionario.keys() #el metodo keys devuelve las claves del diccionario
valores = diccionario.values()

def imprimir_diccionario(dic):
    for clave, valor in dic.items():
        print(f"{clave}: {valor}")
        
imprimir_diccionario(diccionario)

#metodo get devuelve el valor de una clave especifica
print(diccionario.get("nombre"))  # Juan
print(diccionario.get("pais", "No encontrado"))  # No encontrado

#metodo pop elimina una clave y devuelve su valor
valor_eliminado = diccionario.pop("edad")

#metodo clear elimina todos los elementos del diccionario
diccionario.clear()
print(diccionario)  # {}

#metodo items devuelve una lista de tuplas con las claves y valores
def imprimir_items(dic):
    for item in dic.items():
        print(item)
        
imprimir_items({"a": 1, "b": 2, "c": 3})
