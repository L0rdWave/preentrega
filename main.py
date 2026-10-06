# Sistema de gestión básica de productos

productos = []


def validar_texto(mensaje, nombre_campo):
    valor = input(mensaje).strip()
    while valor == "":
        print(f"El {nombre_campo} no puede estar vacío.")
        valor = input(mensaje).strip()
    return valor


def validar_precio():
    precio_txt = input("Precio (sin centavos): ").strip()
    while not precio_txt.isdigit() or int(precio_txt) <= 0:
        print("Precio inválido. Ingresá un número mayor a 0.")
        precio_txt = input("Precio (sin centavos): ").strip()
    return int(precio_txt)


def agregar_producto():
    print("\n[Agregar producto]")
    nombre = validar_texto("Nombre: ", "nombre")
    categoria = validar_texto("Categoría: ", "categoría")
    precio = validar_precio()
    productos.append([nombre, categoria, precio])
    print(f"\n¡Producto '{nombre}' agregado correctamente!")


def mostrar_productos():
    print("\n[Lista de productos]")
    if not productos:
        print("Todavía no hay productos cargados.")
        return

    print("Productos registrados:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto[0]} | {producto[1]} | ${producto[2]}")


def buscar_producto():
    print("\n[Buscar producto]")
    if not productos:
        print("No hay productos para buscar.")
        return

    busqueda = input("¿Qué querés buscar?: ").strip().lower()
    coincidencias = []

    for producto in productos:
        if busqueda in producto[0].lower():
            coincidencias.append(producto)

    if not coincidencias:
        print("No se encontró ningún producto con ese nombre.")
        return

    print("\nCoincidencias:")
    for i, producto in enumerate(coincidencias, 1):
        print(f"{i}. {producto[0]} | {producto[1]} | ${producto[2]}")


def eliminar_producto():
    print("\n[Eliminar producto]")
    if not productos:
        print("No hay nada para eliminar.")
        return

    mostrar_productos()
    posicion = input("Número del producto a borrar: ").strip()
    while not posicion.isdigit() or not (1 <= int(posicion) <= len(productos)):
        print(f"Número inválido. Elegí un número entre 1 y {len(productos)}.")
        posicion = input("Número del producto a borrar: ").strip()

    producto_eliminado = productos.pop(int(posicion) - 1)
    print(f"Se borró '{producto_eliminado[0]}'.")


def mostrar_menu():
    print("\n--- Gestión de Productos ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")


while True:
    mostrar_menu()
    opcion = input("\nElegí una opción: ").strip()

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("\n¡Hasta luego!")
        break
    else:
        print("Opción incorrecta. Elegí un número del 1 al 5.")