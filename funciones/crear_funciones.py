#Creando una funcion simple

def saludar():
    print("hola ivi!")
    
#ejecutando la funcion simple 
saludar()


#Creando una funcion con parametros 

def saludar(nombre,sexo):
    print(f"hola {nombre} como estas?")
    if sexo == "mujer":
        adjetivo ="reina"
    elif sexo =="hombre":
        adjetivo ="capo"
    else:
        adjetivo="amor"
    print(f"hola {nombre} como estas {adjetivo}?")
    
    
#creando una funcion que retorna vaolores 
def crear_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1= num -2
    c2= num 
    c3 = num -5 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
pasword,primernumero= crear_contraseña_random(5)
frase=(f"tu contraseña es {pasword} y el valor para crearla es {primernumero}")
print(frase)




    
    
