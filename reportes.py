# ==============================================================================
#                           MODULO DE REPORTES
#                       BRYAN jOSUE NOGUERA MOLINA
#                               1/6/2026
# ==============================================================================

# 1. Bases de datos "de mentira" para probar los reportes sin depender de los JSON aún
productos_prueba = [
    {"codigo": "P001", "nombre": "Azúcar 1lb", "stock": 4, "stock_minimo": 5}, # ¡Stock bajo!
    {"codigo": "P002", "nombre": "Frijol Negro", "stock": 15, "stock_minimo": 10},
    {"codigo": "P003", "nombre": "Jabón de olor", "stock": 2, "stock_minimo": 5} # ¡Stock bajo!
]

ventas_prueba = [
    {"id_venta": "V0001", "fecha": "2026-05-27 10:00:00", "nit_cliente": "12345678", "total": 15.50,
     "items": [{"nombre": "Azúcar 1lb", "cantidad": 2}, {"nombre": "Frijol Negro", "cantidad": 1}]},
     
    {"id_venta": "V0002", "fecha": "2026-05-27 11:30:00", "nit_cliente": "CF", "total": 8.00,
     "items": [{"nombre": "Jabón de olor", "cantidad": 1}]},
     
    {"id_venta": "V0003", "fecha": "2026-05-28 09:15:00", "nit_cliente": "12345678", "total": 13.00,
     "items": [{"nombre": "Azúcar 1lb", "cantidad": 2}]}
]


# FUNCIONES DE LOS REPORTES (FASE 1)
#-----------------------------------

def reporte_stock_bajo(productos):
    # Muestra los productos cuyo stock actual es menor o igual al mínimo permitido.
    print("\n--- REPORTE: PRODUCTOS CON STOCK BAJO ---")
    
    hay_alertas = False
    
    # Recorremos el inventario
    for p in productos:
        if p["stock"] <= p["stock_minimo"]:
            print(f"   ALERTA - [{p['codigo']}] {p['nombre']}")
            print(f"   Stock actual: {p['stock']} | Mínimo permitido: {p['stock_minimo']}")
            hay_alertas = True
            
    if not hay_alertas:
        print("Todo está en orden. Ningún producto tiene stock bajo.")
    print("-" * 45)


def reporte_historial_cliente(ventas):
    # Muestra todas las compras que ha realizado un cliente específico por su NIT.
    print("\n--- REPORTE: HISTORIAL DE COMPRAS DE CLIENTE ---")
    nit_buscar = input("Ingrese el NIT del cliente a consultar: ").strip()
    
    # Variables para sacar un pequeño resumen al final
    total_gastado = 0
    compras_realizadas = 0
    
    print(f"\nHistorial para el NIT: {nit_buscar}")
    print("=" * 50)
    
    for venta in ventas:
        if venta["nit_cliente"] == nit_buscar:
            print(f"Factura: {venta['id_venta']} | Fecha: {venta['fecha']}")
            print(f"Total pagado: Q{venta['total']}")
            print("Productos llevados:")
            
            # Un ciclo dentro de otro ciclo para mostrar qué compró en esa factura específica
            for item in venta["items"]:
                print(f"  - {item['cantidad']}x {item['nombre']}")
            print("-" * 50)
            
            # Sumamos a los contadores
            total_gastado += venta["total"]
            compras_realizadas += 1
            
    if compras_realizadas == 0:
        print("Este cliente no tiene compras registradas o el NIT no existe.")
    else:
        print(f"RESUMEN: Este cliente ha realizado {compras_realizadas} compras por un total de Q{total_gastado}")


# MENÚ PRINCIPAL DEL MÓDULO DE REPORTES
# -----------------------------------------

def iniciar_modulo_reportes_fase1():
    while True:
        print("\n=== MÓDULO DE REPORTES ===")
        print("1. Top 5 productos más vendidos (Fase 3)")
        print("2. Total de ventas del día (Fase 2)")
        print("3. Total de ventas en rango de fechas (Fase 2)")
        print("4. Productos con stock bajo (¡Listo!)")
        print("5. Historial de compras de un cliente (¡Listo!)")
        print("6. Cierre de caja del día (Fase 3)")
        print("0. Salir de reportes")
        
        opcion = input("\nSeleccione un reporte: ").strip()
        
        if opcion == "1":
            print("En construcción...")
        elif opcion == "2":
            print("En construcción...")
        elif opcion == "3":
            print("En construcción...")
        elif opcion == "4":
            # Le pasamos nuestra lista de prueba
            reporte_stock_bajo(productos_prueba)
        elif opcion == "5":
            # Le pasamos nuestra lista de prueba
            reporte_historial_cliente(ventas_prueba)
        elif opcion == "6":
            print("En construcción...")
        elif opcion == "0":
            print("Saliendo del módulo de reportes...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Arrancar la Fase 1
iniciar_modulo_reportes_fase1()