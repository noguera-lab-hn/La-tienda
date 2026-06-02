import json 
def registrarDatos():
    # abrimos el archivo json y si no exite se crea una nueva
    try:
        with open("clientes.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)
    except FileNotFoundError:# manejo de error
        # Si el archivo no existe empezamos con una lista vacía
        clientes = []
    print("\nIngrese los datos del cliente")
    nit = input("NIT: ")
    for cliente in clientes:
        if cliente["NIT"] == nit:
            print("\nEste nit ya ha sido registrado con los siguientes datos")
            print("Nombre", cliente["Nombre"])
            print("Telefono", cliente["Telefono"])
            print("Correo", cliente["Correo"])
            return

    nombre = input("Nombre: ")
    telefono = (input("Telefono: "))
    correo = input("Correo: ")

    nueva_persona = {
        "NIT": nit,
        "Nombre": nombre,
        "Telefono": telefono,
        "Correo": correo
    }
    clientes.append(nueva_persona)

    with open("clientes.json", "w", encoding="utf-8") as archivo:
        json.dump(clientes, archivo, indent=2)
    print("\nDatos añadidos correctamente ")