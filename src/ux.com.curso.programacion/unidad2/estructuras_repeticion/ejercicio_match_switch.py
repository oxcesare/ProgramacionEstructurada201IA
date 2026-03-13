#Ejemplo de match-case en Python 3.10+
def demostracion():
    print("--- Ejemplo de match-case ---")
    opcion = input("Selecciona una opción (1-3): ")
    
    match opcion:
        case "1":
            print("Has seleccionado la opción 1: Saludar")
            nombre = input("¿Cómo te llamas? ")
            print(f"¡Hola, {nombre}!")
        case "2":
            print("Has seleccionado la opción 2: Calcular suma")
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"La suma es: {num1 + num2}")
        case "3":
            print("Has seleccionado la opción 3: Salir")
            print("¡Adiós!")
        case _:
            print("Opción no válida. Por favor, selecciona entre 1 y 3.")


def main():
    demostracion()

if __name__ == "__main__":
    main()