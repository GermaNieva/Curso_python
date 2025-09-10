import os

def capturar_alumnos():
    alumnos = {}
    print("Ingresa el nombre de cada alumno. Escribe 'fin' para terminar.")
    while True:
        nombre = input("Alumno: ").strip()
        if nombre.lower() == "fin":
            break
        if not nombre:
            continue
        notas = []
        print(f"Ingresa las notas de {nombre}. Escribe 'fin' para terminar.")
        while True:
            entrada = input("Nota: ").strip()
            if entrada.lower() == "fin":
                break
            try:
                notas.append(float(entrada))
            except ValueError:
                print("Por favor ingresa un número válido.")
        alumnos[nombre] = notas
    return alumnos

def guardar_alumnos(ruta, alumnos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        for nombre, notas in alumnos.items():
            linea = ",".join([nombre] + [str(n) for n in notas])
            archivo.write(linea + "\n")

def leer_alumnos(ruta):
    alumnos = {}
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if not partes or partes[0] == "":
                continue
            nombre = partes[0]
            notas = [float(n) for n in partes[1:] if n]
            alumnos[nombre] = notas
    return alumnos

def calcular_promedios(alumnos):
    promedios = {}
    for nombre, notas in alumnos.items():
        if notas:
            promedios[nombre] = sum(notas) / len(notas)
        else:
            promedios[nombre] = 0
    return promedios

def main():
    ruta_archivo = os.path.join(os.path.dirname(__file__), "notas.txt")
    alumnos = capturar_alumnos()
    guardar_alumnos(ruta_archivo, alumnos)
    datos = leer_alumnos(ruta_archivo)
    promedios = calcular_promedios(datos)
    for nombre, promedio in promedios.items():
        print(f"Promedio de {nombre}: {promedio}")

if __name__ == "__main__":
    main()
