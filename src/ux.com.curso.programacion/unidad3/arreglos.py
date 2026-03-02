import utilerias as util

print("arreglos")

def crear_arreglo():
    arreglo = [1, 2, 3, 4, 5]
    return arreglo


def imprimir_arreglo(arreglo):
    for elemento in arreglo:
        print(elemento)

# invocamos la funcion para crear el arreglo
mi_arreglo = crear_arreglo()
# invocamos la funcion para imprimir el arreglo
imprimir_arreglo(mi_arreglo)        
# invocamos la funcion para mostrar la cadena
util.mostrarCadena()