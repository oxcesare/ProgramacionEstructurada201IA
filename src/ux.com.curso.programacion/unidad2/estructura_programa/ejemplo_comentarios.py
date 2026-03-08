"""
SINTANXIS MULTILINEA
Este modulo simula funcion de activiacion de una neurona 
Si la entrada superr el umbral (0.5), la neurona se dispara
"""

def acivar_neurona(valor_entrada):
    umbral =0.5 # Definimos el limite de decision (Comentario de línea)
    if valor_entrada > umbral:
        return 1 
    else:
        return 0 # Retorna 0 si no se supera el umbral
    

#ejecuccion principal 
entrada=0.7
resultado = acivar_neurona(entrada)

print(f"Valor de entrada: {entrada}, Neurona activada: {resultado}")