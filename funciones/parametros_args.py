#utilizando el parametro args (*)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("lucas",5,3,9,10,20,3)
print(resultado)    


#forma optima de sumar valores

def suma_total(numeros):
    return suma({*numeros})

resultado2 = suma_total([5,3,9,10,20,3])