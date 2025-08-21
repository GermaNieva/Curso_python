#Variables

""""Las variables son espacios de memoria que almacenan datos.
Puedes pensar en ellas como etiquetas que apuntan a un valor específico."""

#Para crear una variable, simplemente asigna un valor a un nombre usando el operador "="

nombre = "Juan"  #asignación de una cadena de texto a la variable nombre
edad = 30  #asignación de un número entero a la variable edad
ciudad = "Madrid"  #asignación de una cadena de texto a la variable ciudad

#Puedes cambiar el valor de una variable en cualquier momento

nombre = "Ana"  #ahora la variable nombre apunta a un nuevo valor

#Puedes usar variables en operaciones
#Por ejemplo, si tienes dos variables numéricas y quieres sumarlas: 

a=5
b=8
c=a+b  #suma de variables

#Puedes imprimir el valor de una variable usando la función print()
print(c)  #esto mostrará 13 en la consola
print(nombre)  #esto mostrará "Ana" en la consola

a+=1  #equivalente a a = a + 1
print(a)  #esto mostrará 6 en la consola

Mensaje= "Hola, " + nombre + "! Tienes " + str(edad) + " años y vives en " + ciudad + "."
print(Mensaje)  #esto mostrará "Hola, Ana! Tienes 30 años y vives en Madrid."

print(f"hola, {nombre}! Tienes {edad} años y vives en {ciudad}.")

f'{nombre} es un nombre muy bonito.'

f"hola {nombre}! Tienes {edad} años y vives en {ciudad}."

# (del) nombre  #esto eliminará la variable nombre

# operadores de pertenencia (in, not in)
Mensaje = "Hola, Ana! Tienes 30 años y vives en Madrid."
"hola" in Mensaje  #esto verificará si la subcadena "hola" está presente en la variable Mensaje - devuelve True o False

"lucas" not in Mensaje  #esto verificará si la subcadena "lucas" no está presente en la variable Mensaje - devuelve True o False

# En python no se usa camel case se usa snake case
mi_variable = 10


print(mi_variable)  #esto mostrará 10 en la consola

lista=[]

lista.append()





