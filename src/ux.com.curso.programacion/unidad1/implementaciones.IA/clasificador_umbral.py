# =================================================================
# TÍTULO: Sistema Modular de Clasificación por Umbral (IA Básica)
# DESCRIPCIÓN: Ejemplo de programación estructurada aplicada a IA.
# =================================================================

def obtener_datos_entrada():
    """
    MODULO 1: Captura de Datos.
    Simula la entrada de señales o sensores.
    """
    print("--- Fase de Entrada de Señales ---")
    valor = float(input("Introduce el valor de la señal detectada: "))
    return valor

def procesar_clasificacion(valor_senal, umbral=0.5):
    """
    MODULO 2: Motor de Decisión (Lógica de IA).
    Aplica una función de activación simple (paso unitario).
    """
    # Si la señal supera el umbral, la "neurona" se activa (1), si no, permanece inactiva (0)
    if valor_senal >= umbral:
        return True, "ACTIVA (Categoría A)"
    else:
        return False, "INACTIVA (Categoría B)"

def mostrar_reporte(valor, resultado_bool, etiqueta):
    """
    MODULO 3: Salida y Visualización.
    Muestra los resultados de forma predecible.
    """
    print("\n" + "="*30)
    print(f"REPORTE DEL CLASIFICADOR")
    print("="*30)
    print(f"Señal analizada: {valor}")
    print(f"Estado lógico:   {resultado_bool}")
    print(f"Clasificación:   {etiqueta}")
    print("="*30)

def main():
    """
    ORQUESTADOR: Controla el flujo del programa.
    Mantiene el código escalable y fácil de probar.
    """
    # 1. Entrada
    senal = obtener_datos_entrada()
    
    # 2. Procesamiento (Usamos un umbral definido para el experimento)
    es_activa, nombre_clase = procesar_clasificacion(senal, umbral=1.0)
    
    # 3. Salida
    mostrar_reporte(senal, es_activa, nombre_clase)

# Punto de entrada del script
if __name__ == "__main__":
    main()