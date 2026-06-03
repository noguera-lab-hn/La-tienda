# ==============================================================================
#                           MODULO DE REPORTES
#                       BRYAN jOSUE NOGUERA MOLINA
#                               2/6/2026
# ==============================================================================

# Importamos json para leer los archivos reales de la base de datos
import json
# Importamos datetime para manejar y comparar las fechas de los reportes
from datetime import datetime

# --------------------------------
# FUNCIONES AUXILIARES DE LECTURA
# ---------------------------------

# Esta función lee cualquier archivo JSON y lo convierte en lista de Python.
# Si el archivo no existe, devuelve una lista vacía para que el programa no colapse.
def cargar_datos_json(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


# REPORTES DE LA FASE 1 (Ahora conectados a los JSON reales)
# ----------------------------------------------------------

# Muestra los productos cuyo stock actual es menor o igual al mínimo permitido.
def reporte_stock_bajo():
    print("\n--- REPORTE: PRODUCTOS CON STOCK BAJO ---")
    
    # Cargamos el inventario real justo en el momento de pedir el reporte
    productos = cargar_datos_json("datos/productos.json")
    hay_alertas = False
    
    for p in productos:
        if p["stock"] <= p["stock_minimo"]:
            print(f"ALERTA - [{p['codigo']}] {p['nombre']}")
            print(f"   Stock actual: {p['stock']} | Mínimo permitido: {p['stock_minimo']}")
            hay_alertas = True
            
    if not hay_alertas:
        print("Todo está en orden. Ningún producto tiene stock bajo.")
    print("-" * 45)


# Muestra todas las compras que ha realizado un cliente específico por su NIT.
def reporte_historial_cliente():
    print("\n--- REPORTE: HISTORIAL DE COMPRAS DE CLIENTE ---")
    nit_buscar = input("Ingrese el NIT del cliente a consultar: ").strip()
    
    # Cargamos el historial de ventas real
    ventas = cargar_datos_json("datos/ventas.json")
    
    total_gastado = 0
    compras_realizadas = 0
    
    print(f"\nHistorial para el NIT: {nit_buscar}")
    print("=" * 50)
    
    for venta in ventas:
        if venta["nit_cliente"] == nit_buscar:
            print(f"Factura: {venta['id_venta']} | Fecha: {venta['fecha']}")
            print(f"Total pagado: Q{venta['total']}")
            print("Productos llevados:")
            
            for item in venta["items"]:
                print(f"  - {item['cantidad']}x {item['nombre']}")
            print("-" * 50)
            
            total_gastado += venta["total"]
            compras_realizadas += 1
            
    if compras_realizadas == 0:
        print("Este cliente no tiene compras registradas o el NIT no existe.")
    else:
        print(f"RESUMEN: Este cliente ha realizado {compras_realizadas} compras por un total de Q{total_gastado}")


# REPORTES DE LA FASE 2 (Fechas)
# --------------------------------

# Calcula el total de ventas realizadas en el día de hoy.
def reporte_ventas_dia():
    print("\n--- REPORTE: VENTAS DEL DÍA ---")
    
    ventas = cargar_datos_json("datos/ventas.json")
    
    # Obtenemos la fecha de hoy y nos quedamos solo con la parte "Año-Mes-Día" (los primeros 10 caracteres)
    fecha_hoy_texto = datetime.now().strftime("%Y-%m-%d")
    
    total_dinero = 0
    total_transacciones = 0
    
    for venta in ventas:
        # Extraemos los primeros 10 caracteres de la fecha guardada en el JSON
        fecha_venta_texto = venta["fecha"][:10]
        
        # Si la fecha de la venta es igual a la fecha de hoy
        if fecha_venta_texto == fecha_hoy_texto:
            total_dinero += venta["total"]
            total_transacciones += 1
            
    print(f"Fecha consultada: {fecha_hoy_texto}")
    print(f"Cantidad de transacciones hoy: {total_transacciones}")
    print(f"Monto total vendido: Q{total_dinero}")
    print("-" * 40)


# Calcula el total de ventas en un rango de fechas especificado por el usuario.
def reporte_rango_fechas():
    print("\n--- REPORTE: VENTAS POR RANGO DE FECHAS ---")
    print("Formato requerido: AAAA-MM-DD (Ejemplo: 2026-05-01)")
    
    fecha_inicio_txt = input("Ingrese la fecha de INICIO: ").strip()
    fecha_fin_txt = input("Ingrese la fecha de FIN: ").strip()
    
    try:
        # Convertimos el texto ingresado a objetos de fecha reales (tipo datetime) para poder usar 
        # los signos de mayor que (>) o menor que (<) en Python.
        formato = "%Y-%m-%d"
        fecha_inicio_obj = datetime.strptime(fecha_inicio_txt, formato)
        fecha_fin_obj = datetime.strptime(fecha_fin_txt, formato)
        
        ventas = cargar_datos_json("datos/ventas.json")
        total_dinero = 0
        total_transacciones = 0
        
        for venta in ventas:
            # Extraemos la fecha de la venta y la convertimos también a un objeto datetime
            fecha_venta_txt_corta = venta["fecha"][:10]
            fecha_venta_obj = datetime.strptime(fecha_venta_txt_corta, formato)
            
            # Magia de Python: Comparamos si la fecha de la venta está entre el inicio y el fin
            if fecha_inicio_obj <= fecha_venta_obj <= fecha_fin_obj:
                total_dinero += venta["total"]
                total_transacciones += 1
                
        print("\n" + "=" * 40)
        print(f"Desde: {fecha_inicio_txt} | Hasta: {fecha_fin_txt}")
        print(f"Transacciones encontradas: {total_transacciones}")
        print(f"Total ingresado: Q{total_dinero}")
        print("=" * 40)
        
    except ValueError:
        # Si el usuario escribe "hola" o "05-2026" en lugar del formato correcto, atrapamos el error
        print("Error: El formato de la fecha es incorrecto. Debe ser AAAA-MM-DD.")


# MENÚ PRINCIPAL DEL MÓDULO DE REPORTES
# ---------------------------------------

def iniciar_modulo_reportes():
    while True:
        print("\n=== MÓDULO DE REPORTES ===")
        print("1. Top 5 productos más vendidos (Fase 3)")
        print("2. Total de ventas del día (¡Listo!)")
        print("3. Total de ventas en rango de fechas (¡Listo!)")
        print("4. Productos con stock bajo (¡Listo y conectado!)")
        print("5. Historial de compras de un cliente (¡Listo y conectado!)")
        print("6. Cierre de caja del día (Fase 3)")
        print("0. Salir de reportes")
        
        opcion = input("\nSeleccione un reporte: ").strip()
        
        # Enrutador de opciones
        if opcion == "1":
            print("En construcción...")
        elif opcion == "2":
            reporte_ventas_dia()
        elif opcion == "3":
            reporte_rango_fechas()
        elif opcion == "4":
            reporte_stock_bajo()
        elif opcion == "5":
            reporte_historial_cliente()
        elif opcion == "6":
            print("En construcción...")
        elif opcion == "0":
            print("Saliendo del módulo de reportes...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutamos el programa
iniciar_modulo_reportes()