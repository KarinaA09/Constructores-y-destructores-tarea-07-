# Definición de la clase base (superclase) Libro
class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def __str__(self):
        return f"Libro: {self.__titulo} - Autor: {self.__autor}"


# Definición de la subclase LibroFisico que hereda de Libro
class LibroFisico(Libro):
    def __init__(self, titulo, autor, ubicacion):
        super().__init__(titulo, autor)
        self.__ubicacion = ubicacion

    def get_ubicacion(self):
        return self.__ubicacion

    def __str__(self):
        return f"Libro físico: {self.get_titulo()} - Autor: {self.get_autor()} - Ubicación: {self.__ubicacion}"


# Definición de la subclase LibroDigital que hereda de Libro
class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.__formato = formato

    def get_formato(self):
        return self.__formato

    def __str__(self):
        return f"Libro digital: {self.get_titulo()} - Autor: {self.get_autor()} - Formato: {self.__formato}"


# Función principal para simular el sistema de gestión de biblioteca
def gestion_biblioteca():
    # Crear instancias de libros físicos y digitales
    libro1 = LibroFisico("Python Programming", "John Smith", "Estantería A1")
    libro2 = LibroDigital("Data Science Handbook", "Emily Brown", "PDF")

    # Mostrar información de los libros
    print(libro1)
    print(libro2)


# Ejecutar la función principal
gestion_biblioteca()
