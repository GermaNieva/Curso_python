"""Mini-proyecto: “MiniMarket CLI”

Construí una app de consola para gestionar productos y ventas de un minimercado.

Objetivos

Practicar variables, tipos de datos (str, int, float, bool, list, dict, set, tuple).

Usar input(), condicionales (if/elif/else) y operadores (aritméticos, comparación y lógicos).

Trabajar con métodos de cadenas, listas y diccionarios.

Iterar listas y diccionarios con for.

Usar bucle while para el menú.

Incluir conjuntos (set) y tuplas (con desempaquetado)."""


#1) Agregar producto
#2) Listar productos
#3) Buscar producto (código o nombre)
#4) Vender producto
#5) Reportes
#6) Actualizar precio/stock
#7) Eliminar producto
#8) Salir

from datetime import datetime

tienda=[]
ventas=[]
def agregar_producto():
    if not tienda:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        producto = {"codigo": 1,
                "nombre": nombre,
                "precio": precio,
                "stock": stock}
        tienda.append(producto)
    else:   
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        ultimo = tienda[-1]["codigo"]
        producto = {"codigo": ultimo+1,
                "nombre": nombre,
                "precio": precio,
                "stock": stock}
        tienda.append(producto)
    
def listar_productos():
        if not tienda:
            print("No hay productos en la tienda.")
        else:
            for producto in tienda:
                print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
                
def buscar_producto():
        busqueda = input("Ingrese el código o nombre del producto a buscar: ")
        encontrado = False
        for producto in tienda:
            if producto['codigo'] == busqueda or producto['nombre'].lower() == busqueda.lower():
                print(f"Producto encontrado: {producto}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
            
def vender_producto():
        codigo = input("Ingrese el código del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        for producto in tienda:
            if producto['codigo'] == int(codigo):
                if producto['stock'] >= cantidad:
                    producto['stock'] -= cantidad
                    print(f"Venta realizada, vendiste:{cantidad, producto["nombre"]} por un total de {cantidad*producto["precio"]}. Stock restante: {producto['stock']}")
                    fecha= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    Transaccion={
                        "venta":cantidad,
                        "producto":producto["nombre"],
                        "total":cantidad*producto["precio"],
                        "fecha":fecha
                        }
                    ventas.append(Transaccion)
                        
                else:
                    print("Stock insuficiente.")
                return
        print("Producto no encontrado.")
        
def reporte():
    if not ventas:
         print("No se encontraron transacciones.")
    else:
        for transaccion in ventas:
            print(f"venta: {transaccion['venta']}, Nombre: {transaccion['producto']}, total: {transaccion['total']}, Fecha: {transaccion['fecha']}")

menu = """Bienvenido al MiniMarket CLI
Seleccione una opción:
1) Agregar producto
2) Listar productos
3) Buscar producto (código o nombre)
4) Vender producto
5) Reportes
6) Actualizar precio/stock
7) Eliminar producto
8) Salir """

def iniciar():
    while True:
        print(f"MiniMarket CLI iniciado./n {menu}")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":
            print("Opción 1: Agregar producto")
            agregar_producto()
        elif opcion == "2":
            print("Opción 2: Listar productos")
            listar_productos()
        elif opcion == "3":
            print("Opción 3: Buscar producto")
            buscar_producto()
        elif opcion == "4":
            print("Opción 4: Vender producto")
            vender_producto()
        elif opcion == "5":
            print("Reporte de Ventas")
            reporte()
        else: 
            print("opcion incorrecta, intente de nuevo")
            break
        
iniciar()



