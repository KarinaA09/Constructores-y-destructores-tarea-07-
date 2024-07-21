import math

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

# Función para calcular el perímetro de un círculo
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Función para calcular el perímetro de un rectángulo
def calcular_perimetro_rectangulo(base, altura):
    perimetro = 2 * (base + altura)
    return perimetro

# Ejemplo de uso de las funciones para calcular área y perímetro

# Calcular el área y el perímetro de un círculo con radio 5
radio = 5
area_circulo = calcular_area_circulo(radio)
perimetro_circulo = calcular_perimetro_circulo(radio)
print(f"Para un círculo con radio {radio}:")
print(f"Área: {area_circulo}")
print(f"Perímetro: {perimetro_circulo}")

print()

# Calcular el área y el perímetro de un rectángulo con base 3 y altura 4
base_rectangulo = 3
altura_rectangulo = 4
area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
perimetro_rectangulo = calcular_perimetro_rectangulo(base_rectangulo, altura_rectangulo)
print(f"Para un rectángulo con base {base_rectangulo} y altura {altura_rectangulo}:")
print(f"Área: {area_rectangulo}")
print(f"Perímetro: {perimetro_rectangulo}")
