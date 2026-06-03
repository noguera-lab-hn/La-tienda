# ==============================================================================
#                           MÓDULO DE REPORTES
#                       BRYAN JOSUE NOGUERA MOLINA
#                               2/6/2026
# ==============================================================================

from datetime import datetime
# Importamos nuestra función de lectura centralizada desde el nuevo motor de base de datos
from archivos import cargar_datos

# REPORTES DE LA FASE 1 (Stock e Historial)
# -------------------------------------------

def reporte_stock_bajo():
    print("\n--- REPORTE: PRODUCTOS CON STOCK BAJO ---")
    productos = cargar_datos("datos/productos.json")
    hay_alertas = False
    
    for p in productos:
        if p["stock"] <= p["stock_minimo"]:
            print(f"   ALERTA - [{p['codigo']}] {p['nombre']}")
            print(f"   Stock actual: {p['stock']} | Mínimo permitido: {p['stock_minimo']}")
            hay_alertas = True
            
    if not hay_alertas:
        print("Todo está en orden. Ningún producto tiene stock bajo.")
    print("-" * 45)

def reporte_historial_cliente():
    print("\n--- REPORTE: HISTORIAL DE COMPRAS DE CLIENTE ---")
    nit_buscar = input("Ingrese el NIT del cliente a consultar: ").strip()
    ventas = cargar_datos("datos/ventas.json")
    
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
# ---------------------------------

def reporte_ventas_dia():
    print("\n--- REPORTE: VENTAS DEL DÍA ---")
    ventas = cargar_datos("datos/ventas.json")
    fecha_hoy_texto = datetime.now().strftime("%Y-%m-%d")
    
    total_dinero = 0
    total_transacciones = 0
    
    for venta in ventas:
        if venta["fecha"][:10] == fecha_hoy_texto:
            total_dinero += venta["total"]
            total_transacciones += 1
            
    print(f"Fecha consultada: {fecha_hoy_texto}")
    print(f"Cantidad de transacciones hoy: {total_transacciones}")
    print(f"Monto total vendido: Q{total_dinero}")
    print("-" * 40)

def reporte_rango_fechas():
    print("\n--- REPORTE: VENTAS POR RANGO DE FECHAS ---")
    print("Formato requerido: AAAA-MM-DD (Ejemplo: 2026-05-01)")
    
    fecha_inicio_txt = input("Ingrese la fecha de INICIO: ").strip()
    fecha_fin_txt = input("Ingrese la fecha de FIN: ").strip()
    
    try:
        formato = "%Y-%m-%d"
        fecha_inicio_obj = datetime.strptime(fecha_inicio_txt, formato)
        fecha_fin_obj = datetime.strptime(fecha_fin_txt, formato)
        
        ventas = cargar_datos("datos/ventas.json")
        total_dinero = 0
        total_transacciones = 0
        
        for venta in ventas:
            fecha_venta_txt_corta = venta["fecha"][:10]
            fecha_venta_obj = datetime.strptime(fecha_venta_txt_corta, formato)
            
            if fecha_inicio_obj <= fecha_venta_obj <= fecha_fin_obj:
                total_dinero += venta["total"]
                total_transacciones += 1
                
        print("\n" + "=" * 40)
        print(f"Desde: {fecha_inicio_txt} | Hasta: {fecha_fin_txt}")
        print(f"Transacciones encontradas: {total_transacciones}")
        print(f"Total ingresado: Q{total_dinero}")
        print("=" * 40)
        
    except ValueError:
        print("Error: El formato de la fecha es incorrecto. Debe ser AAAA-MM-DD.")


# REPORTES DE LA FASE 3 (Análisis y Cierre)
# ---------------------------------------------

def reporte_top_5_productos():
    print("\n--- REPORTE: TOP 5 PRODUCTOS MÁS VENDIDOS ---")
    ventas = cargar_datos("datos/ventas.json")
    
    if not ventas:
        print("Aún no hay ventas registradas.")
        return
        
    # Usamos un diccionario vacío como nuestra libreta de apuntes para agrupar
    # Se verá así: {"P001": 5, "P002": 10}
    conteo_productos = {}
    nombres_productos = {} # Para recordar el nombre de cada código
    
    for venta in ventas:
        for item in venta["items"]:
            codigo = item["codigo"]
            cantidad = item["cantidad"]
            
            # Si el código ya está en nuestra libreta, le sumamos la nueva cantidad
            if codigo in conteo_productos:
                conteo_productos[codigo] += cantidad
            # Si es la primera vez que vemos este código, lo creamos
            else:
                conteo_productos[codigo] = cantidad
                nombres_productos[codigo] = item["nombre"]
                
    # Transformamos nuestra libreta en una lista para poder ordenarla
    # Cada elemento será una pequeña lista así: [codigo, cantidad_total]
    lista_conteo = []
    for codigo in conteo_productos:
        lista_conteo.append([codigo, conteo_productos[codigo]])
        
    # Función auxiliar muy sencilla que le dice a Python cómo ordenar nuestra lista
    # Retorna la posición 1 (la cantidad_total) para usarla como criterio
    def criterio_de_orden(elemento):
        return elemento[1]
        
    # Ordenamos la lista usando nuestro criterio, y reverse=True para que sea de mayor a menor
    lista_conteo.sort(key=criterio_de_orden, reverse=True)
    
    print(f"{'POSICIÓN':<10} | {'CÓDIGO':<8} | {'NOMBRE':<20} | {'UNIDADES VENDIDAS'}")
    print("-" * 65)
    
    # Recorremos solo los primeros 5 elementos usando un recorte de lista [:5]
    posicion = 1
    for item in lista_conteo[:5]:
        codigo_ganador = item[0]
        cantidad_ganadora = item[1]
        nombre_ganador = nombres_productos[codigo_ganador]
        
        print(f"#{posicion:<9} | {codigo_ganador:<8} | {nombre_ganador:<20} | {cantidad_ganadora}")
        posicion += 1


def reporte_cierre_caja():
    print("\n--- REPORTE: CIERRE DE CAJA DEL DÍA ---")
    ventas = cargar_datos("datos/ventas.json")
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    
    total_dinero = 0
    total_transacciones = 0
    
    # Reutilizamos la lógica del Top 5 para saber qué se vendió específicamente hoy
    productos_hoy = {}
    
    for venta in ventas:
        if venta["fecha"][:10] == fecha_hoy:
            total_dinero += venta["total"]
            total_transacciones += 1
            
            for item in venta["items"]:
                nombre = item["nombre"]
                cantidad = item["cantidad"]
                
                if nombre in productos_hoy:
                    productos_hoy[nombre] += cantidad
                else:
                    productos_hoy[nombre] = cantidad
                    
    if total_transacciones == 0:
        print("No se registraron ventas en el día de hoy.")
        return
        
    # Calculamos el ticket promedio (Total de dinero dividido entre la cantidad de facturas)
    ticket_promedio = round(total_dinero / total_transacciones, 2)
    
    print("=" * 50)
    print("RESUMEN FINANCIERO")
    print(f"Fecha: {fecha_hoy}")
    print(f"Transacciones (Facturas emitidas): {total_transacciones}")
    print(f"Ingresos Totales: Q{total_dinero}")
    print(f"Ticket Promedio (Gasto por cliente): Q{ticket_promedio}")
    print("\nRESUMEN DE MERCADERÍA VENDIDA HOY")
    print("-" * 50)
    
    for nombre_producto in productos_hoy:
        print(f"- {productos_hoy[nombre_producto]} unidades de {nombre_producto}")
    print("=" * 50)



# MENÚ PRINCIPAL DEL MÓDULO DE REPORTES
# --------------------------------------

def modulo_reportes():
    while True:
        print("\n=== MÓDULO DE REPORTES ===")
        print("1. Top 5 productos más vendidos")
        print("2. Total de ventas del día")
        print("3. Total de ventas en rango de fechas")
        print("4. Productos con stock bajo")
        print("5. Historial de compras de un cliente")
        print("6. Cierre de caja del día")
        print("0. Volver al menú principal")
        
        opcion = input("\nSeleccione un reporte: ").strip()
        
        if opcion == "1":
            reporte_top_5_productos()
        elif opcion == "2":
            reporte_ventas_dia()
        elif opcion == "3":
            reporte_rango_fechas()
        elif opcion == "4":
            reporte_stock_bajo()
        elif opcion == "5":
            reporte_historial_cliente()
        elif opcion == "6":
            reporte_cierre_caja()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")