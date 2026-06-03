#               MODULO DE VENTAS
#            Bryan Josue Noguera Molina
#                   23/5/2026
import os
from datetime import datetime
from archivos import cargar_datos, guardar_datos


def generar_factura_txt(venta_final):
    
    # Genera un archivo de texto plano (.txt) que sirve como comprobante o factura física de la venta realizada, 
    # creando la carpeta 'facturas' si esta no existe.
    
    # Recibe:
        # venta_final (dict): Un diccionario que contiene todos los datos de la venta confirmada 
                            # (ID, fecha, cliente, productos llevados, subtotales y total).
        
    # Devuelve:
        # Nada (crea y guarda el archivo en el sistema e imprime un mensaje en consola).
    
    if not os.path.exists("facturas"):
        os.makedirs("facturas")
        
    ruta_archivo = f"facturas/factura_{venta_final['id_venta']}.txt"
    
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("=== TU TIENDA ===\n")
            archivo.write(f"Factura No:   {venta_final['id_venta']}\n")
            archivo.write(f"Fecha y Hora: {venta_final['fecha']}\n")
            archivo.write(f"NIT Cliente:  {venta_final['nit_cliente']}\n")
            archivo.write("--------------------------------\n")
            
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


def iniciar_nueva_venta():
    
    # Inicia el proceso interactivo para registrar una nueva venta. Permite al usuario gestionar un carrito de compras 
    # (agregar o quitar productos), calcula automáticamente los totales e impuestos (IVA del 12%), descuenta el stock 
    # del inventario y guarda la transacción final.
    
    # Recibe:
        # Nada (interactúa con el usuario a través de la consola).
        
    # Devuelve:
        # Nada (completa o cancela la venta y termina su ejecución).
    
    print("--- INICIANDO NUEVA VENTA ---")
    
    productos = cargar_datos("datos/productos.json")
    ventas = cargar_datos("datos/ventas.json")
    
    nit_cliente = input("Ingrese NIT del cliente (Deje vacío para CF): ").strip()
    if nit_cliente == "":
        nit_cliente = "CF"
        
    carrito = []
    
    while True:
        print("\n--- MENÚ DE VENTA ---")
        print("1. Agregar producto")
        print("2. Mostrar carrito (con totales)")
        print("3. Quitar producto")
        print("4. Confirmar venta y Facturar") 
        print("5. Cancelar venta en curso")    
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            codigo_buscar = input("Ingresa el código del producto (ej. P001): ").upper().strip()
            
            producto_encontrado = None 
            for p in productos:
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
                
        elif opcion == "3":
            if len(carrito) == 0:
                print("El carrito ya está vacío.")
            else:
                codigo_quitar = input("Ingresa el código del producto a quitar: ").upper().strip()
                borrado = False 
                
                for i in range(len(carrito)):
                    if carrito[i]["codigo"] == codigo_quitar:
                        carrito.pop(i)
                        print("Producto eliminado del carrito exitosamente.")
                        borrado = True
                        break 
                
                if not borrado:
                    print("Ese producto no se encuentra en tu carrito.")

        elif opcion == "4":
            if len(carrito) == 0:
                print("No puedes confirmar una venta porque el carrito está vacío.")
            else:
                print("\nProcesando la venta...")
                
                suma_subtotal = sum(item["subtotal"] for item in carrito)
                iva = round(suma_subtotal * 0.12, 2)
                total = round(suma_subtotal + iva, 2)
                
                siguiente_numero = len(ventas) + 1
                id_venta = f"V{str(siguiente_numero).zfill(4)}"
                
                fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                for item in carrito:
                    for p in productos:
                        if p["codigo"] == item["codigo"]:
                            p["stock"] = p["stock"] - item["cantidad"]
                            break 
                            
                nueva_venta = {
                    "id_venta": id_venta,
                    "fecha": fecha_actual,
                    "nit_cliente": nit_cliente,
                    "items": carrito,
                    "subtotal": suma_subtotal,
                    "iva": iva,
                    "total": total
                }
                
                ventas.append(nueva_venta)
                
                guardar_datos("datos/ventas.json", ventas)
                guardar_datos("datos/productos.json", productos)
                
                generar_factura_txt(nueva_venta)
                
                print("¡Venta completada, inventario actualizado y datos guardados con éxito!")
                break 

        elif opcion == "5":
            print("Venta cancelada. No se ha modificado el inventario.")
            break 
            
        else:
            print("Opción incorrecta. Escribe del 1 al 5.")
            
            
if __name__ == "__main__":
    iniciar_nueva_venta()