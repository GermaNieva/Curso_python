# operadores logicos

# Los operadores lógicos se utilizan para combinar expresiones booleanas y devolver un valor booleano (True o False).
# Los operadores lógicos más comunes son:
# and (y): Devuelve True si ambas expresiones son verdaderas.
# or (o): Devuelve True si al menos una de las expresiones es verdadera.
# not (no): Invierte el valor de la expresión (True se convierte en False y viceversa).

a = True
b = False
c = True
d = False
resultado_and = a and b  # False
resultado_or = a or b    # True
resultado_not = not a    # False
resultado_combinado = (a and c) or (b and d)  # True
print("Resultado AND:", resultado_and)
print("Resultado OR:", resultado_or)
print("Resultado NOT:", resultado_not)
print("Resultado combinado:", resultado_combinado)

# Los operadores lógicos son útiles para tomar decisiones en el código, como en estructuras condicionales o bucles.
# Por ejemplo, se pueden usar en una sentencia if para ejecutar un bloque de código solo si una condición compuesta es verdadera.
# También se pueden combinar con operadores de comparación para crear condiciones más complejas.
# Ejemplo de uso de operadores lógicos en una sentencia if

#AND
resultado = True & False  # False
resultado2 = True and False  # False
resultado3 = True and True  # True
resultado4 = False and True  # False
resultado5 = False & False  # False

#or
resultado6 = True | False  # True
resultado7 = True or False  # True
resultado8 = True or True  # True
resultado9 = False or True  # True
resultado10 = False | False  # False

# NOT
resultado11 = not True  # False
resultado12 = not False  # True

# Ejemplo de uso de operadores lógicos en una sentencia if
edad = 18