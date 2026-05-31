# ==============================================================================
#                           MODULO DE VENTAS
#                       BRYAN jOSUE NOGUERA MOLINA
#                               21/5/2026
# ==============================================================================





# FASE 1: EL ESQUELETO BÁSICO (Menú y Carrito en Memoria)

# 1. Base de datos "de mentira" (Hardcoded)
# Creamos esta lista aquí mismo solo para poder probar la fase 1 
# sin tener que conectar los archivos JSON todavía.
productos_prueba = [
    {"codigo": "P001", "nombre": "Azúcar 1lb", "precio": 6.50, "stock": 24},
    {"codigo": "P002", "nombre": "Frijol Negro", "precio": 8.00, "stock": 15}
]

def iniciar_nueva_venta_fase1():
    print("--- INICIANDO NUEVA VENTA ---")
    
    # Pedimos el NIT de forma sencilla
    nit_cliente = input("Ingrese NIT del cliente (Deje vacío para CF): ")
    
    # Si el usuario solo dio Enter, la variable está vacía ("")
    if nit_cliente == "":
        nit_cliente = "CF"
        
    # El carrito empieza como una lista vacía
    carrito = []
    
    # Bucle infinito para mantener el menú vivo
    while True:
        print("\n--- MENÚ DE VENTA ---")
        print("1. Agregar producto")
        print("2. Mostrar carrito")
        print("3. Salir / Cancelar")
        
        opcion = input("Elige una opción: ")
        
        # ----------------------------------------------------
        # OPCIÓN 1: AGREGAR PRODUCTO
        # ----------------------------------------------------
        if opcion == "1":
            codigo_buscar = input("Ingresa el código del producto (ej. P001): ")
            
            # Buscamos el producto usando la forma más primitiva: un 'for' clásico.
            # Asumimos al principio que no existe (None)
            producto_encontrado = None 
            
            for p in productos_prueba:
                if p["codigo"] == codigo_buscar:
                    # Si lo encontramos, lo guardamos en nuestra variable y rompemos el ciclo
                    producto_encontrado = p
                    break 
                    
            # Si el for terminó y la variable sigue vacía, es porque no existe
            if producto_encontrado is None:
                print("Error: El código de producto no existe.")
                
            else:
                # Si sí existe, pedimos la cantidad. 
                # (Aún no usaremos try/except, asumimos que el usuario escribirá bien el número)
                cantidad_texto = input("¿Cuántos deseas llevar?: ")
                cantidad = int(cantidad_texto) 
                
                # Calculamos el subtotal (matemática básica)
                subtotal = cantidad * producto_encontrado["precio"]
                
                # Armamos el "ítem" y lo metemos al carrito usando .append()
                item = {
                    "codigo": producto_encontrado["codigo"],
                    "nombre": producto_encontrado["nombre"],
                    "cantidad": cantidad,
                    "precio_unit": producto_encontrado["precio"],
                    "subtotal": subtotal
                }
                
                carrito.append(item)
                print("¡Producto agregado al carrito con éxito!")
                
        # ----------------------------------------------------
        # OPCIÓN 2: MOSTRAR CARRITO
        # ----------------------------------------------------
        elif opcion == "2":
            print("\n--- TU CARRITO ACTUAL ---")
            
            # len() cuenta cuántos elementos hay en la lista
            if len(carrito) == 0:
                print("El carrito está vacío.")
            else:
                # Recorremos la lista del carrito e imprimimos de forma muy básica
                for item in carrito:
                    print(item["cantidad"], "x", item["nombre"], "- Subtotal: Q", item["subtotal"])
                    
        # ----------------------------------------------------
        # OPCIÓN 3: SALIR
        # ----------------------------------------------------
        elif opcion == "3":
            print("Cancelando venta y saliendo del menú...")
            break # La instrucción break destruye el 'while True' y termina la función
            
        else:
            print("Opción incorrecta. Escribe 1, 2 o 3.")

# ------------------------------------------------------------------------------
# Punto de entrada: Llamamos a la función para que el programa arranque
# ------------------------------------------------------------------------------
iniciar_nueva_venta_fase1()