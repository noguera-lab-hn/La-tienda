from datetime import datetime 

# VALIDACIONES
def validar_email(email):
    # Verifica que un correo electrónico tenga un formato básico válido.
    
    # Recibe:
        # email (str): El texto del correo electrónico a evaluar.
        
    #Devuelve:
        # bool: True si el correo contiene al menos un "@" y un ".", False en caso contrario.
    if "@" in email and "." in email:
        return True
    return False


def validar_entero_positivo(texto):
    
    # Solicita un número al usuario y asegura que sea un entero mayor a cero. 
    # Mantiene al usuario en un bucle hasta que ingrese un dato válido.
    
    # Recibe:
        # texto (str): El mensaje o instrucción que se mostrará en pantalla al usuario (ej. "Ingrese cantidad: ").
        
    # Devuelve:
        # int: El número entero positivo ingresado.
    
    while True:
        try:
            valor = int(input(texto))
            if valor > 0:
                return valor
            else:
                print("Debe ser un número positivo.")
        except ValueError:
            print("Error: debe ingresar un número entero.")


def validar_float_positivo(texto):
    
    # Solicita un número decimal al usuario y asegura que sea mayor a cero (ideal para precios).
    # Mantiene al usuario en un bucle hasta que ingrese un dato válido.
    
    # Recibe:
        # texto (str): El mensaje o instrucción que se mostrará en pantalla al usuario.
        
    # Devuelve:
        # float: El número decimal positivo ingresado.
    
    while True:
        try:
            valor = float(input(texto))
            if valor > 0:
                return valor
            else:
                print("Debe ser un número positivo.")
        except ValueError:
            print("Error: debe ingresar un número válido.")



# FUNCIONES DE FECHA Y HORA
def obtener_fecha_actual():
    
    # Captura el instante exacto actual del sistema y lo formatea para facturación.
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # str: La fecha y hora actual en formato "Año-Mes-Día Hora:Minuto:Segundo" (ej. "2026-05-27 14:32:10").
    
    ahora = datetime.now()
    return ahora.strftime("%Y-%m-%d %H:%M:%S")


def obtener_fecha_solo_dia():
    # Captura el día actual del sistema, omitiendo la hora (ideal para reportes de cierre diario).
    
    # Recibe:
        # Nada.
        
    # Devuelve:
        # str: La fecha actual en formato "Año-Mes-Día" (ej. "2026-05-27").

    ahora = datetime.now()
    return ahora.strftime("%Y-%m-%d")