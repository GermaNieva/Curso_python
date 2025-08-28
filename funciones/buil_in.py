numeros=[4,7,9,11,50]
#encontrando el numero mas alto de una lista

numero_mas_alto= max(numeros)

print(numero_mas_alto)

#encontrnado el numero mas bajo de una lista

numero_mas_bajo= min(numeros)
print(numero_mas_bajo)


#redondeando a 6 decimales 

numero= round(12.4568575,2)
print(numero)

# funcion bool 

bool()   #retorna false si le pasamos valores vacios o ningun valor o True si le pasamos una cadena o valores no vacios
resultado=bool()

# funcion all
# retorna true si todos los valores son verdaderos

resultado_all= all([0,"5",6,True])

#funcion sum ---- suma todos los valores que tiene un iterable # si o si deben ser enteros o arroja excepciones 
suma= sum(numeros)



