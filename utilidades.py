
from datetime import datetime 


def validar_email(email):
    if "@" in email and "." in email:
        return True
    return False


def validar_entero_positivo(texto):
    
    
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
    
    
    while True:
        try:
            valor = float(input(texto))
            
            if valor > 0:
                return valor
            else:
                print("Debe ser un número positivo.")
        except ValueError:
            print("Error: debe ingresar un número válido.")



def obtener_fecha_actual():
    ahora = datetime.now()
    
    return ahora.strftime("%Y-%m-%d %H:%M:%S")


def obtener_fecha_solo_dia():
    ahora = datetime.now()
    return ahora.strftime("%Y-%m-%d")