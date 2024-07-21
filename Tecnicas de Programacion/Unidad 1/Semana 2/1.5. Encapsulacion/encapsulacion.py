# Definición de una clase que utiliza encapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulamiento del atributo nombre
        self.__edad = edad      # Encapsulamiento del atributo edad

    # Método getter para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # Método setter para modificar el nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método getter para obtener la edad
    def get_edad(self):
        return self.__edad

    # Método setter para modificar la edad
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayor que cero.")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Acceder a los atributos utilizando los métodos getter
print(f"Nombre: {persona1.get_nombre()}")  # Salida: Nombre: Juan
print(f"Edad: {persona1.get_edad()}")      # Salida: Edad: 30

# Modificar los atributos utilizando los métodos setter
persona1.set_nombre("Carlos")
persona1.set_edad(35)

# Verificar los cambios
print(f"Nuevo nombre: {persona1.get_nombre()}")  # Salida: Nuevo nombre: Carlos
print(f"Nueva edad: {persona1.get_edad()}")      # Salida: Nueva edad: 35
