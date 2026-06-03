#               MODULO DE VENTAS
#           Angel Adolfo Colop Pastor
#                   2026-05-07
from archivos import cargar_datos, guardar_datos

def registrar_cliente():
    
    # Solicita los datos de un nuevo cliente (NIT, Nombre, Teléfono, Correo),
    # valida que el NIT no esté duplicado ni el correo tenga formato inválido,
    # y los guarda en el registro de clientes.
    
    # Recibe:
        # Nada (interactúa directamente con el usuario por consola).
        
    # Devuelve:
        # Nada.
    
    clientes = cargar_datos("datos/clientes.json")

    print("\n--- INGRESE LOS DATOS DEL CLIENTE ---")
    
    nit = input("NIT: ").strip()
    
    for cliente in clientes:
        if cliente["nit"] == nit:
            print("\nError: Este NIT ya ha sido registrado con los siguientes datos:")
            print(f"Nombre: {cliente['nombre']} | Teléfono: {cliente['telefono']}")
            return

    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Correo: ").strip()
    
    if "@" not in email or "." not in email:
        print("Error: El correo debe contener '@' y un punto '.'.")
        return

    nueva_persona = {
        "nit": nit,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    
    clientes.append(nueva_persona)

    guardar_datos("datos/clientes.json", clientes)
        
    print("\nDatos añadidos correctamente.")


def buscar_cliente():
    
    # Busca un cliente en el registro a partir de su Nombre o su NIT y muestra
    # sus datos en pantalla si coincide.
    
    # Recibe:
        # Nada (solicita el término de búsqueda por consola).
        
    # Devuelve:
        # Nada (imprime los resultados directamente en la consola).
    
    clientes = cargar_datos("datos/clientes.json")
    
    if not clientes:
        print("Aún no hay clientes registrados.")
        return

    buscar = input("\nIngrese Nombre o NIT a buscar: ").strip().lower()
    
    encontrado = False
    
    for cliente in clientes:
        if cliente["nombre"].lower() == buscar or cliente["nit"].lower() == buscar:
            print("\n--- CLIENTE ENCONTRADO ---")
            print(f"NIT: {cliente['nit']}")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Correo: {cliente['email']}")
            
            encontrado = True
            
            break

    if not encontrado:
          print("Cliente no existe.")


def editar_cliente():
    
    # Busca un cliente por su NIT y permite actualizar su teléfono y correo electrónico.
    # Si el usuario deja el espacio en blanco, se conserva el dato anterior.
    
    # Recibe:
        # Nada (interactúa con el usuario por consola).
        
    # Devuelve:
        # Nada.
    
    clientes = cargar_datos("datos/clientes.json")
    
    if not clientes:
        print("Aún no hay clientes registrados.")
        return

    nit = input("\nIngrese el NIT del cliente a editar: ").strip()
    encontrado = False
    
    for cliente in clientes:
        if cliente["nit"] == nit:
            encontrado = True
            print("\n--- DATOS ACTUALES ---")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Correo: {cliente['email']}")

            print("\n(Deje el espacio en blanco y presione Enter si no desea cambiar el dato)")
            telefono_nuevo = input("Nuevo teléfono: ").strip()
            correo_nuevo = input("Nuevo correo: ").strip()

            if telefono_nuevo:
                cliente["telefono"] = telefono_nuevo
                
            if correo_nuevo:
                if "@" in correo_nuevo and "." in correo_nuevo:
                    cliente["email"] = correo_nuevo
                else:
                    print("Formato de correo inválido. Se conservará el correo anterior.")

    if not encontrado:
        print("Cliente no encontrado.")
        return
    
    guardar_datos("datos/clientes.json", clientes)

    print("Cliente editado correctamente.")


def eliminar_cliente():
    
    # Elimina a un cliente del registro mediante su NIT, verificando previamente
    # que no posea ningún historial de ventas vinculado en el sistema.
    
    # Recibe:
        # Nada (solicita el NIT por consola al usuario).
        
    # Devuelve:
        # Nada.
    
    clientes = cargar_datos("datos/clientes.json")
    
    if not clientes:
        print("Aún no hay clientes registrados.")
        return

    ventas = cargar_datos("datos/ventas.json")

    nit_eliminar = input("\nIngrese NIT del cliente a eliminar: ").strip()
    
    for venta in ventas:
        if venta.get("nit_cliente") == nit_eliminar:
            print("Error: No se puede eliminar el cliente porque tiene ventas registradas.")
            return

    encontrado = False
    
    clientes_nuevos = []
    
    for cliente in clientes:
        if cliente["nit"] == nit_eliminar:
            encontrado = True
        else:
            clientes_nuevos.append(cliente)

    if not encontrado:
        print("No existe un cliente con ese NIT.")
        return

    guardar_datos("datos/clientes.json", clientes_nuevos)

    print("Cliente eliminado exitosamente.")


def listar_clientes():
    
    # Muestra en pantalla una tabla formateada con la lista de todos los clientes
    # registrados en el sistema.
    
    # Recibe:
       #  Nada.
        
    # Devuelve:
        # Nada (imprime la lista en la consola).
    
    lista = cargar_datos("datos/clientes.json")

    if not lista:
        print("Aún no hay clientes registrados.")
        return

    print("\n--- CLIENTES REGISTRADOS ---")
    print(f"{'NIT':<15} | {'NOMBRE':<20} | {'TELÉFONO':<12} | {'CORREO'}")
    print("-" * 70)
    
    for c in lista:
        print(f"{c['nit']:<15} | {c['nombre']:<20} | {c['telefono']:<12} | {c['email']}")


def modulo_clientes():
    
    # Muestra el menú interactivo para la gestión de clientes y coordina las llamadas
    # a las funciones de registrar, buscar, editar, eliminar y listar.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # Nada (mantiene el ciclo hasta que el usuario decida regresar al menú principal).
    
    while True:
        print("\n=== MÓDULO DE CLIENTES ===")
        print("1. Registrar cliente nuevo")
        print("2. Buscar cliente")
        print("3. Editar datos de un cliente")
        print("4. Eliminar a un cliente")
        print("5. Listar todos los clientes")
        print("0. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_cliente()
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
            print("\nOpción inválida. Intente de nuevo.")