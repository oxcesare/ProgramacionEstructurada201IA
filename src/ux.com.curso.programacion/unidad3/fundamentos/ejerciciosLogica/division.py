"""
Pasos del Procedimiento

Inicializar un contador en 0 (este será nuestro cociente).

Restar el divisor ($B$) al dividendo ($A$).

Verificar el resultado:

Si el resultado es mayor o igual a cero:

Incrementar el contador en 1.

El nuevo valor del dividendo es el resultado de la resta.

Repetir desde el paso 2.

Si el resultado es menor a cero:

El proceso termina.
"""

def division(divisor, dividendo):
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    
    return cociente

def division_2(divisor, dividendo):

    #Inicializar un contador en 0 (este será nuestro cociente).
    cociente = 0    
    #Restar el divisor ($B$) al dividendo ($A$).
    resultado = dividendo - divisor

    while(resultado >= 0):
        #Incrementar el contador en 1.
        cociente += 1
        #El nuevo valor del dividendo es el resultado de la resta.
        resultado -= divisor
    
    return cociente

def main():
    A = 10
    B = 3
    resultado = division_2(B, A)
    print(f"El resultado de dividir {A} entre {B} es: {resultado}")

if __name__ == "__main__":
    main()