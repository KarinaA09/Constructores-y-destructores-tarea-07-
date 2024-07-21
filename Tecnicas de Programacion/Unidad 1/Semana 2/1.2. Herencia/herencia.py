# Definición de la clase base (superclase)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Definición de una subclase que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamada al constructor de la clase base
        super().__init__(nombre)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau!"

# Definición de otra subclase que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacer_sonido(self):
        return "¡Miau!"

# Crear instancias de las subclases
mi_perro = Perro("Bobby", "Labrador")
mi_gato = Gato("Garfield", "Naranja")

# Acceder a atributos y métodos de las instancias
print(f"{mi_perro.nombre} es un {mi_perro.raza} y dice {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} es de color {mi_gato.color} y dice {mi_gato.hacer_sonido()}")
