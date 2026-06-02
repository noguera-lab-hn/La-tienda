import json
def eliminar_cliente():
    with open("clientes.json", "r", encoding="utf-8") as archivo:
        clientes = json.load(archivo)

    #with open("ventas.json", "r", encoding="utf-8") as archivo:
     #   ventas = json.load(archivo)

    nitAeliminar = input("Ingrese NIT del cliente a eliminar: ")
    #for venta in ventas:
     #   if venta["NIT"] == nitAeliminar:
      #      print("No se puede eliminar el cliente porque tiene ventas registradas.")
       #     return

    encontrado = False
    clientes_nuevos = []
    for cliente in clientes:
        if cliente["NIT"] == nitAeliminar:
            encontrado = True
        else:
            clientes_nuevos.append(cliente)

    if not encontrado:
        print("No existe un cliente con ese NIT.")
        return

    with open("clientes.json", "w", encoding="utf-8") as archivo:
        json.dump(clientes_nuevos, archivo, indent=2, ensure_ascii=False)

    print("Cliente eliminado exitosamente.")