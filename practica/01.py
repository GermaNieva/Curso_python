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

tienda = []

#funcion para agregar productos

def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad en stock: "))
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    tienda.append(producto)
    
agregar_producto()

print(tienda)
    
# #ver productos
# def listar_productos():
#     if not tienda:
#         print("No hay productos en la tienda.")
#         return
#     print("Productos en la tienda:")
#     for codigo, info in tienda.items():
#         print(f"Código: {codigo}, Nombre: {info['nombre']}, Precio: {info['precio']}, Stock: {info['stock']}")


