# creando conjuntos con set()

conjunto=set(["dato1","dato2"])
print(conjunto)

#metiendo un conjunto dentro de otro conjunto frozenset esto permite que el conjunto sea inmutable
conjunto2=frozenset(["dato3","dato4"])
print(conjunto2)

#teoria de conjuntos
conjunto3=set(["dato5","dato6"])
conjunto4=set(["dato6","dato7"])

# verificando si un conjunto es subconjunto de otro
resultado= conjunto3.issubset(conjunto4) # False
resultado = conjunto3 <= conjunto4 # otra forma de verificar si es subconjunto
print(resultado)

# verificando si un conjunto es superconjunto de otro
resultado= conjunto4.issuperset(conjunto3)  # True
resultado= conjunto4 >= conjunto3  # otra forma de verificar si es superconjunto
print(resultado)

#verificar si hay numeros en comun entre conjuntos
resultado= conjunto3.isdisjoint(conjunto4)  # False, porque hay un elemento en comun
resultado= conjunto3.isdisjoint(conjunto2)  # True, porque no hay elementos






