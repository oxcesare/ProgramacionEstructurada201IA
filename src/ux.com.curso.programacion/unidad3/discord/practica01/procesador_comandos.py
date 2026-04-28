import datetime

def obtener_saludo(nombre_bot):
    """
      Retorna un saludo formateado
    """
    return f"Hola, soy {nombre_bot} y estoy listo para ayudarte."

def procesar_comando_recordar(comando):
    """
       Valida y procesa la accion de recordar un dato
    """
    if not comando:
        return "Error: falta el nombre. Uso !recordar [nombre]"

    return f"¡Entendido! Recordaré el nombre: {comando}"

def calcular_uptime(hora_inicio):
    """
       Calcula la diferencia de tiempo entre el inicio
       y el actual (mostrar actividad del boot)
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"Tiempo de actividad: {segundos} segundos"



def main():
    obtener_saludo("DiscordBot")

if __name__ == "__main__":
    main()    

