# Definición de la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad disponible: {self.cantidad}")

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f"Venta realizada: {cantidad_vendida} unidades de {self.nombre}")
        else:
            print(f"No hay suficiente stock de {self.nombre} para vender {cantidad_vendida} unidades.")

# Definición de la clase Tienda que gestiona productos
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la tienda.")

    def listar_productos(self):
        print(f"Productos en la tienda '{self.nombre}':")
        for producto in self.productos:
            producto.mostrar_producto()

    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.vender(cantidad)
                break
        else:
            print(f"No se encontró el producto '{nombre_producto}' en la tienda.")

# Crear una instancia de Tienda
mi_tienda = Tienda("Tienda de Tecnología")

# Crear instancias de Producto y agregarlos a la tienda
producto1 = Producto("Laptop", 1500, 10)
producto2 = Producto("Mouse", 30, 50)
producto3 = Producto("Teclado", 50, 30)

mi_tienda.agregar_producto(producto1)
mi_tienda.agregar_producto(producto2)
mi_tienda.agregar_producto(producto3)

# Listar los productos de la tienda
mi_tienda.listar_productos()

# Simular una venta de productos
mi_tienda.vender_producto("Mouse", 20)
mi_tienda.vender_producto("Laptop", 3)
mi_tienda.vender_producto("Monitor", 2)

# Listar los productos actualizados después de la venta
mi_tienda.listar_productos()
