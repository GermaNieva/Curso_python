# Metodos de cadenas
cadena = "Hola, Mundo!"
cadena2 = "Python es genial"

print(dir(cadena))  # Muestra los métodos disponibles para la cadena  # dir es una funcion que muestra los atributos y métodos de un objeto
print("Longitud de la cadena:", len(cadena))  # Longitud de la cadena

upper_cadena = cadena.upper()  # Convierte la cadena a mayúsculas
lower_cadena = cadena.lower()  # Convierte la cadena a minúsculas
print("Cadena en mayúsculas:", upper_cadena)
print("Cadena en minúsculas:", lower_cadena)

primer_letra_mayuscula = cadena.capitalize()  # Convierte la primera letra a mayúscula
print("Cadena con primera letra mayúscula:", primer_letra_mayuscula)

#buscamos una cadena en otra cadena
posicion = cadena.find("Mundo")  # Encuentra la posición de una subcadena
print("Posición de 'Mundo' en la cadena:", posicion) #imprime la posición de la subcadena 
#devuelve -1 si no se encuentra la subcadena

#la diferencia entre find y index es que find devuelve -1 si no encuentra la subcadena, mientras que index lanza una excepción
posicion_index = cadena.index("Mundo")  # Encuentra la posición de una subcadena
print("Posición de 'Mundo' usando index:", posicion_index)

# isnumeric sirve para verificar si una cadena es numérica
es_numerica = cadena.isnumeric()  # Verifica si la cadena es numérica

#si es alfanumérica, devuelve True si todos los caracteres son alfanuméricos
es_alfanumerica = cadena.isalnum()  # Verifica si la cadena es alfanumérica
print("La cadena es numérica:", es_numerica)

#diferencia entre isalpha e isalnum
es_alpha = cadena.isalpha()  # Verifica si la cadena contiene solo letras
print("La cadena es alfanumérica:", es_alfanumerica)
print("La cadena contiene solo letras:", es_alpha)
# isalnum devuelve True si la cadena contiene letras y números, mientras que isalpha devuelve True solo si la cadena contiene letras.
print("La cadena contiene solo letras:", es_alpha)

#contar cuantas veces aparece una subcadena en una cadena
contador = cadena.count("o")  # Cuenta cuántas veces aparece una subcadena
print("La letra 'o' aparece", contador, "veces en la cadena.")

#contamos cuantos caracteres hay en una cadena
longitud = len(cadena)  # Cuenta la longitud de la cadena
print("La longitud de la cadena es:", longitud)

#verificamos si una cadena empieza con una subcadena
empieza_con = cadena.startswith("Hola")  # Verifica si la cadena empieza con una subcadena
print("La cadena empieza con 'Hola':", empieza_con) #devuelve True o False

#verificamos si una cadena termina con una subcadena
termina_con = cadena.endswith("Mundo!")  # Verifica si la cadena termina con una subcadena
print("La cadena termina con 'Mundo!':", termina_con) #devuelve True o False

#reemplazamos una subcadena por otra
nueva_cadena = cadena.replace("Mundo", "Python")  # Reemplaza una subcadena por otra
print("Cadena después del reemplazo:", nueva_cadena) #esto imprimira "Hola, Python!"

#dividimos una cadena en una lista de subcadenas
lista_subcadenas = cadena.split(", ")  # Divide la cadena en una lista de subcadenas
print("Lista de subcadenas:", lista_subcadenas)  # Imprime la lista



