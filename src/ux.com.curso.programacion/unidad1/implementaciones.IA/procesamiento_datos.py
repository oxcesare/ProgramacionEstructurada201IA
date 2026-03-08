# =================================================================
# TÍTULO: Filtro de Preprocesamiento de Datos para IA
# CONCEPTO: Limpieza y Normalización Estructurada
# =================================================================

def capturar_lectura_sensor():
    """ MODULO 1: Adquisición de Datos. """
    return float(input("Ingrese valor del sensor (0-100): "))

def validar_y_limpiar(valor):
    """ 
    MODULO 2: Limpieza de Datos (Outlier Detection).
    Si el dato es ruidoso (fuera de rango), se descarta o corrige.
    """
    if 0 <= valor <= 100:
        return True, valor  # Dato válido
    else:
        return False, 0.0   # Dato ruidoso (Outlier)

def normalizar_dato(valor):
    """ MODULO 3: Transformación (Escalamiento a rango 0-1). """
    return valor / 100

def main():
    """ ORQUESTADOR: Flujo Estructurado del Pipeline de IA. """
    dato_crudo = capturar_lectura_sensor()
    
    es_valido, dato_limpio = validar_y_limpiar(dato_crudo)
    
    if es_valido:
        dato_final = normalizar_dato(dato_limpio)
        print(f"Dato listo para la Red Neuronal: {dato_final}")
    else:
        print("Alerta: Ruido detectado. Dato descartado.")

if __name__ == "__main__":
    main()