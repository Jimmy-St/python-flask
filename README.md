# Proyecto de Programación Web - Flask

Este proycto corresponde a la evaluación de Programación Web. Corresponde a  una aplicación web desarrollada con Python + Flask, estructurada de forma sencilla y modular.
Usamos Tailwind para estilar

---

## Estructura del Proyecto

* `app.py`: Archivo principal con rutas y lógica en Python.
* `templates/`: Plantillas HTML.
  * `index.html`: Menú principal.
  * `ejercicio1.html`: Formulario de cálculo de compras de pintura.
  * `ejercicio2.html`: Formulario de inicio de sesión de usuarios.
* `static/css/estilos.css`: Estilos personalizados.
* `requirements.txt`: Librerías necesarias.

---

## Cómo Ejecutar el Proyecto

1. **Abrir la terminal** en la carpeta del proyecto.
2. **Activar el entorno virtual**:
   * Windows:
     ```bash
     .\venv\Scripts\activate
     ```
3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```
5. Abrir el navegador e ingresar a:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Datos de Prueba

### Ejercicio 1: Cálculo de Compra
* **Precio por tarro:** $9.000
* **Descuentos según edad:**
  * Menor a 18 años: 0% de descuento.
  * Entre 18 y 30 años: 15% de descuento.
  * Mayor a 30 años: 25% de descuento.

### Ejercicio 2: Inicio de Sesión
* **Administrador:**
  * Usuario: `juan`
  * Contraseña: `admin`
* **Usuario estándar:**
  * Usuario: `pepe`
  * Contraseña: `user`
