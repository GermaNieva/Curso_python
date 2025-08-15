#pedirle un numero al usuario
numero = input("¿Cuál es tu número favorito? ")
print(f"Tu número favorito es {numero}!")
# --- IGNORE ---
# si se quiere convertir a otro tipo de dato se debe hacer explicitamente
# por ejemplo, para convertir a entero:
numero_entero = int(numero)
print(f"Tu número favorito como entero es {numero_entero}!")
# o a flotante:
numero_flotante = float(numero)
print(f"Tu número favorito como flotante es {numero_flotante}!")
# o a booleano:
numero_booleano = bool(numero)
print(f"Tu número favorito como booleano es {numero_booleano}!")