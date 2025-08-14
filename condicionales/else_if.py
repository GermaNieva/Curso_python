# elif en Python
# El uso de elif permite evaluar múltiples condiciones de manera secuencial.
# Si la primera condición es falsa, se evalúa la siguiente, y así sucesivamente.
# Si ninguna condición es verdadera, se puede usar un bloque else para manejar el caso por defecto
# Ejemplo de uso de elif

ingreso_mensual = 3000
if ingreso_mensual < 1000:
    print("estas en la categoría de ingreso bajo")
elif ingreso_mensual < 3000:
    print("estas en la categoría de ingreso medio")
elif ingreso_mensual < 5000:
    print("estas en la categoría de ingreso alto")
else:
    print("estas en la categoría de ingreso muy alto")

# Ejemplo de uso de elif con edad
edad = 20
if edad < 13:
    print("Eres un niño.")
elif edad < 20:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")
elif edad < 100:
    print("Eres un adulto mayor.")
else:
    print("Eres muy mayor.")
    
# Ejemplo de uso de elif con calificaciones
calificacion = 85
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 70:
    print("Bien")
elif calificacion >= 60:
    print("Suficiente")
elif calificacion >= 50:
    print("Insuficiente")
else:
    print("Reprobado")


#if y elif anidados
# Ejemplo de if anidados
numero = 15
if numero > 0:
    print("El número es positivo.")
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
else:
    print("El número es negativo o cero.")
    
# Ejemplo de elif anidados
hora = 14 
if hora < 12:
    print("Buenos días")
elif hora < 18:
    print("Buenas tardes")
elif hora < 22:
    print("Buenas noches")
else:
    print("Hora no válida")

