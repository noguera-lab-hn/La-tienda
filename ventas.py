# ==============================================================================
#                           MODULO DE VENTAS
#                       BRYAN jOSUE NOGUERA MOLINA
#                               30/5/2026
# ==============================================================================






# FASE 3: CONFIRMACIÓN DE VENTA, DESCUENTO DE STOCK Y FACTURA TXT

# FASE 3: Importamos 'os' para crear carpetas en la computadora
import os
# FASE 3: Importamos 'datetime' para obtener la fecha y hora de la compra
from datetime import datetime

# Base de datos "de mentira" para pruebas
productos_prueba = [
    {"codigo": "P001", "nombre": "Azúcar 1lb", "precio": 6.50, "stock": 24},
    {"codigo": "P002", "nombre": "Frijol Negro", "precio": 8.00, "stock": 15}
]

# NUEVO EN FASE 3: Simulamos el archivo ventas.json para saber cuántas ventas llevamos
ventas_prueba = []

# ==============================================================================
# NUEVA FUNCIÓN AUXILIAR DE LA FASE 3: CREAR EL ARCHIVO .TXT
# ==============================================================================
def generar_factura_txt(venta_final):
    # Validamos si la carpeta "facturas" NO existe en la computadora
    if not os.path.exists("facturas"):
        # Si no existe, le pedimos al sistema operativo que la cree
        os.makedirs("facturas")
        
    # Armamos el nombre del archivo usando el ID de la venta. Ej: "facturas/factura_V0001.txt"
    ruta_archivo = f"facturas/factura_{venta_final['id_venta']}.txt"
    
    # Intentamos crear y escribir el archivo
    try:
        # 'w' significa Write (escribir). encoding="utf-8" permite guardar tildes y eñes sin error.
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            # Empezamos a escribir línea por línea dentro del archivo de texto
            archivo.write("=== TU TIENDA ===\n") # \n significa 'salto de línea' (como presionar Enter)
            archivo.write(f"Factura No:   {venta_final['id_venta']}\n")
            archivo.write(f"Fecha y Hora: {venta_final['fecha']}\n")
            archivo.write(f"NIT Cliente:  {venta_final['nit_cliente']}\n")
            archivo.write("--------------------------------\n")
            
            # Recorremos el carrito guardado en la venta para imprimir cada producto
            for item in venta_final['items']:
                archivo.write(f"{item['cantidad']}x {item['nombre']} - Q{item['subtotal']}\n")
                
            archivo.write("--------------------------------\n")
            archivo.write(f"Subtotal:  Q{venta_final['subtotal']}\n")
            archivo.write(f"IVA (12%): Q{venta_final['iva']}\n")
            archivo.write(f"TOTAL:     Q{venta_final['total']}\n")
            archivo.write("=== ¡GRACIAS POR SU COMPRA! ===\n")
            
        print(f"\n¡Éxito! La factura física se ha guardado en: {ruta_archivo}")
        
    except Exception as e:
        print(f"Error al intentar crear el archivo físico: {e}")


# ==============================================================================
# FUNCIÓN PRINCIPAL DEL MÓDULO DE VENTAS
# ==============================================================================
def iniciar_nueva_venta_fase3():
    print("--- INICIANDO NUEVA VENTA ---")
    
    # (FASE 1) Pedimos NIT
    nit_cliente = input("Ingrese NIT del cliente (Deje vacío para CF): ")
    if nit_cliente == "":
        nit_cliente = "CF"
        
    carrito = []
    
    # Bucle infinito del menú
    while True:
        print("\n--- MENÚ DE VENTA ---")
        print("1. Agregar producto")
        print("2. Mostrar carrito (con totales)")
        print("3. Quitar producto")
        print("4. Confirmar venta y Facturar") # NUEVO EN FASE 3
        print("5. Cancelar venta en curso")    # NUEVO EN FASE 3
        
        opcion = input("Elige una opción: ")
        
        # ----------------------------------------------------
        # OPCIÓN 1: AGREGAR PRODUCTO (Fases 1 y 2)
        # ----------------------------------------------------
        if opcion == "1":
            codigo_buscar = input("Ingresa el código del producto (ej. P001): ").upper()
            
            producto_encontrado = None 
            for p in productos_prueba:
                if p["codigo"] == codigo_buscar:
                    producto_encontrado = p
                    break 
                    
            if producto_encontrado is None:
                print("Error: El código de producto no existe.")
            else:
                try:
                    cantidad_texto = input(f"¿Cuántas unidades de '{producto_encontrado['nombre']}' deseas?: ")
                    cantidad = int(cantidad_texto) 
                    
                    if cantidad <= 0:
                        print("Error: Debes ingresar al menos 1 unidad.")
                    elif producto_encontrado["stock"] < cantidad:
                        print(f"Error: No hay suficiente stock. Solo quedan {producto_encontrado['stock']} unidades.")
                    else:
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
                    print("Error: Por favor ingresa únicamente números enteros.")
                
        # ----------------------------------------------------
        # OPCIÓN 2: MOSTRAR CARRITO Y TOTALES (Fase 2)
        # ----------------------------------------------------
        elif opcion == "2":
            print("\n--- TU CARRITO ACTUAL ---")
            if len(carrito) == 0:
                print("El carrito está vacío.")
            else:
                suma_subtotal = 0
                for item in carrito:
                    print(f"{item['cantidad']}x {item['nombre']} - Precio: Q{item['precio_unit']} - Subtotal: Q{item['subtotal']}")
                    suma_subtotal = suma_subtotal + item["subtotal"]
                
                iva = round(suma_subtotal * 0.12, 2)
                total = round(suma_subtotal + iva, 2)
                
                print("-" * 30)
                print(f"Subtotal: Q{suma_subtotal}")
                print(f"IVA (12%): Q{iva}")
                print(f"TOTAL A PAGAR: Q{total}")
                
        # ----------------------------------------------------
        # OPCIÓN 3: QUITAR PRODUCTO (Fase 2)
        # ----------------------------------------------------
        elif opcion == "3":
            if len(carrito) == 0:
                print("El carrito ya está vacío.")
            else:
                codigo_quitar = input("Ingresa el código del producto a quitar: ").upper()
                borrado = False 
                
                for i in range(len(carrito)):
                    if carrito[i]["codigo"] == codigo_quitar:
                        carrito.pop(i)
                        print("Producto eliminado del carrito exitosamente.")
                        borrado = True
                        break 
                
                if not borrado:
                    print("Ese producto no se encuentra en tu carrito.")

        # ----------------------------------------------------
        # OPCIÓN 4: CONFIRMAR VENTA (NUEVO EN FASE 3)
        # ----------------------------------------------------
        elif opcion == "4":
            if len(carrito) == 0:
                print("No puedes confirmar una venta porque el carrito está vacío.")
            else:
                print("\nProcesando la venta...")
                
                # Paso A: Volvemos a calcular los totales exactos
                suma_subtotal = sum(item["subtotal"] for item in carrito)
                iva = round(suma_subtotal * 0.12, 2)
                total = round(suma_subtotal + iva, 2)
                
                # Paso B: Generar ID único (Ej: V0001). zfill(4) rellena con ceros a la izquierda
                siguiente_numero = len(ventas_prueba) + 1
                id_venta = f"V{str(siguiente_numero).zfill(4)}"
                
                # Paso C: Obtener fecha y hora real
                fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Paso D: Restar el stock del inventario principal permanentemente (Requerimiento 7)
                for item in carrito:
                    for p in productos_prueba:
                        if p["codigo"] == item["codigo"]:
                            # Le restamos al stock actual la cantidad que se acaba de vender
                            p["stock"] = p["stock"] - item["cantidad"]
                            break # Rompemos el ciclo interno porque ya encontramos el producto
                            
                # Paso E: Crear el registro oficial de la venta
                nueva_venta = {
                    "id_venta": id_venta,
                    "fecha": fecha_actual,
                    "nit_cliente": nit_cliente,
                    "items": carrito,
                    "subtotal": suma_subtotal,
                    "iva": iva,
                    "total": total
                }
                
                # Agregamos esta venta a nuestra lista histórica de ventas
                ventas_prueba.append(nueva_venta)
                
                # Paso F: Generar el archivo TXT llamando a nuestra nueva función
                generar_factura_txt(nueva_venta)
                
                print("¡Venta completada y stock descontado con éxito!")
                
                # Salimos del bucle porque la venta ya terminó
                break 

        # ----------------------------------------------------
        # OPCIÓN 5: CANCELAR Y SALIR (Fase 1 y 3)
        # ----------------------------------------------------
        elif opcion == "5":
            # Requerimiento 8: Cancelar sin afectar registros ni stock
            print("Venta cancelada. No se ha modificado el inventario.")
            break 
            
        else:
            print("Opción incorrecta. Escribe del 1 al 5.")

# Arrancamos el programa
iniciar_nueva_venta_fase3()

# Solo para comprobar que el código funciona, imprimiremos el inventario al final
# para que veas cómo el stock sí bajó después de que procesaste la venta.
print("\n--- INVENTARIO DESPUÉS DE LA VENTA ---")
for p in productos_prueba:
    print(f"{p['nombre']} - Stock restante: {p['stock']}")