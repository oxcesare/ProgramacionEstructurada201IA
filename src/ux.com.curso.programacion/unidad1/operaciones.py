#Ejemplo de Math 
import math
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Formula: A = π * r^2
    """
    area = math.pi * (radio ** 2)
    return area


print("Área del círculo con radio 5:", calcular_area_circulo(5))

