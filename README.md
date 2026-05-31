# 🛒 Sistema POS "La Tienda"

## Descripción del Proyecto
Este proyecto es un Sistema de Punto de Venta (POS) diseñado específicamente para "La Tienda", un negocio local administrado por Doña Marta. El sistema está construido en **Python** y opera en la consola, ofreciendo una solución robusta, rápida y sin necesidad de conexión a internet. 

El objetivo principal es digitalizar el control de ventas, inventario y clientes que antes se llevaba en un cuaderno, asegurando que los datos perduren (persistencia) mediante archivos `JSON`, incluso ante cortes de energía eléctrica.

### Módulos Principales:
* **Productos:** Gestión de inventario, alertas de stock mínimo y actualización de precios.
* **Clientes:** Registro y búsqueda de compradores (con soporte para Consumidor Final).
* **Ventas:** Carrito de compras, validación de stock en tiempo real, cálculo de IVA (12%) y generación de facturas en `.txt`.
* **Reportes:** Estadísticas de ventas diarias, productos más vendidos e historial de transacciones.

---

## Cómo correr el proyecto (Ejecución)

### Requisitos previos
* [Python 3.10](https://www.python.org/downloads/) o superior instalado en tu computadora.
* Git instalado.

### Pasos de instalación
1. **Clonar el repositorio:**
   Abre tu terminal y ejecuta el siguiente comando para descargar el código a tu máquina local:
   ```bash
   git clone [Pega_Aqui_El_Enlace_De_Tu_Repositorio_GitHub]

```

2. **Navegar a la carpeta del proyecto:**
```bash
cd [Nombre_De_La_Carpeta_Del_Repositorio]

```


3. **Ejecutar el sistema:**
Para iniciar el programa, corre el archivo principal:
```bash
python main.py

```


*(Nota: Dependiendo de tu sistema operativo, puede que necesites usar `python3 main.py`)*

---

## Capturas de Pantalla del Menú

### Menú Principal

> *Vista del menú principal donde se accede a los distintos módulos.*

### Módulo de Ventas (Carrito)

> *DInterfaz de ventas mostrando el carrito, el cálculo del IVA y los totales.*

### Ejemplo de Factura Generada

> *Archivo .txt generado automáticamente tras confirmar una venta.*

---

## Autores

Este proyecto fue desarrollado como Proyecto Final para el curso de **Programación 1** en la **Universidad Mesoamericana (UMES)**.

* **[Bryan Josue Noguera Molina]** - *Desarrollador (Módulo de Ventas)* - GitHub: [@tu_usuario](https://www.google.com/search?q=https://github.com/tu_usuario)
* **[Compañero 1]** - *Desarrollador (Módulo de Clientes)* - GitHub: [@usuario_compañero1](https://www.google.com/search?q=https://github.com/usuario_companero1)
* **[Compañero 2]** - *Desarrollador (Módulo de Productos)* - GitHub: [@usuario_compañero2](https://www.google.com/search?q=https://github.com/usuario_companero2)

---

*Hecho con mucho ☕ y código.*

```
