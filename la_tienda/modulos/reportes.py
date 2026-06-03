from datetime import datetime
from archivos import cargar_datos


def reporte_stock_bajo():
    
    # Revisa el inventario y muestra en pantalla los productos cuyo stock actual es menor o igual al permitido.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # Nada (imprime los resultados directamente en la consola).
    
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
    
    # Solicita el NIT de un cliente y muestra todas las compras que ha realizado, los productos llevados y el total gastado.
    
    # Recibe:
        # Nada (solicita el NIT al usuario durante la ejecución).
        
    # Devuelve:
        # Nada (imprime el historial y el resumen financiero en la consola).
    
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


def reporte_ventas_dia():
    
    # Calcula y muestra el total de ingresos y la cantidad de transacciones realizadas en el día actual.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # Nada (imprime los totales del día en la consola).
    
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
    
    # Solicita una fecha de inicio y una de fin, filtrando las ventas para mostrar el total de ingresos en ese periodo.
    
    # Recibe:
        # Nada (solicita las fechas por consola al usuario).
        
    # Devuelve:
        # Nada (imprime el resumen del rango de fechas en la consola).
    
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


def reporte_top_5_productos():
    
    # Procesa el registro de ventas para determinar cuáles son los 5 productos con mayor cantidad de unidades vendidas.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # Nada (imprime una tabla con el Top 5 en la consola).
    
    print("\n--- REPORTE: TOP 5 PRODUCTOS MÁS VENDIDOS ---")
    ventas = cargar_datos("datos/ventas.json")
    
    if not ventas:
        print("Aún no hay ventas registradas.")
        return
        
    conteo_productos = {}
    nombres_productos = {} 
    
    for venta in ventas:
        for item in venta["items"]:
            codigo = item["codigo"]
            cantidad = item["cantidad"]
            
            if codigo in conteo_productos:
                conteo_productos[codigo] += cantidad
            else:
                conteo_productos[codigo] = cantidad
                nombres_productos[codigo] = item["nombre"]
                
    lista_conteo = []
    for codigo in conteo_productos:
        lista_conteo.append([codigo, conteo_productos[codigo]])
        
    def criterio_de_orden(elemento):
        return elemento[1]
        
    lista_conteo.sort(key=criterio_de_orden, reverse=True)
    
    print(f"{'POSICIÓN':<10} | {'CÓDIGO':<8} | {'NOMBRE':<20} | {'UNIDADES VENDIDAS'}")
    print("-" * 65)
    
    posicion = 1
    for item in lista_conteo[:5]:
        codigo_ganador = item[0]
        cantidad_ganadora = item[1]
        nombre_ganador = nombres_productos[codigo_ganador]
        
        print(f"#{posicion:<9} | {codigo_ganador:<8} | {nombre_ganador:<20} | {cantidad_ganadora}")
        posicion += 1


def reporte_cierre_caja():
    
    # Genera un desglose completo del día, incluyendo transacciones, ingresos totales, ticket promedio y mercadería vendida.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # Nada (imprime el resumen financiero del cierre de caja en la consola).
    
    print("\n--- REPORTE: CIERRE DE CAJA DEL DÍA ---")
    ventas = cargar_datos("datos/ventas.json")
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    
    total_dinero = 0
    total_transacciones = 0
    
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


def modulo_reportes():
    
    # Muestra el menú interactivo para acceder a los distintos reportes del sistema y gestiona la elección del usuario.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # Nada (mantiene al usuario en un bucle hasta que decida salir).
    
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