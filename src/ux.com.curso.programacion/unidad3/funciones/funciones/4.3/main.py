import visualizacion as visual
import calculos as calc


def ejecutar_simulacion():
    # 1. Preparar la interfaz (Usando funciones de visualización)
    visual.imprimir_encabezado("Simulador de Neurona para Ingeniería en IA")
    
    # 2. Datos de prueba (Entrada, Peso, Valor Real)
    dato_entrada = 10.5
    peso_sinaptico = 0.85
    valor_real_esperado = 9.2
    
    # 3. Realizar predicción (Usando funciones de cálculos)
    prediccion = calc.predecir_simple(dato_entrada, peso_sinaptico)
    
    # 4. Calcular métricas (Usando funciones de cálculos)
    error = calc.calcular_error_lineal(valor_real_esperado, prediccion)
    # Simulamos que de 200 pruebas, acertó en 175
    precision = calc.calcular_precision(200, 175)
    
    # 5. Mostrar resultados (Usando funciones de visualización)
    print(f"Entrada: {dato_entrada} | Predicción calculada: {prediccion:.4f}")
    visual.reporte_ia("Perceptrón de Prueba", error, precision)

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    ejecutar_simulacion()