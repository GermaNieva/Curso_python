# ejercicio numero 2, obtener nombre y edad de los compañeros de clase, el alumno de mayor edad sera el profesor y el de menor edad sera el asistente 

def obtener_compañeros(cantidad_de_compañeros):
    compañeros=[]   # creando la lista compañeros 
    
    #ejecutando un for para pedir la informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre=input("ingrese el nombre del compañero: ")
        edad= int(input("ingrese la edad del compañero"))
        compañero=(nombre,edad)
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    # ordeando los elementos de la lista con sort segun su edad
    compañeros.sort(key=lambda x:x[1])
    #compañeros x devuuelve una tupla con (nombre,edad) y luego accedemos al nombre para definir el asistente y el profesor 
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    #retornamos una tupla
    return asistente,profesor
#desempaquetamos lo retornado por la funcion 
asistente,profesor=obtener_compañeros(5)
#mostramos el resultado
print(f"el profesor es {profesor} y el asistente es {asistente}")




