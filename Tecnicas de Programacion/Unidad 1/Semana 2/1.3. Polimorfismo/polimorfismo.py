# Definición de la clase base (superclase)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

# Definición de una subclase que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

# Definición de otra subclase que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Función que utiliza polimorfismo
def hacer_sonido_de_animal(animal):
    return animal.hacer_sonido()

# Crear instancias de las subclases
mi_perro = Perro("Bobby")
mi_gato = Gato("Garfield")

# Usar la función con diferentes tipos de objetos
print(f"El perro dice: {hacer_sonido_de_animal(mi_perro)}")
print(f"El gato dice: {hacer_sonido_de_animal(mi_gato)}")
