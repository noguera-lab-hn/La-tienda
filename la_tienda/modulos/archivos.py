# ==============================================================================
#                           MÓDULO DE ARCHIVOS
#                       BRYAN JOSUE NOGUERA MOLINA
#                               2/6/2026
# ==============================================================================

import os
import json

def cargar_datos(ruta_archivo):
    # Intentamos abrir el archivo en modo lectura
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Si el archivo aún no existe (es la primera vez), devolvemos una lista vacía
        return []

def guardar_datos(ruta_archivo, datos):
    # Verificamos si la ruta incluye la carpeta "datos/" y si esta existe
    if not os.path.exists("datos"):
        os.makedirs("datos")
        
    # Intentamos sobrescribir el archivo con los datos nuevos
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            # indent=4 lo formatea bonito y ensure_ascii=False respeta las tildes
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error crítico al guardar en {ruta_archivo}: {e}")
        return False