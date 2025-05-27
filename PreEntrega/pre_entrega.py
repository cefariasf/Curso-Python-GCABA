productos = []

def agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            break
        print("Error: el nombre no puede estar vacío.")

    while True:
        categoria = input("Ingrese la categoría del producto: ").strip()
        if categoria:
            break
        print("Error: la categoría no puede estar vacía.")

    while True:
        precio_input = input("Ingrese el precio del producto (sin centavos, solo números enteros): ").strip()
        if precio_input.isdigit() and int(precio_input) > 0:
            precio = int(precio_input)
            break
        print("Error: el precio debe ser un número entero positivo.")

    productos.append([nombre, categoria, precio])
    print(f"Producto '{nombre}' agregado correctamente.\n")

def mostrar_productos():
    if not productos:
        print("No hay productos registrados.\n")
        return
    print("\nProductos registrados:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. Nombre: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]}")
    print()

def buscar_producto():
    if not productos:
        print("No hay productos para buscar.\n")
        return

    busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    resultados = []
    for producto in productos:
        if busqueda in producto[0].lower():
            resultados.append(producto)

    if resultados:
        print(f"\nResultados encontrados ({len(resultados)}):")
        for p in resultados:
            print(f"- Nombre: {p[0]}, Categoría: {p[1]}, Precio: ${p[2]}")
        print()
    else:
        print("No se encontraron productos con ese nombre.\n")

def eliminar_producto():
    if not productos:
        print("No hay productos para eliminar.\n")
        return

    mostrar_productos()
    while True:
        opcion = input("Ingrese el número del producto a eliminar (o '0' para cancelar): ").strip()
        if opcion == '0':
            print("Eliminación cancelada.\n")
            break
        if opcion.isdigit():
            indice = int(opcion) - 1
            if 0 <= indice < len(productos):
                eliminado = productos.pop(indice)
                print(f"Producto '{eliminado[0]}' eliminado correctamente.\n")
                break
        print("Número inválido. Intente de nuevo.")

def menu():
    while True:
        print("----- Menú de gestión de productos -----")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto por nombre")
        print("4. Eliminar producto por número")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor ingrese un número del 1 al 5.\n")

if __name__ == "__main__":
    menu()