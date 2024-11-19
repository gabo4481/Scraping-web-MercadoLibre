# Scraping-web-MercadoLibre
# Proyecto de Web Scraping y Gestión de Productos

Este proyecto permite realizar web scraping de productos desde un sitio web de comercio electrónico (Mercado Libre), almacenarlos en una base de datos PostgreSQL, y generar un reporte en formato PDF con la información obtenida. Además, ofrece una interfaz gráfica de usuario (GUI) para gestionar los productos, eliminar registros y realizar búsquedas. Se emplea la librería **Dear PyGui** para la interfaz, **Playwright** para el scraping, y **ReportLab** para la generación de PDFs.

## Estructura del Proyecto

El proyecto está dividido en varios módulos y archivos, cada uno con una función específica. A continuación, se describe la estructura y funcionalidad de cada uno.

### Archivos del Proyecto

1. **`main.py`**: Archivo principal donde se ejecuta la interfaz gráfica y se gestionan las interacciones con el controlador de base de datos, scraping y generación de PDFs.
2. **`scraping.py`**: Contiene la clase `Scraping_controller`, encargada de realizar el scraping de productos desde Mercado Libre.
3. **`pdf_controller.py`**: Contiene la clase `PDF_controller`, encargada de generar un reporte PDF con los productos obtenidos.
4. **`DB_controller.py`**: Contiene la clase `DB_controller`, que maneja la conexión a la base de datos PostgreSQL y las operaciones CRUD sobre los productos.

## Funcionalidad

### `main.py`

Este archivo maneja la interfaz gráfica con **Dear PyGui** y las interacciones entre los controladores de scraping, base de datos y PDF.

#### Funciones principales:

- **`eliminar_todo()`**: Elimina todos los registros de la base de datos y restaura las secuencias del ID de los productos.
- **`realizar_scraping()`**: Realiza el scraping de productos desde la página de Mercado Libre, obtiene los datos y los guarda en la base de datos.
- **`actualizar_productos()`**: Actualiza la tabla de productos en la interfaz gráfica con los registros almacenados en la base de datos.
- **`create_eliminar_callback()`**: Crea una función de eliminación de un producto en la base de datos a partir de su ID.

### `scraping.py`

Este archivo contiene la clase `Scraping_controller`, que usa **Playwright** para realizar el scraping de los productos.

#### Función principal:

- **`obtener_valores()`**: Realiza el scraping de la página de productos de Mercado Libre y devuelve una lista de diccionarios con la descripción y precio de los productos.

### `pdf_controller.py`

Este archivo contiene la clase `PDF_controller`, que se encarga de generar un archivo PDF con los productos almacenados en la base de datos.

#### Función principal:

- **`generar_pdf()`**: Genera un archivo PDF con los productos, mostrando su ID, descripción y precio.

### `DB_controller.py`

Este archivo contiene la clase `DB_controller`, que maneja la interacción con la base de datos PostgreSQL.

#### Funciones principales:

- **`conectar()`**: Establece la conexión a la base de datos PostgreSQL.
- **`obtener_registros()`**: Obtiene todos los registros de productos desde la base de datos.
- **`guardar_registros()`**: Guarda los productos obtenidos desde el scraping en la base de datos.
- **`elminar_registro()`**: Elimina un producto de la base de datos por su ID.
- **`eliminar_todos_registros()`**: Elimina todos los registros de productos de la base de datos.
- **`obtener_primeros_10()`**: Obtiene los primeros 10 productos con los precios más bajos.
- **`registros_ordenados_descripcion()`**: Obtiene los productos ordenados alfabéticamente por descripción.
- **`registros_ordenados_precio()`**: Obtiene los productos ordenados por precio.
- **`conteo_registros()`**: Obtiene el número total de productos en la base de datos.
- **`restaurar_secuencias()`**: Restaura la secuencia de ID en la base de datos, comenzando desde 1.

## Requisitos

Para ejecutar este proyecto, es necesario tener los siguientes requisitos instalados:

- **Python 3.7+**
- **Playwright** para realizar el scraping: `pip install playwright`
- **Dear PyGui** para la interfaz gráfica: `pip install dearpygui`
- **ReportLab** para generar PDFs: `pip install reportlab`
- **psycopg2** para interactuar con PostgreSQL: `pip install psycopg`

Además, se necesita tener configurada una base de datos PostgreSQL con una tabla de productos como la siguiente:

```sql
create table productos(
id serial primary key,
descripcion varchar(500) not null,
precio float not null,
fecha_guardado date default current_date
);
