# ==============================================================================
#                           SISTEMA POS "LA TIENDA"
#                                 MAIN.PY
# ==============================================================================

import sys
# 1. TRUCO DE RUTAS: Le decimos a Python que incluya la carpeta "modulos" 
# en su radar. Así, los archivos internos podrán encontrarse entre sí.
sys.path.append("modulos")

# 2. Ahora importamos los 4 módulos principales directamente
import productos
import clientes
import ventas
import reportes

def menu_principal():
    # Este bucle mantiene vivo todo el sistema de Doña Marta
    while True:
        print("\n" + "="*45)
        print("SISTEMA POS 'LA TIENDA' - MENÚ PRINCIPAL")
        print("="*45)
        print("1. Módulo de Productos (Inventario)")
        print("2. Módulo de Clientes")
        print("3. Módulo de Ventas y Facturación")
        print("4. Módulo de Reportes")
        print("0. Cerrar Sistema")
        print("="*45)
        
        opcion = input("\nSeleccione un módulo para ingresar: ").strip()
        
        # Enrutador principal: Llama a las funciones "padre" de cada archivo
        if opcion == "1":
            productos.modulo_productos()
            
        elif opcion == "2":
            clientes.modulo_clientes()
            
        elif opcion == "3":
            ventas.iniciar_nueva_venta()
            
        elif opcion == "4":
            reportes.modulo_reportes()
            
        elif opcion == "0":
            # Si elige 0, rompemos el bucle infinito y el programa termina de ejecutarse
            print("\nGuardando datos y cerrando el sistema... ¡Hasta pronto, Doña Marta!\n")
            break
            
        else:
            print("Opción inválida. Por favor, seleccione un número del 0 al 4.")

# 3. Punto de arranque del programa
if __name__ == "__main__":
    menu_principal()