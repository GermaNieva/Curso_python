
# Ejercicio práctico 1: Comparación de duración de cursos
# Este ejercicio compara la duración del curso de Dalto con otros cursos.

duracio_otros_cursos_min = 2.5
duracio_otros_cursos_max = 7
duracio_otros_cursos_promedio = 4

curso_dalto= 1.5

#duracion_de_video_crudo
crudo_promedio= 5
crudo_video_dalto= 3.5

diferencia_con_min= 100 - curso_dalto/duracio_otros_cursos_min*100
diferencia_con_max= 100 - curso_dalto//duracio_otros_cursos_max*100 #aqui se usa // para obtener el entero
# se usa // porque la duración de los cursos es un número entero
diferencia_con_promedio= 100 - curso_dalto/duracio_otros_cursos_promedio*100

print(f"El curso de Dalto es un {diferencia_con_min:.2f}% más corto que el curso más corto.")
print(f"El curso de Dalto es un {diferencia_con_max:.2f}% más corto que el curso más largo.")
print(f"El curso de Dalto es un {diferencia_con_promedio:.2f}% más corto que el curso promedio.")

#calculando la duracion de tiempo de video crudo

tiempo_vacio_promedio= 100 - duracio_otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_promedio_dalto = 100 - curso_dalto * 1000 // crudo_video_dalto / 10

print(f"El curso de Dalto tiene un {tiempo_vacio_promedio_dalto:.2f}% de tiempo vacío en comparación con el promedio.")
print(f"El curso promedio tiene un {tiempo_vacio_promedio:.2f}% de tiempo vacío en comparación con el curso de Dalto.")

#ver 10 horas del curso de Dalto equivale a ver cuantas horas de otros cursos?
horas_dalto = 10
horas_otros_cursos = horas_dalto * duracio_otros_cursos_promedio
print(f"Ver {horas_dalto} horas del curso de Dalto equivale a ver {horas_otros_cursos:.2f} horas de otros cursos.")







