import json
def listar_clientes():
    with open("clientes.json","r",encoding="utf-8") as archivo:
        lista = json.load(archivo)

    print("\nESTOS SON LOS CLIENTES REGISTRADOS")
    
    for cliente in lista:
        print("\nNIT", cliente["NIT"])
        print("Nombre", cliente["Nombre"])
        print("Telefono", cliente["Telefono"])
        print("Correo", cliente["Correo"])