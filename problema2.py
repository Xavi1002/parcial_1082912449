def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre in inventario:
        print("El producto ya existe.")
        return
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        if cantidad <= 0 or precio <= 0:
            print("Cantidad y precio deben ser positivos.")
            return
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        print("Producto agregado.")
    except ValueError:
        print("Cantidad y precio deben ser números válidos.")

def ver_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("Inventario:")
    total_general = 0
    for nombre, datos in inventario.items():
        cantidad = datos['cantidad']
        precio = datos['precio']
        total = cantidad * precio
        total_general += total
        print(f"- {nombre}: Cantidad: {cantidad}, Precio: ${precio:.2f}, Total: ${total:.2f}")
    print(f"Total general: ${total_general:.2f}")

def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"Producto encontrado: {nombre}, Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}")
    else:
        print("Producto no encontrado.")

def actualizar_cantidad(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    if nombre not in inventario:
        print("Producto no encontrado.")
        return
    try:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        if nueva_cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        inventario[nombre]['cantidad'] = nueva_cantidad
        print("Cantidad actualizada.")
    except ValueError:
        print("La cantidad debe ser un número válido.")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def menu():
    inventario = {}
    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            ver_inventario(inventario)
        elif opcion == '3':
            buscar_producto(inventario)
        elif opcion == '4':
            actualizar_cantidad(inventario)
        elif opcion == '5':
            eliminar_producto(inventario)
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
