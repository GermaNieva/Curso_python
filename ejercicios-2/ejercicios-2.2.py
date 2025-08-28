#funcion que nos devuelva numeros primos entre 0 y el argumento que le pasemos 

def es_primo(num):   # esta funcion devuelve true si un numero es primo 
    for i in range (2,num-1):   #verificamos que el numero pasado no pueda dividirse ente ningun numero a partir de dos ni por si mismo 
        if num%i==0: return False     #si es divisible por algun numero retorna false y termina el bucle
    return True  #caso contrario devuelve true

def primos_hasta(num):   #crea una funcion que retorna la lista con todos los primos 
    primos=[]  #crea la lsita donde se almacenaran los primos 
    for i in range (3,num+1): 
        resultado= es_primo(i)  #verificamos si el valor es primo (si la funcion evuelve  true)
        if resultado == True: primos.append(i)  # si lo es lo agrega a la lista (primos)
    return primos

resultado= primos_hasta(98)

print(resultado)