"""
Generador de Secuencias Impares: Diseñar un algoritmo que 
imprima los primeros N números impares, donde N es ingresado por el usuario.
"""
def generador_secuencias():
    N = int(input("Ingrese el número de secuencias impares que desea generar: "))
    contador =0
    numero =1 
    while  contador < N:
        print(numero)
        numero += 2
        contador += 1   
    return numero

def main():
    generador_secuencias()

if __name__ == "__main__":
    main()

     