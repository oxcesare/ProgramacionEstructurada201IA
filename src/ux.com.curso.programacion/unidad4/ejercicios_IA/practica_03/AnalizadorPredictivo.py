# --- SOLUCIÓN: SISTEMA DE MONITOREO INDUSTRIAL ---

def limpiar_dato(lectura):
    """
    FUNCIÓN 1: Limpieza y validación.
    Convierte el texto a número y descarta valores fuera de rango (ruido).
    """
    try:
        # Convertimos la cadena a número flotante
        valor = float(lectura)
        
        # Filtramos valores que no tienen sentido físico (Ruido del sensor)
        if valor < 0 or valor > 100:
            return None
        
        return valor
    except ValueError:
        # Si la línea tiene texto no numérico o está vacía, retornamos None
        return None

def calcular_alerta(valor_normalizado):
    """
    FUNCIÓN 2: Clasificación de estados basada en umbrales.
    Simula la decisión de un clasificador de IA sencillo.
    """
    if valor_normalizado > 0.8:
        return "CRÍTICO"
    elif valor_normalizado > 0.5:
        return "PRECAUCIÓN"
    else:
        return "NORMAL"

def obtener_estadisticas(lista_datos):
    """
    FUNCIÓN 3: Análisis descriptivo.
    Retorna una tupla con los indicadores clave del lote de datos.
    """
    if not lista_datos:
        return (0, 0, 0)
    
    maximo = max(lista_datos)
    minimo = min(lista_datos)
    promedio = sum(lista_datos) / len(lista_datos)
    
    return (maximo, minimo, promedio)

def generar_reporte(total_datos, validos, estadisticas):
    """
    FUNCIÓN 4: Salida de resultados.
    Formatea la información para el usuario final.
    """
    # Desempaquetamos la tupla de estadísticas
    v_max, v_min, v_prom = estadisticas
    descartados = total_datos - validos
    
    print("-" * 40)
    print("REPORTE DE MANTENIMIENTO PREDICTIVO")
    print("-" * 40)
    print(f"Lecturas procesadas: {total_datos}")
    print(f"Datos válidos:       {validos}")
    print(f"Ruido descartado:    {descartados}")
    print("-" * 20)
    print(f"Temperatura Máxima:  {v_max:.2f}")
    print(f"Temperatura Mínima:  {v_min:.2f}")
    print(f"Temperatura Promedio: {v_prom:.2f}")
    print("-" * 20)
    
    # Ejemplo de uso de la función de alerta con el promedio
    estado_general = calcular_alerta(v_prom)
    print(f"ESTADO DEL SISTEMA:  [{estado_general}]")
    print("-" * 40)

# --- LÓGICA PRINCIPAL (Pipeline de datos) ---
import os 

def ejecutar_pipeline():
    datos_finales = []
    cuenta_total = 0
    
    # Obtener la ruta absoluta del archivo en la misma carpeta que el script
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, "lecturas_sensores.txt")

    # Intentamos abrir el archivo de datos
    try:
        with open(ruta_archivo, "r") as f:
            for linea in f:
                cuenta_total += 1
                # Llamada a Función 1
                valor = limpiar_dato(linea.strip())
                
                if valor is not None:
                    # Normalización a rango 0-1 (Preparación para IA)
                    datos_finales.append(valor / 100)
        
        if datos_finales:
            # Llamada a Función 3
            stats = obtener_estadisticas(datos_finales)
            # Llamada a Función 4
            generar_reporte(cuenta_total, len(datos_finales), stats)
        else:
            print("Error: No se encontraron datos válidos para procesar.")
            
    except FileNotFoundError:
        print("Error: El archivo 'lecturas_sensores.txt' no existe.")

if __name__ == "__main__":
    ejecutar_pipeline()