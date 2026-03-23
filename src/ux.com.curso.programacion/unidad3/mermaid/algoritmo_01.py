"""
Suma Condicional de Rango Fijo: 
Diseñar un algoritmo que calcule la suma de todos los números enteros del 1 al 100 que son divisibles por 3 Y, además, impares.
"""
def es_divisible_por_3_y_impar():
    suma =0
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 2 != 0:
            suma += i
        i += 1
    return suma

def main():
    suma = es_divisible_por_3_y_impar()
    print("La suma de los números enteros del 1 al 100 que son divisibles por 3 y, además, impares es:", suma)

if __name__ == "__main__":
    main()        

