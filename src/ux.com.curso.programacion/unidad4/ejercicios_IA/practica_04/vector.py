def definir_vector():
    
    #Declara un vector llamado sensores_distancia de tamaño 5.
    sensores_distancia = [0] * 5
    
    #Usa un ciclo for para solicitar al usuario que ingrese la distancia detectada por cada uno de los 5 sensores frontales del robot.
    for i in range(5):
        sensores_distancia[i] = float(input(f"Ingrese la distancia detectada por el sensor {i+1}: "))
    
    #Operación: Calcula el promedio de distancia de todo el vector.
    promedio_distancia = sum(sensores_distancia) / len(sensores_distancia)  
    print("Distancias detectadas por los sensores:", sensores_distancia)
    print("Promedio de distancia:", promedio_distancia)

    #Si el promedio es menor a 2.0 metros, imprime un aviso de: "Aviso: Reduciendo velocidad global".
    if promedio_distancia < 2.0:
        print("Aviso: Reduciendo velocidad global")


def main():
    definir_vector()

if __name__ == "__main__":
    main()    

