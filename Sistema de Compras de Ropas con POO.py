class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_info(self):
        return f"{self.nombre}: Gs.{self.precio:.2f}"


class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def obtener_info(self):
        return f"{self.nombre} (Talla: {self.talla}): Gs.{self.precio:.2f}"


class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def obtener_info(self):
        return f"{self.nombre} (Talla: {self.talla}): Gs.{self.precio:.2f}"


class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def obtener_info(self):
        return f"{self.nombre} (Talla: {self.talla}): Gs.{self.precio:.2f}"


class Accesorio(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)


class RopaInvierno(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def obtener_info(self):
        return f"{self.nombre} (Talla: {self.talla}): Gs.{self.precio:.2f}"


class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"\nCategoría: {self.nombre}")
        for idx, producto in enumerate(self.productos):
            print(f"{idx + 1}. {producto.obtener_info()}")

    def obtener_producto(self, index):
        return self.productos[index]


class Tienda:
    def __init__(self):
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def mostrar_categorias(self):
        print("Categorías disponibles:")
        for idx, categoria in enumerate(self.categorias):
            print(f"{idx + 1}. {categoria.nombre}")

    def seleccionar_categoria(self):
        self.mostrar_categorias()
        while True:
            seleccion = input("Selecciona el número de la categoría (o 'q' para finalizar): ")

            if seleccion.lower() == 'q':
                return None

            try:
                index = int(seleccion) - 1
                if 0 <= index < len(self.categorias):
                    return index
                else:
                    print("Número de categoría no válido. Por favor, intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número o 'q' para finalizar.")

    def mostrar_productos_categoria(self, index_categoria):
        categoria = self.categorias[index_categoria]
        categoria.mostrar_productos()

    def procesar_compra(self, productos_seleccionados):
        if not productos_seleccionados:
            print("\nNo se han seleccionado productos.")
            return
        total = sum(producto.precio for producto in productos_seleccionados)
        print(f"\nTotal de la compra: Gs.{total:.2f}")

    def seleccionar_productos(self):
        productos_seleccionados = []
        while True:
            index_categoria = self.seleccionar_categoria()
            if index_categoria is None:
                break

            while True:
                self.mostrar_productos_categoria(index_categoria)
                seleccion = input("\nSelecciona el número del producto a comprar (o 'q' para volver a categorías): ")

                if seleccion.lower() == 'q':
                    break

                try:
                    index_producto = int(seleccion) - 1
                    if 0 <= index_producto < len(self.categorias[index_categoria].productos):
                        producto_seleccionado = self.categorias[index_categoria].obtener_producto(index_producto)
                        productos_seleccionados.append(producto_seleccionado)
                        print(f"Producto '{producto_seleccionado.nombre}' agregado a la compra.")
                    else:
                        print("Número de producto no válido. Por favor, intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes ingresar un número o 'q' para volver a categorías.")

        if not productos_seleccionados:
            print("\nNo se han seleccionado productos.")
        else:
            self.procesar_compra(productos_seleccionados)


if __name__ == "__main__":
    camisa1 = Camisa("Camisa de Rayas", 150.000, "M")
    pantalon1 = Pantalon("Pantalón Vaquero", 490.000, "32")
    zapato1 = Zapato("Zapato Deportivo", 598.000, "42")
    gorra = Accesorio("Gorra de Marca", 180.000)
    bufanda = RopaInvierno("Bufanda de Lana", 70.000, "Única")
    abrigo = RopaInvierno("Abrigo Térmico", 814.000, "M")

    categoria_ropa = Categoria("Ropa")
    categoria_ropa.agregar_producto(camisa1)
    categoria_ropa.agregar_producto(pantalon1)

    categoria_calzado = Categoria("Calzado")
    categoria_calzado.agregar_producto(zapato1)

    categoria_accesorios = Categoria("Accesorios")
    categoria_accesorios.agregar_producto(gorra)

    categoria_ropa_invierno = Categoria("Ropa de Invierno")
    categoria_ropa_invierno.agregar_producto(bufanda)
    categoria_ropa_invierno.agregar_producto(abrigo)

    tienda = Tienda()
    tienda.agregar_categoria(categoria_ropa)
    tienda.agregar_categoria(categoria_calzado)
    tienda.agregar_categoria(categoria_accesorios)
    tienda.agregar_categoria(categoria_ropa_invierno)

    tienda.seleccionar_productos()
