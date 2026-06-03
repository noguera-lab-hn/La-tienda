# Sistema POS "La Tienda"

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
   git clone https://github.com/noguera-lab-hn/La-tienda.git
   ```

2. **Navegar a la carpeta del proyecto:**
```bash
cd la-tienda
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

<img width="475" height="224" alt="Captura de pantalla 2026-06-02 235452" src="https://github.com/user-attachments/assets/73a9d01f-9b82-4b05-a628-bfb5f14dd7b5" />


### Módulo de Ventas (Carrito)

<img width="859" height="843" alt="Captura de pantalla 2026-06-02 235643" src="https://github.com/user-attachments/assets/9e8b55d2-45d9-44ad-a5e3-a0a7b3402f77" />


### Ejemplo de Factura Generada

<img width="690" height="481" alt="Captura de pantalla 2026-06-02 235712" src="https://github.com/user-attachments/assets/7d3e873b-99f5-461e-a14b-e2421add8989" />


---

## Autores

Este proyecto fue desarrollado como Proyecto Final para el curso de **Programación 1** en la **Universidad Mesoamericana (UMES)**.

* **[Bryan Josue Noguera Molina]**
* **[Angel Adolfo Colop Pastor]**
* **[Francis Asaf Estrada Francia]**
