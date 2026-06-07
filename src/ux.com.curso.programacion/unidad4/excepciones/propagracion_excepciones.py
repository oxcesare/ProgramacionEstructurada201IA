def calcular_raiz():
    # Esta función provoca una excepción (ValueError) si se le pasa un número negativo
    # pero NO tiene un bloque try-except interno para manejarlo.
    import math
    return math.sqrt(-10) 

def procesar_datos():
    # Esta función llama a calcular_raiz(). 
    # Al no manejar el error aquí tampoco, la excepción se propaga hacia arriba.
    print("Iniciando procesamiento...")
    resultado = calcular_raiz()
    print("Procesamiento terminado.")
    return resultado

if __name__ == "__main__":
    # Nivel Principal (Main)
    # Aquí es donde decidimos poner el "escudo" para detener la propagación
    try:
        procesar_datos()
    except ValueError as e:
        print("\n[MANEJO DE EXCEPCIÓN]: ¡El error fue atrapado en el nivel MAIN!")
        print(f"Detalle del error: No se pueden calcular raíces de números negativos ({e}).")

        