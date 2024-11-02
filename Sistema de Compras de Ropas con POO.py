class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def obtener_info(self):
        return f"{self._nombre}: Gs.{self._precio:.2f}"

    def obtener_precio(self):
        return self._precio


class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def obtener_info(self):
        return f"{self._nombre} (Talla: {self._talla}): Gs.{self._precio:.2f}"


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla)
        self._tipo_tela = tipo_tela

    def obtener_info(self):
        return f"{self._nombre} (Talla: {self._talla}, Tela: {self._tipo_tela}): Gs.{self._precio:.2f}"


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla)
        self._tipo_tela = tipo_tela

    def obtener_info(self):
        return f"{self._nombre} (Talla: {self._talla}, Tela: {self._tipo_tela}): Gs.{self._precio:.2f}"


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio, talla)

    def obtener_info(self):
        return f"{self._nombre} (Talla: {self._talla}): Gs.{self._precio:.2f}"


class Accesorio(Producto):
    pass


class RopaInvierno(Ropa):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio, talla)

    def obtener_info(self):
        return f"{self._nombre} (Talla: {self._talla}): Gs.{self._precio:.2f}"


class Categoria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        print(f"\nCategoría: {self._nombre}")
        for idx, producto in enumerate(self._productos):
            print(f"{idx + 1}. {producto.obtener_info()}")

    def obtener_producto(self, index):
        return self._productos[index]


class Carrito:
    def __init__(self):
        self._productos_seleccionados = []

    def agregar_producto(self, producto):
        self._productos_seleccionados.append(producto)

    def calcular_total(self):
        return sum(producto.obtener_precio() for producto in self._productos_seleccionados)

    def mostrar_resumen(self):
        if not self._productos_seleccionados:
            print("\nNo se han seleccionado productos.")
            return

        print("\nResumen de la compra:")
        for producto in self._productos_seleccionados:
            print(f"- {producto.obtener_info()}")
        print(f"Total de la compra: Gs.{self.calcular_total():.2f}")


class Tienda:
    def __init__(self):
        self._categorias = []

    def agregar_categoria(self, categoria):
        self._categorias.append(categoria)

    def mostrar_categorias(self):
        print("Categorías disponibles:")
        for idx, categoria in enumerate(self._categorias):
            print(f"{idx + 1}. {categoria._nombre}")

    def seleccionar_categoria(self):
        self.mostrar_categorias()
        while True:
            seleccion = input("Selecciona el número de la categoría (o 'q' para finalizar): ")

            if seleccion.lower() == 'q':
                return None

            try:
                index = int(seleccion) - 1
                if 0 <= index < len(self._categorias):
                    return index
                else:
                    print("Número de categoría no válido. Por favor, intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número o 'q' para finalizar.")

    def mostrar_productos_categoria(self, index_categoria):
        categoria = self._categorias[index_categoria]
        categoria.mostrar_productos()

    def seleccionar_productos(self):
        carrito = Carrito()
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
                    if 0 <= index_producto < len(self._categorias[index_categoria]._productos):
                        producto_seleccionado = self._categorias[index_categoria].obtener_producto(index_producto)
                        carrito.agregar_producto(producto_seleccionado)
                        print(f"Producto '{producto_seleccionado._nombre}' agregado a la compra.")
                    else:
                        print("Número de producto no válido. Por favor, intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Debes ingresar un número o 'q' para volver a categorías.")

        carrito.mostrar_resumen()


if __name__ == "__main__":
    camisa1 = Camisa("Camisa de Rayas", 150000, "M", "Algodón")
    pantalon1 = Pantalon("Pantalón Vaquero", 490000, "32", "Denim")
    zapato1 = Zapato("Zapato Deportivo", 598000, "42")
    gorra = Accesorio("Gorra de Marca", 180000)
    bufanda = RopaInvierno("Bufanda de Lana", 70000, "Única")
    abrigo = RopaInvierno("Abrigo Térmico", 814000, "M")

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
