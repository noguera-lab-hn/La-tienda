# ==============================================================================
#                           MÓDULO DE VENTAS
#                       BRYAN JOSUE NOGUERA MOLINA
#                               2/6/2026
# ==============================================================================

import os
import json
from datetime import datetime

# ==============================================================================
# FUNCIONES AUXILIARES PARA LEER Y GUARDAR JSON
# ==============================================================================

def cargar_datos(ruta):
    # Intentamos abrir el archivo. Si no existe, devolvemos una lista vacía.
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(ruta, datos):
    # Asegurarnos de que la carpeta 'datos' exista antes de guardar
    if not os.path.exists("datos"):
        os.makedirs("datos")
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar en {ruta}: {e}")


# ==============================================================================
# FUNCIÓN PARA CREAR EL ARCHIVO .TXT
# ==============================================================================
def generar_factura_txt(venta_final):
    # Validamos si la carpeta "facturas" NO existe en la computadora
    if not os.path.exists("facturas"):
        os.makedirs("facturas")
        
    # Armamos el nombre del archivo usando el ID de la venta.
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


# ==============================================================================
# FUNCIÓN PRINCIPAL DEL MÓDULO DE VENTAS
# ==============================================================================
def iniciar_nueva_venta():
    print("--- INICIANDO NUEVA VENTA ---")
    
    # 1. Cargamos las bases de datos REALES al iniciar la transacción
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
        
        # ----------------------------------------------------
        # OPCIÓN 1: AGREGAR PRODUCTO 
        # ----------------------------------------------------
        if opcion == "1":
            codigo_buscar = input("Ingresa el código del producto (ej. P001): ").upper().strip()
            
            producto_encontrado = None 
            # Ahora iteramos sobre el inventario real 'productos'
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
                
        # ----------------------------------------------------
        # OPCIÓN 2: MOSTRAR CARRITO Y TOTALES
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
        # OPCIÓN 3: QUITAR PRODUCTO
        # ----------------------------------------------------
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

        # ----------------------------------------------------
        # OPCIÓN 4: CONFIRMAR VENTA Y GUARDAR
        # ----------------------------------------------------
        elif opcion == "4":
            if len(carrito) == 0:
                print("No puedes confirmar una venta porque el carrito está vacío.")
            else:
                print("\nProcesando la venta...")
                
                suma_subtotal = sum(item["subtotal"] for item in carrito)
                iva = round(suma_subtotal * 0.12, 2)
                total = round(suma_subtotal + iva, 2)
                
                # LA SOLUCIÓN AL PROBLEMA DE LA FACTURA ESTÁ AQUÍ:
                # Calculamos el ID basándonos en la longitud real del archivo JSON de ventas
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
                
                # Insertamos la nueva venta en la lista en memoria RAM
                ventas.append(nueva_venta)
                
                # 2. ESCRITURA: Sobrescribimos los JSON con los nuevos datos permanentemente
                guardar_datos("datos/ventas.json", ventas)
                guardar_datos("datos/productos.json", productos)
                
                generar_factura_txt(nueva_venta)
                
                print("¡Venta completada, inventario actualizado y datos guardados con éxito!")
                break 

        # ----------------------------------------------------
        # OPCIÓN 5: CANCELAR Y SALIR 
        # ----------------------------------------------------
        elif opcion == "5":
            print("Venta cancelada. No se ha modificado el inventario.")
            break 
            
        else:
            print("Opción incorrecta. Escribe del 1 al 5.")
            
            
if __name__ == "__main__":
    iniciar_nueva_venta()