import datetime

def agregar_tarea(lista_tareas,descripcion):
    """
      Agregar una tarea a la lista si cumple con los requisitos
    """

    if len(descripcion)< 3:
        return "Error: Longitud no valida"
    
    # crear formato para tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con exito"

def listar_tareas(lista_tareas):
    """
     Formatea la lista de tareas para su visualización
    """
    if not lista_tareas:
        return "No hay tareas"
    
    # agrega una variable llamada resultado
    resultado = "Listado de tareas: \n"

    #Iterar la lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"
    return resultado   