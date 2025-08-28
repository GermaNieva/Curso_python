#creando una funcion de 3 parametros
#utilizando keyword arguments 
def frase(nombre,apellido,adjetivo):
    return f" Hola {nombre} {apellido}, sos {adjetivo}"

frase_resultante= frase(nombre="German",apellido="nieva",adjetivo="alto")
print(frase_resultante)

#utilizando la funcion con un parametro opcion y un valor por defecto 

def frase(nombre,apellido,adjetivo="bajo"):
    return f" Hola {nombre} {apellido}, sos {adjetivo}"

frase_resultante= frase("lucas","dalto")
print(frase_resultante)

#luego puedo cambiar el valor por defecto definiendolo de nuevo 

frase_resultante= frase("lucas","dalto",adjetivo="alto")
print(frase_resultante)



