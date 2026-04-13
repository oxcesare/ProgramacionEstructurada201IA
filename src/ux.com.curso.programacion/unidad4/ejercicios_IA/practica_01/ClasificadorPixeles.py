# Normalizacion de datos

#Constantes: Define UMBRAL_BAJO = 0.3 y UMBRAL_ALTO = 0.7.
UMBRAL_BAJO = 0.3
UMBRAL_ALTO = 0.7

def clasificar_pixel():
    #Entrada: Solicita al usuario un valor de "Intensidad de Píxel" (rango 0.0 a 1.0).
    intensidad_pixel = float(input("Ingrese la intensidad del píxel (0.0 a 1.0): "))

   # Si la intensidad es menor a 0.0 o mayor a 1.0: Imprime "Error: Valor de píxel inválido".
    if intensidad_pixel < 0.0 or intensidad_pixel > 1.0:
        print("Error: Valor de píxel inválido")
        return

    # Si la intensidad está entre 0.0 y UMBRAL_BAJO (inclusive): Imprime "Clasificación: Fondo (Oscuro)".
    if 0.0 <= intensidad_pixel <= UMBRAL_BAJO:
        print("Clasificación: Fondo (Oscuro)")

    # Si la intensidad es mayor a UMBRAL_BAJO y menor que UMBRAL_ALTO: Imprime "Clasificación: Gris (Ruido)".
    elif UMBRAL_BAJO < intensidad_pixel < UMBRAL_ALTO:
        print("Clasificación: Gris (Ruido)")

    # Si la intensidad es mayor o igual a UMBRAL_ALTO: Imprime "Clasificación: Objeto (Brillante)".
    elif intensidad_pixel >= UMBRAL_ALTO:
        print("Clasificación: Objeto (Brillante)")

    # Cierre: Imprime "Análisis de imagen finalizado".
    print("Análisis de imagen finalizado")

    

# Llamada a la función para ejecutar el programa
def main():
    clasificar_pixel()  # El valor no se utiliza, ya que se solicita al usuario dentro de la función

if __name__ == "__main__":
    main()