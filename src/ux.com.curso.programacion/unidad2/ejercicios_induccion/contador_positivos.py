# Contar el numero de enteros positivos introducidos por el teclado

def contar_positivos():
    contador = 0
    while True:
        try:
            numero = int(input("Introduce un número entero (o un número negativo para terminar): "))
            if numero < 0:
                break
            contador += 1
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    print(f"Has introducido {contador} números enteros positivos.")

#Es donde empieza la acción de nuestro programa. Es el punto de partida.
def main():
    print("=== Contador de Números Enteros Positivos ===")
    contar_positivos()    

"""
El bloque 'if __name__ == "__main__":' es una convención en Python que permite
que el código dentro de este bloque se ejecute solo cuando el archivo se ejecuta directamente, 
y no cuando se importa como módulo en otro archivo.
"""
if __name__ == "__main__":  
    main()
