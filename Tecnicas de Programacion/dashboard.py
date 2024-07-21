import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Tecnicas de Programacion/Unidad 1/Semana 2/1.2. Herencia/herencia.py',
        '2': 'Tecnicas de Programacion/Unidad 1/Semana 2/1.3. Polimorfismo/polimorfismo.py',
        '3': 'Tecnicas de Programacion/Unidad 1/Semana 2/1.4. Abstraccion/abstracion.py',
        '4': 'Tecnicas de Programacion/Unidad 1/Semana 2/1.5. Encapsulacion/encapsulacion.py',
        '5': 'Tecnicas de Programacion/Unidad 1/Semana 3/1.6. Programacion orientada a objetos/programacion orientada a objetos.py',
        '6': 'Tecnicas de Programacion/Unidad 1/Semana 3/1.6.2. Programacion tradicional/programacion tradicional.py',
        '7': 'Tecnicas de Programacion/Unidad 1/Semana 4/1.7.1. Ejemplo del mundo real/ejemplo del mundoreal.py',
        '8': 'Tecnicas de Programacion/Unidad 1/Semana 5/1.8.  Calcular el area del perimetro/calcular el area del perimetro.py',
        '9': 'Tecnicas de Programacion/Unidad 2/2.1. Objetos clases herencia polimosfismo/objetos clases herencia polimorfismo.py',
        '10': 'Tecnicas de Programacion/Unidad 2/2.2. Implementacion de constructores y destructores/implementacion de constructores y destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()