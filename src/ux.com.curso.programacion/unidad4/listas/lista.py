# Ejemplo de listas en Python


#Crea una lista vacía llamada pendientes.
pendientes = []

#Implementa una función que permita añadir 3 tareas a la lista usando .append().
def agregar_tareas():
    pendientes.append("Comprar leche")
    pendientes.append("Lavar el coche")
    pendientes.append("Estudiar para el examen")

    #Ordena la lista alfabéticamente con .sort().
    pendientes.sort()

    #Elimina la segunda tarea de la lista usando pop() o remove().
    pendientes.pop(1)  # Elimina la tarea en el índice 1 (segunda tarea)

def main():
    agregar_tareas()
    print("Tareas pendientes:")
    for tarea in pendientes:
        print(f"  - {tarea}")

if __name__ == "__main__":
    main()