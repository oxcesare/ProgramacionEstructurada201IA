# Normalizacion de datos

#Constantes: Define UMBRAL_BAJO = 0.3 y UMBRAL_ALTO = 0.7.
UMBRAL_BAJO = 0.3
UMBRAL_ALTO = 0.7

def clasificar_pixel(intensidad_pixel):
    # Retorna la clasificación como cadena, o None si es inválido
    if intensidad_pixel < 0.0 or intensidad_pixel > 1.0:
        return None
    if 0.0 <= intensidad_pixel <= UMBRAL_BAJO:
        return "Fondo (Oscuro)"
    elif UMBRAL_BAJO < intensidad_pixel < UMBRAL_ALTO:
        return "Gris (Ruido)"
    elif intensidad_pixel >= UMBRAL_ALTO:
        return "Objeto (Brillante)"


import os

def cargar_y_procesar(nombre_archivo):
    datos_limpios = []
    ruido_detectado = 0
    fondo_oscuro = 0
    gris_ruido = 0
    objeto_brillante = 0

    # Obtener la ruta absoluta del archivo en la misma carpeta que el script
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)

    try:
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                # Convertir cada línea a número flotante
                valor_crudo = float(linea.strip())

                # Clasificar el pixel
                resultado = clasificar_pixel(valor_crudo)

                if resultado is None:
                    ruido_detectado += 1
                else:
                    datos_limpios.append(resultado)
                    if resultado == "Fondo (Oscuro)":
                        fondo_oscuro += 1
                    elif resultado == "Gris (Ruido)":
                        gris_ruido += 1
                    elif resultado == "Objeto (Brillante)":
                        objeto_brillante += 1

        print(f"--- Reporte de Ingeniería ---")
        print(f"Total de lecturas procesadas: {len(datos_limpios) + ruido_detectado}")
        print(f"Datos válidos (Normalizados): {len(datos_limpios)}")
        print(f"Anomalías descartadas: {ruido_detectado}")
        print(f"Fondo (Oscuro): {fondo_oscuro}")
        print(f"Gris (Ruido): {gris_ruido}")
        print(f"Objeto (Brillante): {objeto_brillante}")
        print(f"Primeros 10 datos para la IA: {datos_limpios[:10]}")

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe en {ruta_script}.")

# Llamada a la función para ejecutar el programa
def main():
    #  Cargar el archivo lecturas_sensores.txt y procesar los datos
    cargar_y_procesar("lecturas_sensores.txt")

if __name__ == "__main__":
    main()