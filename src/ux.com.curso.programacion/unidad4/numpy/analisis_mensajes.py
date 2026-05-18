# 1. IMPORTACIÓN 
# Importamos la biblioteca externa y le asignamos un alias 'np' para facilitar su uso
import numpy as np

def procesar_estadisticas(lista_mensajes):
    """
    Función que recibe datos y utiliza funciones externas de 
    la biblioteca NumPy para procesarlos.
    """
    # Invocación de función externa para el promedio
    promedio = np.mean(lista_mensajes)
    
    # Invocación de función externa para encontrar el valor máximo
    pico_maximo = np.max(lista_mensajes)
    
    # Invocación de función externa para la desviación estándar
    desviacion = np.std(lista_mensajes)

    #Calculo de la mediana
    mediana = np.median(lista_mensajes)
    
    return promedio, pico_maximo, desviacion, mediana

def main():
    # Ejemplo de datos de mensajes (pueden ser números representando la cantidad de mensajes por día)
    datos_mensajes = [10, 20, 15, 30, 25]
    
    # Procesamos las estadísticas utilizando la función definida
    promedio, pico_maximo, desviacion, mediana = procesar_estadisticas(datos_mensajes)
    
    # Imprimimos los resultados
    print(f"Promedio de mensajes: {promedio}")
    print(f"Pico máximo de mensajes: {pico_maximo}")
    print(f"Desviación estándar de mensajes: {desviacion}")
    print(f"Mediana de mensajes: {np.round(mediana)}")


if __name__ == "__main__":
    main()