
import os
import json

def cargar_datos(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(ruta_archivo, datos):
    if not os.path.exists("datos"):
        os.makedirs("datos")
        
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error crítico al guardar en {ruta_archivo}: {e}")
        return False