import sys
sys.path.append("modulos")

import productos
import clientes
import ventas
import reportes

def menu_principal():
    while True:
        print("\n" + "SISTEMA POS 'LA TIENDA' - MENÚ PRINCIPAL")
        print("1. Módulo de Productos (Inventario)")
        print("2. Módulo de Clientes")
        print("3. Módulo de Ventas y Facturación")
        print("4. Módulo de Reportes")
        print("0. Cerrar Sistema")
        
        opcion = input("\nSeleccione un módulo para ingresar: ").strip()
        
        if opcion == "1":
            productos.modulo_productos()
            
        elif opcion == "2":
            clientes.modulo_clientes()
            
        elif opcion == "3":
            ventas.iniciar_nueva_venta()
            
        elif opcion == "4":
            reportes.modulo_reportes()
            
        elif opcion == "0":
            print("\nGuardando datos y cerrando el sistema... ¡Hasta pronto, Doña Marta!\n")
            break
            
        else:
            print("Opción inválida. Por favor, seleccione un número del 0 al 4.")

if __name__ == "__main__":
    menu_principal()