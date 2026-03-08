"""
EJEMPLOS DE ESTRUCTURAS DE REPETICIÓN (BUCLES) EN PYTHON
Este archivo muestra el uso de For, While y la simulación de Do-While.
"""

def ejemplo_for():
    print("--- Estructura FOR ---")
    # El bucle 'for' en Python es ideal para iterar sobre secuencias (listas, rangos, etc.)
    frutas = ["manzana", "banana", "cereza"]
    
    print("Iterando una lista:")
    for fruta in frutas:
        print(f"  Hoy comeré: {fruta}")
    
    print("\nUsando range(inicio, fin, paso):")
    for i in range(1, 6, 2):
        print(f"  Número: {i}")
    print("\n")


def ejemplo_while():
    print("--- Estructura WHILE ---")
    # Se ejecuta mientras la condición sea verdadera.
    contador = 5
    while contador > 0:
        print(f"  Cuenta regresiva: {contador}")
        contador -= 1  # Es vital modificar la condición para evitar bucles infinitos
    print("  ¡Despegue!\n")


def ejemplo_do_while():
    print("--- Simulación de DO-WHILE ---")
    # Python no tiene 'do-while'. Se simula con 'while True' y un 'break'.
    # Esto garantiza que el código se ejecute AL MENOS una vez.
    
    secreto = "python123"
    intentos = 0
    
    while True:
        # El código aquí siempre se ejecuta la primera vez
        print("  (Simulación: El código se ejecuta antes de validar)")
        intento_usuario = "python123" # Simulamos entrada del usuario
        intentos += 1
        
        # Condición de salida al final
        if intento_usuario == secreto or intentos >= 1:
            print(f"  Acceso concedido en el intento {intentos}.")
            break
    print("\n")


def main():
    print("=== DEMOSTRACIÓN DE BUCLES EN PYTHON ===\n")
    ejemplo_for()
    ejemplo_while()
    ejemplo_do_while()

if __name__ == "__main__":
    main()