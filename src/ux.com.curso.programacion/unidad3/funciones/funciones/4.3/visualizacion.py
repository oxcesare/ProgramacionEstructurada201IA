# -----------------------------------------------------------------
# SECCIÓN 2: "Simulación del archivo visualizacion.py"
# -----------------------------------------------------------------

def imprimir_encabezado(titulo):
    """Imprime un título decorado para la consola."""
    print("\n" + "=" * 50)
    print(f" {titulo.upper()} ".center(50, "="))
    print("=" * 50)

def reporte_ia(nombre_modelo, error, precision):
    """Muestra un resumen de métricas organizado."""
    print(f"Resultados del modelo: {nombre_modelo}")
    print(f"- Error detectado: {error:.4f}")
    print(f"- Precisión final: {precision}%")
    
    if precision > 80:
        print("Estado: MODELO ÓPTIMO")
    else:
        print("Estado: REQUIERE MÁS ENTRENAMIENTO")
    print("-" * 50)