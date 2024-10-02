import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        if not os.path.exists(self.archivo):
            # Crea el archivo si no existe
            with open(self.archivo, 'w') as f:
                pass

        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except ValueError:
            print("Error: Formato de datos incorrecto en el archivo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: Permiso denegado al intentar escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            print("El producto ya existe. Actualizando la cantidad.")
            self.productos[nombre].cantidad += cantidad
        else:
            self.productos[nombre] = Producto(nombre, cantidad, precio)
        self.guardar_inventario()

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto {nombre} eliminado exitosamente.")
        else:
            print("El producto no existe en el inventario.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre].cantidad = cantidad
            if precio is not None:
                self.productos[nombre].precio = precio
            self.guardar_inventario()
            print(f"Producto {nombre} actualizado exitosamente.")
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        print("Inventario actual:")
        for producto in self.productos.values():
            print(producto)

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    inventario.agregar_producto("Manzana", 50, 0.5)
    inventario.agregar_producto("Pera", 30, 0.6)
    inventario.mostrar_inventario()
    inventario.actualizar_producto("Manzana", precio=0.55)
    inventario.eliminar_producto("Pera")
    inventario.mostrar_inventario()
