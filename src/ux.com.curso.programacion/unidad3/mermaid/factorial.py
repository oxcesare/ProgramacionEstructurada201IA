"""
Diseñar un algoritmo que calcule el factorial de un número entero positivo ingresado por el usuario (N).
"""

def factorial():
    numero_ingresado = int(input("Ingrese un número entero positivo: "))
    factorial = 1
    i =1
    while i <= numero_ingresado:
        factorial *= i
        i += 1
    return factorial

def main():
    resultado = factorial()
    print("El factorial del número ingresado es:", resultado)

if __name__ == "__main__":
    main()