import os
import json


def cargar_datos(ruta_archivo):
    
    # Abre y lee el contenido de un archivo JSON, convirtiéndolo a una estructura manejable en Python.
    
    # Recibe:
        # ruta_archivo (str): La ruta exacta donde se encuentra el archivo (ej. "datos/clientes.json").
        
    # Devuelve:
        # list/dict: Los datos leídos del archivo. Si el archivo no existe, devuelve una lista vacía [].
    
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_datos(ruta_archivo, datos):
    
    # Sobrescribe un archivo JSON con nueva información, creando la carpeta 'datos' si esta no existe.
    
    # Recibe:
        # ruta_archivo (str): La ruta exacta donde se guardará el archivo.
        # datos (list/dict): La estructura de datos de Python que se desea guardar.
        
    # Devuelve:
        # bool: True si los datos se guardaron correctamente, False si ocurrió un error crítico.
    
    if not os.path.exists("datos"):
        os.makedirs("datos")
        
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error crítico al guardar en {ruta_archivo}: {e}")
        return False