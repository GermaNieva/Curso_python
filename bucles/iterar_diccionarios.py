#iterar diccionarios
diccionario={"nombre":"juan","edad":30,"ciudad":"madrid"}
for clave in diccionario:
    print(clave)  #esto imprime las llaves del diccionario
    print(diccionario[clave])  #esto imprime los valores del diccionario
    
for clave, valor in diccionario.items():  #esto imprime las llaves y los valores del diccionario
    print(f"{clave}: {valor}")
    
#otra forma de iterar un diccionario es usando el metodo items()
#esto devuelve una lista de tuplas con las llaves y los valores del diccionario    
for datos in diccionario.items():  #esto imprime las tuplas con las llaves y los valores del diccionario
    key=datos[0]  #el primer elemento de la tupla es la llave
    value=datos[1]  #el segundo elemento de la tupla es el valor
    print(f"{key}: {value}")
    
#e
frutas = ["banana", "manzana", "naranja", "kiwi", "fresa", "mango", "piña"]
for fruta in frutas:
    if fruta == "kiwi":
        continue
    print(f"Esta {fruta} me gusta")
    
for fruta in frutas:
    if fruta == "kiwi":
        print(f"Esta {fruta} no me gusta me cae mal")
        break   #cuando el codigo encuntra el break, sale del bucle
    else:
        #si no se encuentra el break, se ejecuta el else
        #esto es util para cuando queremos hacer algo si no se encuentra el break
        #en este caso, si no se encuentra el kiwi, se imprime el mensaje
        print(f"Esta {fruta} me gusta")
        
#iterando una cadena de texto
cadena = "hola mundo"
for letra in cadena:
    print(letra)  #esto imprime cada letra de la cadena
    
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        print("Número encontrado:", numero)
        break  # sale del bucle si encuentra el número 3
    
numeros_duplicados = [x*2 for x in numeros]  # esto duplica cada número en la lista
print("Números duplicados:", numeros_duplicados)
