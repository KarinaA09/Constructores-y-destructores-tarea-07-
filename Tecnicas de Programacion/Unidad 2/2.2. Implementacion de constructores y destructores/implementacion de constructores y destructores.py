class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear objetos utilizando el constructor
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Llamar al método saludar de cada objeto
persona1.saludar()
persona2.saludar()


class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.abrir_archivo()

    def abrir_archivo(self):
        print(f"Abriendo el archivo '{self.nombre}'")

    def cerrar_archivo(self):
        print(f"Cerrando el archivo '{self.nombre}'")

    def __del__(self):
        self.cerrar_archivo()
        print(f"Se ha destruido el objeto '{self.nombre}'")

# Crear un objeto de la clase Archivo
archivo = Archivo("documento.txt")

# Simular el uso del archivo (aquí el archivo sigue en uso)
print("Realizando operaciones con el archivo...")

# Al salir de este ámbito, el destructor se llamará automáticamente
