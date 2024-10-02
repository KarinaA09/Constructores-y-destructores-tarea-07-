class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Almacena como tupla (nombre, apellido)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} - ISBN: {self.isbn} (Categoría: {self.categoria})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.user_id})"

    def __hash__(self):
        return hash(self.user_id)

    def __eq__(self, other):
        return isinstance(other, Usuario) and self.user_id == other.user_id


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros: ISBN -> Libro
        self.usuarios = set()  # Conjunto de usuarios

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, nombre, user_id):
        if user_id in [usuario.user_id for usuario in self.usuarios]:
            print(f"El ID de usuario {user_id} ya está en uso.")
        else:
            usuario = Usuario(nombre, user_id)
            self.usuarios.add(usuario)
            print(f"Usuario '{nombre}' registrado exitosamente.")

    def dar_baja_usuario(self, user_id):
        self.usuarios = {usuario for usuario in self.usuarios if usuario.user_id != user_id}
        print(f"Usuario con ID {user_id} ha sido dado de baja.")

    def prestar_libro(self, isbn, user_id):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)

        if libro is None:
            print("El libro no está disponible.")
        elif usuario is None:
            print("El usuario no está registrado.")
        elif libro in usuario.libros_prestados:
            print("El usuario ya tiene este libro prestado.")
        else:
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")

    def devolver_libro(self, isbn, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)

        if usuario is None:
            print("El usuario no está registrado.")
            return

        libro = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)

        if libro:
            usuario.libros_prestados.remove(libro)
            print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
        else:
            print("El usuario no tiene este libro prestado.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and valor.lower() in libro.titulo.lower()) or \
                    (criterio == "autor" and valor.lower() in f"{libro.autor[0]} {libro.autor[1]}".lower()) or \
                    (criterio == "categoria" and valor.lower() == libro.categoria.lower()):
                resultados.append(libro)

        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)

        if usuario is None:
            print("El usuario no está registrado.")
            return

        if usuario.libros_prestados:
            print(f"Libros prestados a '{usuario.nombre}':")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print("El usuario no tiene libros prestados.")


# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Añadir libros
    libro1 = Libro("1984", ("George", "Orwell"), "Ficción", "1234567890")
    libro2 = Libro("El Principito", ("Antoine", "de Saint-Exupéry"), "Fantasía", "0987654321")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar usuarios
    biblioteca.registrar_usuario("Alice", "001")
    biblioteca.registrar_usuario("Bob", "002")

    # Prestar libros
    biblioteca.prestar_libro("1234567890", "001")
    biblioteca.prestar_libro("0987654321", "002")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("001")
    biblioteca.listar_libros_prestados("002")

    # Devolver libros
    biblioteca.devolver_libro("1234567890", "001")

    # Buscar libros
    biblioteca.buscar_libros("autor", "Orwell")

    # Dar de baja a un usuario
    biblioteca.dar_baja_usuario("002")
