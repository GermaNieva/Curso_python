#sucesion de fibonacci 
#la succesion de fibonacci lo que hace es sumar el primer y segundo numero y al resultado sumarle el anterior ej: a+b= c , c+b = d 
def fibonacci(num):
    a,b=0,1  # desempaquetado
    fibonacci_lista=[0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b=b,a+b
            
resultado = fibonacci(33)
print(resultado)


