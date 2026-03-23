#Suma Condicional de Rango Fijo

def suma_condicional():
    suma=0
    i = 1

    while(i<=100):
        if (i%3==0 and i%2 !=0):
            suma+=i
            i = i+1
        else:
            i = i+1
    print("La suma de los números impares múltiplos de 3 entre 1 y 100 es: ",suma)

def main():
    suma_condicional()  

if __name__ == "__main__":
    main()