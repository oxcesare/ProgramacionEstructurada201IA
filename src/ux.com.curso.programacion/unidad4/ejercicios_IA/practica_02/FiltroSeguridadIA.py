# Estructura y Validacion de datos para IA

LIMITE_SUPERIOR =100.0
LIMITE_INFERIOR = 0.0

def normalizar_dato():
    lectura = float(input("Ingrese un dato: "))
    if lectura >= LIMITE_INFERIOR and lectura <= LIMITE_SUPERIOR:
        dato_normalizdo = lectura / LIMITE_SUPERIOR
        #Ajustar dato_normalizdo a un rango de 0.0 a 1.0    
        print("Señal aceptada. valor normalizado:", dato_normalizdo)
    else:
        print("Error: Dato fuera de rango")

    return "Fin del proceso de filtrado de datos"    

def main():
    normalizar_dato()

if __name__ == "__main__":
    main()