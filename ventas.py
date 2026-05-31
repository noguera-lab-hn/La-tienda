# ==============================================================================
#                           MODULO DE VENTAS
#                       BRYAN jOSUE NOGUERA MOLINA
#                               23/5/2026
# ==============================================================================





# FASE 2: VALIDACIONES, IVA Y QUITAR DEL CARRITO

# Base de datos "de mentira" (Mantenemos la de la Fase 1)
productos_prueba = [
    {"codigo": "P001", "nombre": "Azúcar 1lb", "precio": 6.50, "stock": 24},
    {"codigo": "P002", "nombre": "Frijol Negro", "precio": 8.00, "stock": 15}
]

def iniciar_nueva_venta_fase2():
    print("--- INICIANDO NUEVA VENTA ---")
    
    # (FASE 1) Pedimos el NIT 
    nit_cliente = input("Ingrese NIT del cliente (Deje vacío para CF): ")
    if nit_cliente == "":
        nit_cliente = "CF"
        
    carrito = []
    
    while True:
        print("\n--- MENÚ DE VENTA ---")
        print("1. Agregar producto")
        print("2. Mostrar carrito (con totales)") # Actualizado
        print("3. Quitar producto")              # NUEVO
        print("4. Salir / Cancelar")             # Cambió al número 4
        
        opcion = input("Elige una opción: ")
        
        # ----------------------------------------------------
        # OPCIÓN 1: AGREGAR PRODUCTO (AHORA CON VALIDACIONES)
        # ----------------------------------------------------
        if opcion == "1":
            codigo_buscar = input("Ingresa el código del producto (ej. P001): ").upper()
            
            # (FASE 1) Buscamos el producto
            producto_encontrado = None 
            for p in productos_prueba:
                if p["codigo"] == codigo_buscar:
                    producto_encontrado = p
                    break 
                    
            if producto_encontrado is None:
                print("Error: El código de producto no existe.")
            else:
                # NUEVO EN FASE 2: Protegemos el programa con try/except
                try:
                    cantidad_texto = input(f"¿Cuántas unidades de '{producto_encontrado['nombre']}' deseas?: ")
                    cantidad = int(cantidad_texto) 
                    
                    # NUEVO EN FASE 2: Validamos que no ponga 0 o negativos
                    if cantidad <= 0:
                        print("Error: Debes ingresar al menos 1 unidad.")
                        
                    # NUEVO EN FASE 2: Validamos el stock (Requerimiento 3)
                    elif producto_encontrado["stock"] < cantidad:
                        print(f"Error: No hay suficiente stock. Solo quedan {producto_encontrado['stock']} unidades.")
                        
                    else:
                        # Si pasa todas las pruebas, lo agregamos al carrito
                        subtotal = cantidad * producto_encontrado["precio"]
                        
                        item = {
                            "codigo": producto_encontrado["codigo"],
                            "nombre": producto_encontrado["nombre"],
                            "cantidad": cantidad,
                            "precio_unit": producto_encontrado["precio"],
                            "subtotal": subtotal
                        }
                        
                        carrito.append(item)
                        print("¡Producto agregado al carrito con éxito!")
                        
                except ValueError:
                    # Si intenta escribir letras como "dos", el programa no se cierra, viene aquí.
                    print("Error: Por favor ingresa únicamente números enteros.")
                
        # ----------------------------------------------------
        # OPCIÓN 2: MOSTRAR CARRITO (AHORA CALCULA IVA Y TOTAL)
        # ----------------------------------------------------
        elif opcion == "2":
            print("\n--- TU CARRITO ACTUAL ---")
            
            if len(carrito) == 0:
                print("El carrito está vacío.")
            else:
                # NUEVO EN FASE 2: Variables para llevar la suma de toda la compra
                suma_subtotal = 0
                
                # Imprimimos los productos y vamos sumando sus subtotales
                for item in carrito:
                    print(f"{item['cantidad']}x {item['nombre']} - Precio: Q{item['precio_unit']} - Subtotal: Q{item['subtotal']}")
                    suma_subtotal = suma_subtotal + item["subtotal"]
                
                # NUEVO EN FASE 2: Cálculos matemáticos requeridos (Requerimiento 6)
                # Multiplicamos por 0.12 para sacar el IVA y usamos round() para dejar solo 2 decimales
                iva = round(suma_subtotal * 0.12, 2)
                total = round(suma_subtotal + iva, 2)
                
                print("-" * 30)
                print(f"Subtotal: Q{suma_subtotal}")
                print(f"IVA (12%): Q{iva}")
                print(f"TOTAL A PAGAR: Q{total}")
                
        # ----------------------------------------------------
        # OPCIÓN 3: QUITAR PRODUCTO (NUEVO EN FASE 2)
        # ----------------------------------------------------
        elif opcion == "3":
            if len(carrito) == 0:
                print("El carrito ya está vacío, no hay nada que quitar.")
            else:
                codigo_quitar = input("Ingresa el código del producto a quitar: ").upper()
                
                # Variable para saber si logramos borrar algo
                borrado = False 
                
                # Usamos un for con un contador manual 'i' para saber en qué posición estamos
                for i in range(len(carrito)):
                    if carrito[i]["codigo"] == codigo_quitar:
                        # La función pop() elimina el elemento en la posición 'i'
                        carrito.pop(i)
                        print("Producto eliminado del carrito exitosamente.")
                        borrado = True
                        break # Rompemos el ciclo porque ya lo borramos
                
                if not borrado:
                    print("Ese producto no se encuentra en tu carrito.")

        # ----------------------------------------------------
        # OPCIÓN 4: SALIR / CANCELAR
        # ----------------------------------------------------
        elif opcion == "4":
            print("Cancelando venta y saliendo del menú...")
            break 
            
        else:
            print("Opción incorrecta. Escribe 1, 2, 3 o 4.")

# Arrancamos la Fase 2
iniciar_nueva_venta_fase2()