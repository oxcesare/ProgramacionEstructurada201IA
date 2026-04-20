# Archivo: calculos.py
# Este archivo contiene solo lógica matemática para nuestra IA

def calcular_error_lineal(valor_real, valor_predicho):
    """
    Calcula la diferencia absoluta entre la realidad y la prediccion.
    Es una métrica básica en modelos de regresión.
    """
    error = valor_real - valor_predicho
    # Usamos abs() para obtener el valor absoluto
    return abs(error)

def calcular_precision(total_ejemplos, aciertos):
    """
    Calcula el porcentaje de precisión del modelo.
    Evita la división por cero si la lista está vacía.
    """
    if total_ejemplos == 0:
        return 0.0
    
    precision = (aciertos / total_ejemplos) * 100
    return round(precision, 2)

def predecir_simple(valor_entrada, peso):
    """
    Simula una neurona simple (Entrada * Peso).
    """
    return valor_entrada * peso