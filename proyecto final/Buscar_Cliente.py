import json 

def buscar_cliente():
    with open("clientes.json","r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)

    buscar = input("Ingrese Nombre o NIT: ")
    buscar.lower()

    encontrado = False
    for cliente in clientes:
        if (cliente["Nombre"].lower() == buscar or cliente ["NIT"] == buscar):
            print("\nNIT", cliente["NIT"])
            print("Nombre", cliente["Nombre"])
            print("Telefono", cliente["Telefono"])
            print("Correo", cliente["Correo"])

            encontrado = True
            break

    if encontrado is False:
          print("Cliente no existe")
          