"""
Módulo: utilidades.py
Autores: [Francis Asaf Estrada Francia]
Fecha: 2026-05-06
Descripción: Funciones de utilidad para validaciones matemáticas, de correo y formato de fechas.
"""

from datetime import datetime 

# ============================================
# VALIDACIONES
# ============================================

def validar_email(email):
    """Validación básica de email: debe tener @ y un punto después."""
    # "in" verifica si un texto contiene otro texto
    # Ejemplo: "@" in "maria@gmail.com" es True porque el @ está dentro
    # and significa que las DOS condiciones deben cumplirse
    if "@" in email and "." in email:
        # Si tiene @ Y tiene ., es válido
        return True
    # Si no cumple la condición, es inválido
    return False


def validar_entero_positivo(texto):
    """
    Pide un número entero positivo al usuario.
    Sigue preguntando hasta que ingrese un número válido.
    """
    # while True = bucle infinito. Solo sale con return
    while True:
        # TRY: Intentamos convertir a número
        try:
            # input(texto) muestra el mensaje y espera que el usuario escriba
            # int() convierte lo escrito a número entero
            # Ejemplo: "5" → 5, "hola" → error
            valor = int(input(texto))
            
            # Si el número es mayor que 0
            if valor > 0:
                # return devuelve el valor Y sale de la función (termina el bucle)
                return valor
            else:
                # Si es 0 o negativo, mostramos error y el bucle sigue
                print("Debe ser un número positivo.")
        
        # EXCEPT: Si int() no pudo convertir (ej: el usuario escribió "abc")
        except ValueError:
            print("Error: debe ingresar un número entero.")


def validar_float_positivo(texto):
    """
    Pide un número decimal positivo al usuario (ej: 6.50, 12.99).
    Sigue preguntando hasta que ingrese un número válido.
    """
    while True:
        try:
            # float() convierte a número decimal (permite punto decimal)
            # Ejemplo: "6.50" → 6.5, "hola" → error
            valor = float(input(texto))
            
            if valor > 0:
                return valor
            else:
                print("Debe ser un número positivo.")
        except ValueError:
            print("Error: debe ingresar un número válido.")


# ============================================
# FUNCIONES DE FECHA Y HORA
# ============================================

def obtener_fecha_actual():
    """Devuelve la fecha y hora actual como string."""
    # datetime.now() obtiene la fecha y hora exacta del computador en este momento
    ahora = datetime.now()
    
    # strftime() formatea la fecha como texto
    # %Y = año con 4 dígitos (2026)
    # %m = mes con 2 dígitos (05)
    # %d = día con 2 dígitos (27)
    # %H = hora en formato 24 horas (14)
    # %M = minutos (32)
    # %S = segundos (10)
    # Resultado: "2026-05-27 14:32:10"
    return ahora.strftime("%Y-%m-%d %H:%M:%S")


def obtener_fecha_solo_dia():
    """Devuelve solo la fecha actual (año-mes-día) para comparar ventas del día."""
    ahora = datetime.now()
    # Solo devuelve la fecha sin la hora
    # Resultado: "2026-05-27"
    return ahora.strftime("%Y-%m-%d")