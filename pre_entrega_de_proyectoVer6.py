# Programa para gestionar productos
"""
Este programa permite realizar las siguientes operaciones sobre una lista de productos:
1. Agregar un producto con nombre, categoría y precio.
2. Visualizar todos los productos registrados.
3. Buscar productos por nombre.
4. Eliminar un producto especificando su posición en la lista.
5. Salir del programa.

Variables:
    productos (list): Lista que almacena los productos. Cada producto es un diccionario con las claves:
        - 'nombre' (str): Nombre del producto.
        - 'categoria' (str): Categoría del producto.
        - 'precio' (int): Precio del producto (sin centavos).

Flujo del programa:
    - El programa muestra un menú de opciones al usuario en la consola.
    - Según la opción seleccionada, ejecuta la operación correspondiente (agregar, visualizar, buscar o eliminar productos).
    - El programa continúa ejecutándose hasta que el usuario elige la opción de salir.

Notas:
    - El precio del producto debe ser un número entero mayor que cero.
    - Todas las entradas del usuario se validan para evitar errores y asegurar la consistencia de los datos.
    - El programa es interactivo y utiliza la consola para la entrada y salida de datos.
"""


productos = []

while True:
    print("\n--- Menú de Opciones ---")
    print("1. Agregar producto\n2. Visualizar productos\n3. Buscar producto por nombre")
    print("4. Eliminar producto por posición\n5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    # Bloque: Agregar un producto
    if opcion == "1":
        print("\n--- Agregar Producto ---")
        nombre = input("Ingrese el nombre del producto: ").strip()
        while not nombre:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        categoria = input("Ingrese la categoría del producto: ").strip()
        while not categoria:
            print("La categoría no puede estar vacía. Intente nuevamente.")
            categoria = input("Ingrese la categoría del producto: ").strip()

        precio_valido = False
        while not precio_valido:
            precio_str = input(
                "Ingrese el precio del producto (sin centavos): "
            ).strip()
            try:
                precio = int(precio_str)
                if 0 < precio <= 1_000_000:
                    precio_valido = True
                else:
                    print(
                        "El precio debe ser mayor que cero y menor o igual a 1,000,000. Intente nuevamente."
                    )
            except ValueError:
                print("El precio debe ser un número entero. Intente nuevamente.")

        productos.append({"nombre": nombre, "categoria": categoria, "precio": precio})
        print(f"Producto '{nombre}' agregado exitosamente.")

    # Bloque: Visualizar productos o preparar para eliminar
    elif opcion in ["2", "4"]:
        if not productos:
            print(
                "No hay productos registrados."
                if opcion == "2"
                else "No hay productos registrados para eliminar."
            )
        else:
            # Mostrar la lista de productos
            print(
                "\n--- Lista de Productos ---"
                if opcion == "2"
                else "\n--- Eliminar Producto ---"
            )
            for i, p in enumerate(productos, start=1):
                print(
                    f"{i}. Nombre: {p['nombre']}, Categoría: {p['categoria']}, Precio: ${p['precio']}"
                )

            # Bloque: Eliminar producto por posición
            if opcion == "4":
                pos = input(
                    f"Ingrese el número del producto a eliminar (1-{len(productos)}): "
                ).strip()

                # Validar entrada
                while not (pos.isdigit() and 1 <= int(pos) <= len(productos)):
                    print(
                        f"Número inválido. Debe estar entre 1 y {len(productos)}. Intente nuevamente."
                    )
                    pos = input(
                        f"Ingrese el número del producto a eliminar (1-{len(productos)}): "
                    ).strip()

                # Confirmar eliminación
                pos_int = int(pos)
                producto_a_eliminar = productos[pos_int - 1]
                confirmacion = (
                    input(
                        f"¿Está seguro que desea eliminar '{producto_a_eliminar['nombre']}'? (s/n): "
                    )
                    .strip()
                    .lower()
                )

                if confirmacion == "s":
                    eliminado = productos.pop(pos_int - 1)
                    print(f"Producto '{eliminado['nombre']}' eliminado exitosamente.")

                    # Mostrar la lista actualizada
                    if productos:
                        print("\n--- Lista actualizada de Productos ---")
                        for i, p in enumerate(productos, start=1):
                            print(
                                f"{i}. Nombre: {p['nombre']}, Categoría: {p['categoria']}, Precio: ${p['precio']}"
                            )
                    else:
                        print("No quedan productos en la lista.")
                else:
                    print("Operación de eliminación cancelada.")

    # Bloque: Buscar producto por nombre
    elif opcion == "3":
        if not productos:
            print("No hay productos registrados para buscar.")
        else:
            termino_busqueda = input(
                "Ingrese el nombre del producto a buscar: "
            ).strip()

            # Validar que no esté vacío y solicitar nuevamente si es necesario
            while not termino_busqueda:
                print("El término de búsqueda no puede estar vacío.")
                termino_busqueda = input(
                    "Ingrese el nombre del producto a buscar: "
                ).strip()

            # Buscar productos que coincidan
            encontrados = [
                p for p in productos if termino_busqueda.lower() in p["nombre"].lower()
            ]

            if encontrados:
                print("\n--- Productos Encontrados ---")
                for p in encontrados:
                    print(
                        f"Nombre: {p['nombre']}, Categoría: {p['categoria']}, Precio: ${p['precio']}"
                    )
            else:
                print(
                    f"No se encontraron productos que contengan '{termino_busqueda}'."
                )

    # Bloque: Salir del programa
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    # Opción inválida
    else:
        print("Opción inválida. Intente nuevamente.")
