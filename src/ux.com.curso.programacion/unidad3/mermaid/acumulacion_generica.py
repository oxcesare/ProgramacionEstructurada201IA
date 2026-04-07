# Algoritmo de acumulación genérica
def acumulacion_genérica(n):
    suma=0    
    while suma <500:
        numero = int(input("Ingrese un número: "))
        suma += numero
    return suma    

def main():
    resultado = acumulacion_genérica(500)
    print("La suma acumulada es:", resultado)   

if __name__ == "__main__":
    main()        
            
