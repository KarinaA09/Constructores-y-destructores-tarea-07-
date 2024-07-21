class MiClase:
    def __init__(self, nombre):
        """
        Constructor de la clase MiClase.

        Args:
        nombre (str): Nombre para inicializar el objeto.
        """
        self.nombre = nombre
        print(f'Se ha creado el objeto {self.nombre}.')

    def __del__(self):
        """
        Destructor de la clase MiClase.

        Se activa cuando el objeto es destruido (cuando ya no hay referencias a él).
        Realiza una limpieza o liberación de recursos asociados al objeto.
        """
        print(f'Se está destruyendo el objeto {self.nombre}.')
        # Aquí podrías añadir código para liberar recursos si es necesario.


# Ejemplo de uso
if __name__ == "__main__":
    # Creamos objetos de la clase MiClase
    objeto1 = MiClase("Objeto1")
    objeto2 = MiClase("Objeto2")

    # Los objetos se destruyen automáticamente cuando ya no son referenciados
    del objeto1
    del objeto2

# Salida esperada:
# Se ha creado el objeto Objeto1.
# Se ha creado el objeto Objeto2.
# Se está destruyendo el objeto Objeto1.
# Se está destruyendo el objeto Objeto2.

