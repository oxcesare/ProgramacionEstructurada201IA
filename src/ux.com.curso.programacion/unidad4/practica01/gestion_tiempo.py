# 1. IMPORTACIÓN (Biblioteca Estándar)
import datetime

def calcular_dias_restantes(fecha_evento_str):
    """
    Función que utiliza la biblioteca datetime para calcular la 
    diferencia entre hoy y una fecha futura.
    """
    # Obtener la fecha y hora actual del sistema (Función externa)
    ahora = datetime.datetime.now()
    
    # Convertir un texto (string) a un objeto de fecha real
    fecha_evento = datetime.datetime.strptime(fecha_evento_str, "%d/%m/%Y")
    
    # Operación entre objetos de tiempo (Parámetros de salida implícitos)
    diferencia = fecha_evento - ahora
    
    return diferencia.days

#Implementar este formato Hoy es día: [Día] del mes: [Mes]".

def imprimir_fecha_formato(fecha_evento_str):
    """
    Función que utiliza la biblioteca datetime para calcular la 
    diferencia entre hoy y una fecha futura.
    """
    # Obtener la fecha y hora actual del sistema (Función externa)
    ahora = datetime.datetime.now()
    
    # Convertir un texto (string) a un objeto de fecha real
    fecha_evento = datetime.datetime.strftime(ahora, "Hoy es día: %d del mes: %m")
    
    
    return fecha_evento

def saludar_usuario(nombre):

    ahora = datetime.datetime.now()

    #Antes de las 12 
    if ahora.hour < 12:
        saludo = f"¡Buenos días, {nombre}!"
    else:
        saludo = f"¡Buenas tardes, {nombre}!"

def main():

    # --- Programa Principal ---
    # Definimos la fecha de nuestro próximo torneo en Discord (Día/Mes/Año)
    fecha_torneo = "15/05/2025"

    # Invocación y paso de parámetros
    dias = calcular_dias_restantes(fecha_torneo)

    if dias <0:
        print("El evento ya ha pasado.")
        return
        

    print("=== SISTEMA DE EVENTOS DISCORD ===")
    print(f"Fecha del evento: {fecha_torneo}")
    print(f"Estado: Faltan exactamente {dias} días para el inicio.")

    
if __name__ == "__main__":
    main()    
