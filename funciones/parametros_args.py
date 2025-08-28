#utilizando el parametro args (*)
# * el operador o parametro args sirve para llamar o utilizar multiples elementos o variables en una funcion, siempre debe estar al fiinal de lo que llamemos en la funcion ya que es infinito
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("lucas",5,3,9,10,20,3)
print(resultado)    


#forma optima de sumar valores

def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])

print(resultado2)

resultado3=suma("ivi",5,6,7,8)
print(resultado3)

sum([5,6,7,8])



