from sub_menu import mostrarMenu
from Registrar_cliente import registrarDatos
from Buscar_Cliente import buscar_cliente
from editar_cliente import editar_cliente
from eliminar_cliente import eliminar_cliente
from listado_clientes import listar_clientes

def modulo_clientes():
    while True:
        mostrarMenu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
             registrarDatos()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            editar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            listar_clientes()
        elif opcion == "0":
            break
        else:
            print("\nOpción inválida")