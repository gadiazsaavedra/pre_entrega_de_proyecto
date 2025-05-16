# pre_entrega_de_proyecto
Pre entrega de Proyecto de la Comision 25006
# Gestor de Productos

Este programa en Python permite gestionar una lista de productos desde la terminal de manera interactiva. Es ideal para practicar estructuras de datos, validaciones y menús en consola.

## Funcionalidades

- **Agregar producto:** Permite ingresar el nombre, la categoría y el precio (sin centavos) de un producto.
- **Visualizar productos:** Muestra todos los productos registrados, numerados y con sus datos.
- **Buscar productos por nombre:** Permite buscar productos ingresando parte o todo el nombre. Muestra coincidencias o informa si no hay resultados.
- **Eliminar producto por posición:** Permite eliminar un producto indicando su número en la lista.
- **Salir:** Finaliza el programa.

## Estructura de los datos

Cada producto se almacena como un diccionario con las siguientes claves:
- `nombre` (str): Nombre del producto.
- `categoria` (str): Categoría del producto.
- `precio` (int): Precio del producto (sin centavos).

Todos los productos se almacenan en una lista llamada `productos`.

## Validaciones

- El nombre y la categoría no pueden estar vacíos.
- El precio debe ser un número entero mayor que cero.
- Todas las entradas del usuario se validan para evitar errores y asegurar la consistencia de los datos.

## Uso

1. Ejecuta el programa en tu terminal con Python 3.
2. Selecciona una opción del menú escribiendo el número correspondiente.
3. Sigue las instrucciones en pantalla para cada operación.
4. El programa continuará ejecutándose hasta que elijas la opción de salir.

## Ejemplo de menú
--- Menú de Opciones ---

1.Agregar producto
2.Visualizar productos
3.Buscar producto por nombre
4.Eliminar producto por posición
5.Salir Seleccione una opción:

## Requisitos

- Python 3.x

## Notas

- El programa es interactivo y utiliza la consola para la entrada y salida de datos.
- No utiliza archivos ni bases de datos; los datos se pierden al cerrar el programa.

---

¡Puedes modificar y mejorar este programa según tus necesidades!
