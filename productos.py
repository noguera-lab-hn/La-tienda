"""
Módulo: productos.py
Autores: [Francis Asaf Estrada Francia]
Fecha: 2026-05-06
Descripción: Funciones para gestionar productos (CRUD, stock, búsquedas)
"""

# IMPORTAMOS FUNCIONES DE utils.py
from utils import cargar_datos, guardar_datos, validar_entero_positivo, validar_float_positivo

# CONSTANTE: Nombre del archivo donde se guardan los productos
ARCHIVO_PRODUCTOS = "productos.json"


# ============================================
# FUNCIONES BÁSICAS (CARGAR, GUARDAR, VERIFICAR)
# ============================================

def obtener_productos():
    # Llama a cargar_datos pasándole el nombre del archivo
    # Lo que devuelva cargar_datos (lista de productos) lo devuelve
    return cargar_datos(ARCHIVO_PRODUCTOS)


def guardar_productos(productos):
    # Llama a guardar_datos con el nombre del archivo y los datos
    # Devuelve True si se guardó bien, False si hubo error
    return guardar_datos(ARCHIVO_PRODUCTOS, productos)


def producto_existe(codigo, productos):
    # FOR: Itera sobre cada producto en la lista de productos
    for p in productos:
        # Si el código del producto actual es igual al código buscado
        if p["codigo"] == codigo:
            # Encontrado: devuelve True (sí existe)
            return True
    # Si terminó el bucle sin encontrar, devuelve False (no existe)
    return False


# ============================================
# FUNCIONES PRINCIPALES DEL CRUD
# ============================================

def registrar_producto():
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    
    # Obtiene la lista actual de productos para verificar códigos únicos
    productos = obtener_productos()
    
    # --- Solicitar código único ---
    while True:  # Bucle que se repite hasta que el código sea válido
        # input() pide al usuario, .strip() elimina espacios, .upper() convierte a mayúsculas
        # Ejemplo: usuario escribe " p001 " → se convierte en "P001"
        codigo = input("Código (ej: P001): ").strip().upper()
        
        # Si el código NO existe (producto_existe devuelve False)
        # not False = True, entonces entra al if
        if not producto_existe(codigo, productos):
            break  # break sale del bucle while
        # Si existe, muestra error y el bucle se repite
        print("Ese código ya existe use otro.")
    
    # --- Solicitar nombre ---
    # .strip() elimina espacios, .capitalize() pone primera letra mayúscula
    # Ejemplo: "azucar" → "Azucar"
    nombre = input("Nombre: ").strip().capitalize()
    
    # --- Solicitar categoría ---
    categoria = input("Categoría (Abarrotes, Bebidas, etc): ").strip().capitalize()
    
    # --- Solicitar precio (con validación) ---
    # validar_float_positivo se encarga de que sea número positivo
    precio = validar_float_positivo("Precio (Q): ")
    
    # --- Solicitar stock inicial ---
    stock = validar_entero_positivo("Stock inicial: ")
    
    # --- Solicitar stock mínimo (alerta) ---
    stock_minimo = validar_entero_positivo("Stock mínimo: ")
    
    # --- Crear diccionario con los datos del nuevo producto ---
    # Un diccionario tiene clave: valor, como una ficha o formulario
    nuevo = {
        "codigo": codigo,           # clave "codigo" guarda el código
        "nombre": nombre,            # clave "nombre" guarda el nombre
        "categoria": categoria,      # clave "categoria" guarda la categoría
        "precio": precio,            # clave "precio" guarda el precio
        "stock": stock,              # clave "stock" guarda la cantidad
        "stock_minimo": stock_minimo # clave "stock_minimo" guarda el mínimo
    }
    
    # --- Agregar a la lista y guardar ---
    productos.append(nuevo)  # .append() agrega el nuevo diccionario al final de la lista
    
    # Intentamos guardar en el archivo
    if guardar_productos(productos):
        # f"texto {variable}" permite insertar variables dentro del texto
        print(f"Producto {nombre} registrado con éxito.")
    else:
        print("Error al guardar.")


def listar_productos():
    """Muestra todos los productos en formato tabla."""
    productos = obtener_productos()
    
    # Si la lista está vacía (not productos = True cuando está vacía)
    if not productos:
        print("No hay productos registrados.")
        return  # return sale de la función, no hace nada más
    
    # --- Imprimir cabecera de la tabla ---
    # "\n" es salto de línea, "="*70 crea 70 signos = consecutivos
    print("\n" + "="*70)
    # :<10 significa alineado a la izquierda con ancho 10 caracteres
    print(f"{'Código':<10} {'Nombre':<20} {'Precio':<10} {'Stock':<8} {'Stock Mín':<10}")
    print("-"*70)
    
    # --- Imprimir cada producto ---
    for p in productos:  # p es cada producto (diccionario) en la lista
        # p["codigo"] accede al valor dentro del diccionario con la clave "codigo"
        # :<9.2f significa: alineado izquierda, ancho 9, 2 decimales (float)
        print(f"{p['codigo']:<10} {p['nombre']:<20} Q{p['precio']:<9.2f} {p['stock']:<8} {p['stock_minimo']:<10}")
    
    print("="*70)


def buscar_producto():
    productos = obtener_productos()
    
    if not productos:
        print("No hay productos.")
        return
    
    # Pedir búsqueda y convertir a minúsculas para que no distinga mayúsculas
    busqueda = input("Ingrese código o nombre a buscar: ").strip().lower()
    
    # Lista vacía donde guardaremos los resultados
    resultados = []
    
    # Recorrer todos los productos
    for p in productos:
        # lower() convierte a minúsculas para comparar sin importar mayúsculas
        # "in" verifica si el texto de búsqueda está dentro del código o nombre
        if busqueda in p["codigo"].lower() or busqueda in p["nombre"].lower():
            resultados.append(p)  # Agregar producto encontrado a la lista de resultados
    
    # Mostrar resultados
    if resultados:
        print("\nResultados encontrados:")
        for r in resultados:
            print(f"{r['codigo']} - {r['nombre']} | Precio: Q{r['precio']} | Stock: {r['stock']}")
    else:
        print("No se encontraron productos.")


def actualizar_precio():
    productos = obtener_productos()
    codigo = input("Código del producto: ").strip().upper()
    
    # Buscar el producto por código
    for p in productos:
        if p["codigo"] == codigo:
            # Pedir nuevo precio con validación
            nuevo_precio = validar_float_positivo(f"Precio actual: Q{p['precio']}. Nuevo precio: Q")
            # Actualizar el precio en el diccionario
            p["precio"] = nuevo_precio
            
            # Guardar cambios
            if guardar_productos(productos):
                print(f"Precio actualizado a Q{nuevo_precio}")
            else:
                print("Error al guardar.")
            return  # Salir de la función porque ya encontramos y actualizamos
    
    # Si llegamos aquí, no se encontró el producto
    print("Producto no encontrado.")


def ajustar_stock():
    productos = obtener_productos()
    codigo = input("Código del producto: ").strip().upper()
    
    for p in productos:
        if p["codigo"] == codigo:
            print(f"Stock actual: {p['stock']}")
            print("1. Aumentar stock")
            print("2. Disminuir stock")
            opcion = input("Opción: ")
            
            if opcion == "1":
                # Aumentar stock
                cantidad = validar_entero_positivo("Cantidad a agregar: ")
                # += es atajo para: p["stock"] = p["stock"] + cantidad
                p["stock"] += cantidad
                motivo = "compra"  # Esta variable no se usa pero la guardamos para futuro
                
            elif opcion == "2":
                # Disminuir stock
                cantidad = validar_entero_positivo("Cantidad a retirar: ")
                # Verificar que no se retire más de lo que hay
                if cantidad > p["stock"]:
                    print("No se puede retirar más del stock actual.")
                    return  # Salir sin guardar cambios
                # -= es atajo para: p["stock"] = p["stock"] - cantidad
                p["stock"] -= cantidad
                motivo = "merma"
                
            else:
                print("Opción inválida")
                return
            
            # Guardar cambios
            if guardar_productos(productos):
                print(f"Stock actualizado. Nuevo stock: {p['stock']}")
            return  # Salir porque ya procesamos
    
    print("Producto no encontrado.")


def eliminar_producto():
    # Importamos dentro de la función para evitar import circular
    # Esto es porque productos.py y ventas.py se necesitan mutuamente
    from ventas import obtener_ventas
    
    productos = obtener_productos()
    codigo = input("Código del producto a eliminar: ").strip().upper()
    
    # --- Buscar el producto ---
    producto_encontrado = None  # None significa "nada", es un valor vacío
    for p in productos:
        if p["codigo"] == codigo:
            producto_encontrado = p  # Guardamos el producto encontrado
            break  # break sale del bucle porque ya lo encontramos
    
    # Si no se encontró (producto_encontrado sigue siendo None)
    if not producto_encontrado:
        print("Producto no encontrado.")
        return
    
    # --- Verificar si el producto tiene ventas registradas ---
    ventas = obtener_ventas()  # Cargar todas las ventas
    
    # Recorrer cada venta
    for venta in ventas:
        # Recorrer cada producto dentro de la venta
        for item in venta["items"]:  # venta["items"] es la lista de productos de esa venta
            if item["codigo"] == codigo:
                # Si encuentra el código en alguna venta
                print("No se puede eliminar: este producto tiene ventas registradas.")
                return  # Salir sin eliminar
    
    # --- Si llegamos aquí, no tiene ventas. Proceder a eliminar ---
    # .remove() elimina el elemento de la lista
    productos.remove(producto_encontrado)
    
    # Guardar cambios
    if guardar_productos(productos):
        print(f"Producto {producto_encontrado['nombre']} eliminado.")
    else:
        print("Error al guardar.")


def productos_bajo_stock(): # Muestra productos con stock actual menor o igual al stock mínimo
    productos = obtener_productos()
    
    # Comprensión de lista: forma compacta de crear una lista filtrada
    # Esto es equivalente a:
    #   bajos = []
    #   for p in productos:
    #       if p["stock"] <= p["stock_minimo"]:
    #           bajos.append(p)
    bajos = [p for p in productos if p["stock"] <= p["stock_minimo"]]
    
    if bajos:
        print("\nPRODUCTOS CON STOCK BAJO ")
        for p in bajos:
            print(f"{p['codigo']} - {p['nombre']}: Stock {p['stock']} (Mínimo {p['stock_minimo']})")
    else:
        print("Todos los productos tienen stock adecuado.")
    
    # Devolvemos la lista por si se necesita (para reportes)
    return bajos
