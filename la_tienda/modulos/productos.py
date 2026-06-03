#               MODULO DE VENTAS
#           Francis Asaf Estrada Francia
#                   2026-05-07
from archivos import cargar_datos, guardar_datos
from utilidades import validar_entero_positivo, validar_float_positivo
ARCHIVO_PRODUCTOS = "datos/productos.json"


def obtener_productos():
    
    # Carga la lista de productos desde el archivo JSON de inventario.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # list: Una lista de diccionarios con la información de los productos registrados.
    
    return cargar_datos(ARCHIVO_PRODUCTOS)


def guardar_productos(productos):
    
    # Sobrescribe el archivo de inventario con la lista actualizada de productos.
    
    # Recibe:
        # productos (list): Lista de diccionarios con los productos a guardar.
        
    # Devuelve:
        # bool: True si se guardaron los datos correctamente, False si ocurrió un error.
    
    return guardar_datos(ARCHIVO_PRODUCTOS, productos)


def producto_existe(codigo, productos):
    
    # Verifica si un código de producto ya se encuentra registrado en el inventario.
    
    # Recibe:
        # codigo (str): El código del producto a buscar.
        # productos (list): La lista actual de productos registrados.
        
    # Devuelve:
        # bool: True si el código ya existe, False en caso contrario.
    
    for p in productos:
        if p["codigo"] == codigo:
            return True
    return False


def registrar_producto():
    
    # Solicita al usuario los datos necesarios para crear y guardar un nuevo producto en el inventario.
    
    # Recibe:
        # Nada (interactúa directamente con el usuario por consola).
        
    # Devuelve:
        # Nada.
    
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    
    productos = obtener_productos()
    
    while True:
        codigo = input("Código (ej: P001): ").strip().upper()
        if not producto_existe(codigo, productos):
            break
        print("Ese código ya existe. Use otro.")
    
    nombre = input("Nombre: ").strip().capitalize()
    categoria = input("Categoría (Abarrotes, Bebidas, etc): ").strip().capitalize()
    precio = validar_float_positivo("Precio (Q): ")
    stock = validar_entero_positivo("Stock inicial: ")
    stock_minimo = validar_entero_positivo("Stock mínimo: ")
    
    nuevo = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "stock_minimo": stock_minimo
    }
    
    productos.append(nuevo)
    
    if guardar_productos(productos):
        print(f"Producto {nombre} registrado con éxito.")
    else:
        print("Error al guardar.")


def listar_productos():
    
    # Muestra en pantalla una tabla formateada con todos los productos registrados en el inventario.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # Nada (imprime la tabla en la consola).
    
    productos = obtener_productos()
    
    if not productos:
        print("No hay productos registrados.")
        return
    
    print("\n" + "="*70)
    print(f"{'Código':<10} {'Nombre':<20} {'Precio':<10} {'Stock':<8} {'Stock Mín':<10}")
    print("-"*70)
    
    for p in productos:
        print(f"{p['codigo']:<10} {p['nombre']:<20} Q{p['precio']:<9.2f} {p['stock']:<8} {p['stock_minimo']:<10}")
    
    print("="*70)


def buscar_producto():
    
    # Permite al usuario buscar productos por su código o nombre y muestra las coincidencias.
    
    # Recibe:
        # Nada (solicita el término de búsqueda por consola).
        
    # Devuelve:
        # Nada (imprime los resultados encontrados en la consola).
    
    productos = obtener_productos()
    
    if not productos:
        print("No hay productos.")
        return
    
    busqueda = input("Ingrese código o nombre a buscar: ").strip().lower()
    resultados = []
    
    for p in productos:
        if busqueda in p["codigo"].lower() or busqueda in p["nombre"].lower():
            resultados.append(p)
    
    if resultados:
        print("\nResultados encontrados:")
        for r in resultados:
            print(f"{r['codigo']} - {r['nombre']} | Precio: Q{r['precio']} | Stock: {r['stock']}")
    else:
        print("No se encontraron productos.")


def actualizar_precio():
    
    # Solicita el código de un producto y permite modificar su precio actual.
    
    # Recibe:
        # Nada (interactúa con el usuario por consola).
        
    # Devuelve:
        # Nada.
    
    productos = obtener_productos()
    codigo = input("Código del producto: ").strip().upper()
    
    for p in productos:
        if p["codigo"] == codigo:
            nuevo_precio = validar_float_positivo(f"Precio actual: Q{p['precio']}. Nuevo precio: Q")
            p["precio"] = nuevo_precio
            
            if guardar_productos(productos):
                print(f"Precio actualizado a Q{nuevo_precio}")
            else:
                print("Error al guardar.")
            return
            
    print("Producto no encontrado.")


def ajustar_stock():
    
    # Permite sumar unidades (compra), restar unidades (merma) o modificar el stock mínimo de un producto específico.
    
    # Recibe:
        # Nada (interactúa con el usuario por consola).
        
    # Devuelve:
        # Nada.
    
    productos = obtener_productos()
    codigo = input("Código del producto: ").strip().upper()
    
    for p in productos:
        if p["codigo"] == codigo:
            print(f"Stock actual: {p['stock']}")
            print("1. Aumentar stock")
            print("2. Disminuir stock")
            print("3. Modificar stock minimo")
            opcion = input("Opción: ").strip()
            
            if opcion == "1":
                cantidad = validar_entero_positivo("Cantidad a agregar: ")
                p["stock"] += cantidad
                motivo = "compra"
                
            elif opcion == "2":
                cantidad = validar_entero_positivo("Cantidad a retirar: ")
                if cantidad > p["stock"]:
                    print("No se puede retirar más del stock actual.")
                    return
                p["stock"] -= cantidad
                motivo = "merma"
            
            elif opcion == "3":
                nuevo_minimo = validar_entero_positivo("Nuevo stock mínimo: ")
                p["stock_minimo"] = nuevo_minimo
                motivo = "actualización de stock mínimo"
                mensaje = f"Nuevo stock mínimo: {p['stock_minimo']}"
                
            else:
                print("Opción inválida")
                return
            
            if guardar_productos(productos):
                print(f"Stock actualizado por {motivo}. Nuevo stock: {p['stock']}")
            return
            
    print("Producto no encontrado.")


def eliminar_producto():
    
    # Elimina un producto del inventario mediante su código, validando antes que no tenga ventas registradas.
    
    # Recibe:
        # Nada (interactúa con el usuario por consola).
        
    # Devuelve:
        # Nada.
    
    productos = obtener_productos()
    
    if not productos:
        print("No hay productos registrados.")
        return
        
    codigo = input("Código del producto a eliminar: ").strip().upper()
    
    producto_encontrado = None
    for p in productos:
        if p["codigo"] == codigo:
            producto_encontrado = p
            break
    
    if not producto_encontrado:
        print("Producto no encontrado.")
        return
    
    ventas = cargar_datos("datos/ventas.json")
    
    for venta in ventas:
        for item in venta.get("items", []):
            if item["codigo"] == codigo:
                print("No se puede eliminar: este producto tiene ventas registradas.")
                return
    
    productos.remove(producto_encontrado)
    
    if guardar_productos(productos):
        print(f"Producto {producto_encontrado['nombre']} eliminado.")
    else:
        print("Error al guardar.")


def productos_bajo_stock():
    
    # Identifica y muestra los productos cuyo stock actual es menor o igual a su stock mínimo configurado.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # list: Una lista con los diccionarios de los productos que tienen el stock bajo.
    
    productos = obtener_productos()
    
    bajos = [p for p in productos if p["stock"] <= p["stock_minimo"]]
    
    if bajos:
        print("\nPRODUCTOS CON STOCK BAJO ")
        for p in bajos:
            print(f"{p['codigo']} - {p['nombre']}: Stock {p['stock']} (Mínimo {p['stock_minimo']})")
    else:
        print("Todos los productos tienen stock adecuado.")
    
    return bajos


def modulo_productos():
    
    # Muestra el menú interactivo para acceder a las opciones de gestión de inventario y maneja la elección del usuario.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # Nada (mantiene al usuario en un bucle hasta que decida salir).
    
    while True:
        print("\n=== MÓDULO DE INVENTARIO Y PRODUCTOS ===")
        print("1. Registrar producto nuevo")
        print("2. Listar todos los productos")
        print("3. Buscar producto")
        print("4. Actualizar precio")
        print("5. Ajustar stock (Entradas/Mermas)")
        print("6. Mostrar productos con stock bajo")
        print("7. Eliminar producto")
        print("0. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_precio()
        elif opcion == "5":
            ajustar_stock()
        elif opcion == "6":
            productos_bajo_stock()
        elif opcion == "7":
            eliminar_producto()
        elif opcion == "0":
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")