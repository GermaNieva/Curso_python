#condicionales
edad = 18
tiene_identificacion = True
puede_entrar = edad >= 18 and tiene_identificacion

if puede_entrar:
    print("Puedes entrar al club.")
else:
    print("No puedes entrar al club.")
    
contraseña_almacenada = "secreto123"
contraseña_ingresada = input("Ingresa tu contraseña: ")

if contraseña_ingresada == contraseña_almacenada:
    print("Contraseña correcta. Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")
