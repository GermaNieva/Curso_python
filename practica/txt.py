ejercicios= "ejercicios.txt"
escritura= "german 8, ivanna 9, lean 10"

with open(ejercicios, "w") as archivo:
    archivo.write(escritura)

print(f"el archivo {ejercicios} fue creado y escrito correctamente \n su contenido es")
with open(ejercicios, "r") as archivo:
    archivo=archivo.read()
print(escritura)