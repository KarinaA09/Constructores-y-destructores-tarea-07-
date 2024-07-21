# Ejemplo de programación tradicional en Python

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = 3.14159 * radio ** 2
    return area

# Función para calcular el volumen de un cilindro
def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen

# Función principal para utilizar las funciones anteriores
def main():
    # Calcular el área de un círculo con radio 5
    radio = 5
    area_circulo = calcular_area_circulo(radio)
    print(f"El área de un círculo con radio {radio} es: {area_circulo}")

    # Calcular el volumen de un cilindro con radio 3 y altura 10
    radio_cilindro = 3
    altura_cilindro = 10
    volumen_cilindro = calcular_volumen_cilindro(radio_cilindro, altura_cilindro)
    print(f"El volumen de un cilindro con radio {radio_cilindro} y altura {altura_cilindro} es: {volumen_cilindro}")

# Llamar a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
