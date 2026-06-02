import json
def editar_cliente():
    with open("clientes.json", "r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)

    nit = input("Ingrese el NIT del cliente: ")
    encontrado = False

    for cliente in clientes:

        if cliente["NIT"] == nit:

            encontrado = True

            print("\nDatos actuales")
            print("Nombre:", cliente["Nombre"])
            print("Telefono:", cliente["Telefono"])
            print("Correo:", cliente["Correo"])

            nombre_nuevo = input("Nuevo nombre: ")
            telefono_nuevo = input("Nuevo telefono: ")
            correo_nuevo = input("Nuevo correo: ")

            cliente["Nombre"] = nombre_nuevo
            cliente["Telefono"] = telefono_nuevo
            cliente["Correo"] = correo_nuevo

    if not encontrado:
        print("Cliente no encontrado")
        return

    with open("clientes.json", "w", encoding="utf-8") as archivo:
        json.dump(clientes, archivo, indent=2, ensure_ascii=False)

    print("Cliente editado correctamente")

editar_cliente()