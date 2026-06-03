# Importamos nuestro motor central de base de datos
from archivos import cargar_datos, guardar_datos

# ==============================================================================
# 1. REGISTRAR CLIENTE
# ==============================================================================
def registrar_cliente():
    # Usamos la función cargar_datos que ya maneja si el archivo no existe
    clientes = cargar_datos("datos/clientes.json")

    print("\n--- INGRESE LOS DATOS DEL CLIENTE ---")
    
    # input() captura lo que el usuario escribe. El método .strip() es una medida de seguridad: 
    # elimina cualquier espacio en blanco accidental que el usuario haya dejado al inicio o al final.
    nit = input("NIT: ").strip()
    
    # Recorremos la lista de diccionarios para validar que el NIT no esté duplicado.
    for cliente in clientes:
        if cliente["nit"] == nit:
            print("\nError: Este NIT ya ha sido registrado con los siguientes datos:")
            print(f"Nombre: {cliente['nombre']} | Teléfono: {cliente['telefono']}")
            # El return finaliza la ejecución de la función inmediatamente, 
            # evitando que el código de abajo se ejecute y duplique al cliente.
            return

    # Si el NIT es nuevo, procedemos a solicitar el resto de la información.
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Correo: ").strip()
    
    # Validación básica obligatoria: el operador 'in' verifica si un carácter 
    # específico existe dentro de la cadena de texto del correo.
    if "@" not in email or "." not in email:
        print("Error: El correo debe contener '@' y un punto '.'.")
        return

    # Estructuramos los datos capturados en un nuevo diccionario de Python.
    # Es crucial que las llaves ("nit", "nombre", etc.) estén en minúsculas y coincidan 
    # exactamente con la estructura que usarás en el módulo de ventas.
    nueva_persona = {
        "nit": nit,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    
    # Agregamos este nuevo diccionario al final de nuestra lista en la memoria RAM.
    clientes.append(nueva_persona)

    # Ahora guardamos usando nuestro módulo de archivos
    guardar_datos("datos/clientes.json", clientes)
        
    print("\nDatos añadidos correctamente.")


# ==============================================================================
# 2. BUSCAR CLIENTE
# ==============================================================================
def buscar_cliente():
    clientes = cargar_datos("datos/clientes.json")
    
    if not clientes:
        print("Aún no hay clientes registrados.")
        return

    # Convertimos la entrada del usuario a minúsculas (.lower()) para hacer 
    # una comparación "case-insensitive" (es decir, que "JUAN", "Juan" y "juan" sean iguales).
    buscar = input("\nIngrese Nombre o NIT a buscar: ").strip().lower()
    
    # Creamos una variable de estado (bandera) para saber si la búsqueda tuvo éxito.
    encontrado = False
    
    for cliente in clientes:
        # Evaluamos dos condiciones: que coincida con el nombre (convertido a minúsculas) 
        # o que coincida con el NIT (también convertido a minúsculas por seguridad).
        if cliente["nombre"].lower() == buscar or cliente["nit"].lower() == buscar:
            print("\n--- CLIENTE ENCONTRADO ---")
            print(f"NIT: {cliente['nit']}")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Correo: {cliente['email']}")
            
            # Cambiamos el estado de la bandera porque sí lo encontramos.
            encontrado = True
            
            # Usamos break para detener el ciclo for; no tiene sentido seguir buscando.
            break

    # Si después de revisar toda la lista la bandera sigue siendo False, el cliente no existe.
    if not encontrado:
          print("Cliente no existe.")


# ==============================================================================
# 3. EDITAR CLIENTE
# ==============================================================================
def editar_cliente():
    clientes = cargar_datos("datos/clientes.json")
    
    if not clientes:
        print("Aún no hay clientes registrados.")
        return

    nit = input("\nIngrese el NIT del cliente a editar: ").strip()
    encontrado = False
    
    for cliente in clientes:
        # En este caso, la búsqueda debe ser exacta mediante el NIT único.
        if cliente["nit"] == nit:
            encontrado = True
            print("\n--- DATOS ACTUALES ---")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Correo: {cliente['email']}")

            print("\n(Deje el espacio en blanco y presione Enter si no desea cambiar el dato)")
            telefono_nuevo = input("Nuevo teléfono: ").strip()
            correo_nuevo = input("Nuevo correo: ").strip()

            # En Python, un string vacío ("") se evalúa como False.
            # Esto significa: "Si el usuario escribió algo en teléfono_nuevo..."
            if telefono_nuevo:
                # Modificamos directamente el valor dentro del diccionario actual.
                cliente["telefono"] = telefono_nuevo
                
            if correo_nuevo:
                # Volvemos a validar que el nuevo correo tenga el formato correcto.
                if "@" in correo_nuevo and "." in correo_nuevo:
                    cliente["email"] = correo_nuevo
                else:
                    print("Formato de correo inválido. Se conservará el correo anterior.")

    if not encontrado:
        print("Cliente no encontrado.")
        return
    
    # Guardamos la lista completa de vuelta en el archivo JSON físico.
    guardar_datos("datos/clientes.json", clientes)

    print("Cliente editado correctamente.")


# ==============================================================================
# 4. ELIMINAR CLIENTE
# ==============================================================================
def eliminar_cliente():
    clientes = cargar_datos("datos/clientes.json")
    
    if not clientes:
        print("Aún no hay clientes registrados.")
        return

    # Cargamos las ventas para asegurarnos de no dejar facturas "huérfanas"
    ventas = cargar_datos("datos/ventas.json")

    nit_eliminar = input("\nIngrese NIT del cliente a eliminar: ").strip()
    
    # Iteramos sobre el historial de ventas.
    for venta in ventas:
        if venta.get("nit_cliente") == nit_eliminar:
            print("Error: No se puede eliminar el cliente porque tiene ventas registradas.")
            return

    encontrado = False
    
    # En lugar de usar .pop() o .remove(), creamos una lista paralela nueva.
    clientes_nuevos = []
    
    for cliente in clientes:
        if cliente["nit"] == nit_eliminar:
            encontrado = True
        else:
            # Si no es el cliente que queremos borrar, lo agregamos a la nueva lista.
            clientes_nuevos.append(cliente)

    if not encontrado:
        print("No existe un cliente con ese NIT.")
        return

    # Sobrescribimos el archivo JSON usando la nueva lista filtrada.
    guardar_datos("datos/clientes.json", clientes_nuevos)

    print("Cliente eliminado exitosamente.")


# ==============================================================================
# 5. LISTAR CLIENTES
# ==============================================================================
def listar_clientes():
    lista = cargar_datos("datos/clientes.json")

    # Comprobamos que la lista no esté vacía.
    if not lista:
        print("Aún no hay clientes registrados.")
        return

    print("\n--- CLIENTES REGISTRADOS ---")
    # Utilizamos f-strings con formateo de columnas.
    print(f"{'NIT':<15} | {'NOMBRE':<20} | {'TELÉFONO':<12} | {'CORREO'}")
    print("-" * 70)
    
    for c in lista:
        print(f"{c['nit']:<15} | {c['nombre']:<20} | {c['telefono']:<12} | {c['email']}")


# ==============================================================================
# MENÚ PRINCIPAL DEL MÓDULO
# ==============================================================================
def modulo_clientes():
    # Un ciclo infinito que mantiene al usuario dentro de este submódulo.
    while True:
        print("\n=== MÓDULO DE CLIENTES ===")
        print("1. Registrar cliente nuevo")
        print("2. Buscar cliente")
        print("3. Editar datos de un cliente")
        print("4. Eliminar a un cliente")
        print("5. Listar todos los clientes")
        print("0. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        # Enrutamos el control a la función correspondiente según la entrada del usuario.
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
            # La instrucción break destruye el ciclo while True, finalizando esta función
            # y devolviendo el control al archivo main.py.
            break
        else:
            print("\nOpción inválida. Intente de nuevo.")